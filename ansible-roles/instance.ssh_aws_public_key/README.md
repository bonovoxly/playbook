instance.ssh_aws_public_key
=========

Adds a command to echo out the SSH public key to the AWS System Log.

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

Bill Cawthra - http://bonovoxly.github.io/
