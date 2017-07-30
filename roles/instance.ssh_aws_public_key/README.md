instance.ssh_aws_public_key
=========

Adds a command to echo out the SSH public key to the AWS System Log. Also adds the script/command to `/var/lib/cloud/scripts/per-boot/`, in case AWS System Log stops outputting before rc.local runs.

Requirements
------------

None.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: instance
  become: yes
  gather_facts: yesh
  user: ubuntu

  roles:
    - role: instance.ssh_aws_public_key
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
