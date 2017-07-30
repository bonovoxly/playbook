instance.volume
=========

Formats and mounts an EBS volume.  Uses systemd.

Requirements
------------

An EBS volume mount.

Role Variables
--------------

- `volume_name` - defaults to `data`. The friendly volume name for systemd.
- `volume_path` - defaults to `/data`.  The directory where the EBS volume is mounted.
- `filesystem_fstype` - defaults to `ext4`. The filesystem format.
- `filesystem_dev` - defaults to `/dev/xvde`.  The AWS device.  Note this changes from `/dev/sdX` to `/dev/xvdX`.

Dependencies
------------

None.

Example Playbook
----------------

None.

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
