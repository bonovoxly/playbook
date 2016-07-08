instance.ssh_fingerprint
=========

Adds a command to echo out the SSH fingerprint to the AWS System Log.

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
    - role: instance.ssh_fingerprint
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
