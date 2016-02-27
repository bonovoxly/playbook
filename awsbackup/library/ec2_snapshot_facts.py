#!/usr/bin/python
#
# This is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This Ansible library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

DOCUMENTATION = '''
---
module: ec2_snapshot_facts
short_description: Gather facts about ec2 volume snapshots in AWS
description:
    - Gather facts about ec2 volume snapshots in AWS
version_added: "2.0"
author: "Rob White (@wimnat)"
options:
  filters:
    description:
      - A dict of filters to apply. Each dict item consists of a filter key and a filter value. See U(http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html) for possible filters.
    required: false
    default: null
notes:
  - By default, the module will return all snapshots, including public ones. To limit results to snapshots owned by the account use the filter 'owner-id'.

extends_documentation_fragment:
    - aws
    - ec2
'''

EXAMPLES = '''
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather facts about all snapshots, including public ones
- ec2_snapshot_facts:

# Gather facts about all snapshots owned by the account 0123456789
- ec2_snapshot_facts:
    filters:
      owner-id: 0123456789

# Gather facts about a particular snapshot using ID
- ec2_snapshot_facts:
    filters:
      snapshot-id: snap-00112233

# Gather facts about any snapshot with a tag key Name and value Example
- ec2_snapshot_facts:
    filters:
      "tag:Name": Example

# Gather facts about any snapshot with an error status
- ec2_snapshot_facts:
    filters:
      status: error

'''

try:
    import boto.ec2
    from boto.exception import BotoServerError
    HAS_BOTO = True
except ImportError:
    HAS_BOTO = False

def get_snapshot_info(snapshot):

    snapshot_info = { 'id': snapshot.id,
                    'start_time': snapshot.start_time,
                    'status': snapshot.status,
                    'description': snapshot.description,
                    'encrypted': snapshot.encrypted,
                    'owner_alias': snapshot.owner_alias,
                    'volume_size': snapshot.volume_size,
                    'volume_id': snapshot.volume_id,
                    'progress': snapshot.progress,
                    'owner_id': snapshot.owner_id,
                    'tags': snapshot.tags,
                  }

    return snapshot_info

def list_ec2_snapshots(connection, module):

    filters = module.params.get("filters")
    snapshot_dict_array = []

    try:
        all_snapshots = connection.get_all_snapshots(filters=filters)
    except BotoServerError as e:
        module.fail_json(msg=e.message)

    for snapshot in all_snapshots:
        snapshot_dict_array.append(get_snapshot_info(snapshot))

    module.exit_json(snapshots=snapshot_dict_array)


def main():
    argument_spec = ec2_argument_spec()
    argument_spec.update(
        dict(
            filters = dict(default=None, type='dict')
        )
    )

    module = AnsibleModule(argument_spec=argument_spec)

    if not HAS_BOTO:
        module.fail_json(msg='boto required for this module')

    region, ec2_url, aws_connect_params = get_aws_connection_info(module)

    if region:
        try:
            connection = connect_to_aws(boto.ec2, region, **aws_connect_params)
        except (boto.exception.NoAuthHandlerFound, StandardError), e:
            module.fail_json(msg=str(e))
    else:
        module.fail_json(msg="region must be specified")

    list_ec2_snapshots(connection, module)

from ansible.module_utils.basic import *
from ansible.module_utils.ec2 import *

if __name__ == '__main__':
    main()
