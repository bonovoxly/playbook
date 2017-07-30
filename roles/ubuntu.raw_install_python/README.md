ubuntu.raw_install_python
=========

Using the Ansible raw module, installs Python on the system.  Usually needed on brand new AMIs.

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
- hosts: bastionhost_public
  become: yes
  gather_facts: no
  user: ubuntu

  roles:
    - role: ubuntu.raw_install_python
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
