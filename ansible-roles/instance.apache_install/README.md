instance.apache_install
=========

Just a basic role that installs Apache on Ubuntu. Made for testing purposes.

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
- hosts: internal_instances
  become: yes
  gather_facts: no
  user: ubuntu

  roles:
    - role: instance.apache_install
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
