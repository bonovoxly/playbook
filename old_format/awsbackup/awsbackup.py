#!/usr/bin/env python
import boto.ec2
import logging
import imp
import os
import sys
from configparser import ConfigParser
from datetime import datetime, timedelta
from optparse import OptionParser

class AwsBackups():
  def __init__(self, options, args, profile):
    self.snapdate = datetime.now().strftime("%Y-%m-%d")
    self.readable_date = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    logging.basicConfig(level=logging.INFO)
    self.logger = logging.getLogger()

    self.options = options
    self.options.max = int(self.options.max)
    self.args = args
    self.volumes_to_snap = []
    self.instances_to_snap = {}
    self.log_names_to_snap = {}
    self.log_snapshots_to_delete = []
    self.log_snapshots_created = {}
    region = "us-east-1"
    self.conn = boto.ec2.connect_to_region(region, aws_access_key_id=profile.get(options.profile, 'aws_access_key_id'), \
                                           aws_secret_access_key=profile.get(options.profile, 'aws_secret_access_key'))

  def getInstancesFull(self):
    self.reservations = self.conn.get_all_instances(filters={"tag-key":self.options.key, "tag-value":self.options.tag})
    self.instances = [i for r in self.reservations for i in r.instances]
    for i in self.instances:
      self.volumes_to_snap.extend(v.id for v in self.conn.get_all_volumes() if v.attach_data.instance_id == i.id)
      self.instances_to_snap.update({i:self.volumes_to_snap})
      self.log_names_to_snap.update({i.tags['Name']:self.volumes_to_snap})
      self.volumes_to_snap = []

  def takeSnapshotsFull(self):
    for i in self.instances_to_snap:
      self.volumes_to_snap.extend(v.id for v in self.conn.get_all_volumes() if v.attach_data.instance_id == i.id)
      for v in self.instances_to_snap[i]:
        snapshot = self.conn.create_snapshot(v, "Automated snapshot.")
        myname = i.tags['Name'] + '_daily_' + self.snapdate
        snapshot.add_tags({'Name': myname, self.options.key: self.options.tag, 'identifier': 'awsbackup'})
      self.log_snapshots_created.update({myname:self.volumes_to_snap})
      self.volumes_to_snap = []

  def getSnapshotsFull(self):
    for i in self.instances_to_snap:
      print self.instances_to_snap[i]
      for v in self.conn.get_all_volumes(filters={'attachment.instance-id': i.id}):
        self.deleteSnapshotsFull(v)

  def deleteSnapshotsFull(self, v):
    snapshots = self.conn.get_all_snapshots(filters={'volume-id': v.id, "tag-key":self.options.key, "tag-value":self.options.tag, \
                                            "tag-key":'identifier', "tag-value":'awsbackup'})
    print len(snapshots)
    snap_sorted = sorted([(s.id, s.start_time) for s in snapshots], key=lambda k: k[1])
    print snap_sorted
    for s in snap_sorted[:-self.options.max]:
      self.log_snapshots_to_delete.append(s[0])
      self.conn.delete_snapshot(s[0])

  def reportBackup(self):
    # self.logger.info("<b>AWS snapshot complete.<br> Instances snapshotted: </b>" + str(self.log_names_to_snap.keys()) + "<br>" + \
    #                  "<b>Snapshots created: </b>" + str(self.log_snapshots_created.keys()) + "<br>" + \
    #                  "<b>Snapshots deleted: </b>" + str(self.log_snapshots_to_delete))
    self.logger.info("AWS snapshot script -----------------> Started: " + self.readable_date)
    self.logger.info(sys.argv[0] + " -p " + self.options.profile + " -k " + self.options.key + " -t " + self.options.tag)
    self.logger.info(self.readable_date)
    self.logger.info("AWS snapshot complete.")
    self.logger.info("Snapshots created:")
    for each in self.log_names_to_snap.keys():
      self.logger.info(each)
    for each in self.log_snapshots_created.keys():
      self.logger.info(each)
    try:
      for each in self.log_snapshots_to_delete.keys():
        self.logger.info(each)
    except:
      pass
    self.logger.info("AWS snapshot script -----------------> Complete: " + datetime.now().strftime("%m-%d-%Y %H:%M:%S"))

  def main(self):
    print "Filter key: %s" % self.options.key
    print "Filter tag: %s " % self.options.tag
    self.getInstancesFull()
    self.takeSnapshotsFull()
    self.getSnapshotsFull()
    self.reportBackup()

def parseit():
  parser = OptionParser()
  parser.add_option("-a", "--all", action="store", dest="all", default="default",
    		    help="Makes a backup of all found volumes that are in use.")
  parser.add_option("-p", "--profile", action="store", dest="profile", default="default",
    		    help="The INI profile to select.  Reads profiles from ~/.aws/credentials")
  parser.add_option("-k", "--key", action="store", dest="key", default="Environment",
    		    help="The tag key.  Defaults to Environment.")
  parser.add_option("-m", "--max", action="store", dest="max", default="3",
    		    help="Maximum snapshots to keep.  Defaults to 3.")
  parser.add_option("-t", "--tag", action="store", dest="tag", default="default",
    		    help="The tag value.  Defaults to default.")
  (options, args) =  parser.parse_args()
  profile = ConfigParser()
  try:
    profile.read(os.path.expanduser('~/.aws/credentials'))
  except:
    print "Missing AWS credentials file.  Exiting."
    parser.print_help()
  try:
    profile.get(options.profile, 'aws_access_key_id')
    profile.get(options.profile, 'aws_secret_access_key')
  except:
    print "Profile %s doesn't exist.  Exiting." % options.profile
    parser.print_help()

  return (options, args, profile)

def run():
  (options, args, profile) = parseit()
  x = AwsBackups(options, args, profile)
  x.main()

if __name__=='__main__':
  run()
