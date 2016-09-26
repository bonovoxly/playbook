instance.packages
=========

Installs variable packages when the lists are defined.  Hope to support apt, pip, and npm.

Requirements
------------

None.

Role Variables
--------------

- `apt_packages` - list of apt packages to install.

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
    - role: ubuntu.raw_install_python
    - role: instance.packages
      apt_packages_vars: "{{ apt }}"

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
