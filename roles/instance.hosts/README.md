instance.hosts
=========

Configures /etc/hosts file and sets the hostname.

Requirements
------------

Requires the Python boto package.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

```
- hosts: test
  remote_user: ubuntu
  gather_facts: yes

  roles:
    - role: instance.hosts
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
