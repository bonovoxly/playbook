linux.add_user
=========

Creates users from a list of dictionaries.

Requirements
------------

None.

Role Variables
--------------

Variable should be a list of dictionaries such as:

```
users:
  - user: bob
    shell: /bin/bash
    groups: admin
```

Dependencies
------------

None.

Example Playbook
----------------

- hosts: all
  gather_facts: false

  vars_files:
    - vars/all.yml

  roles:
    - role: instance.add_user
      users_vars: "{{ users }}"

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
