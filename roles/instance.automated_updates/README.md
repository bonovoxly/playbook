instance.automated_updates
=========

Configures an Ubuntu system to automatically update at a specified time.  If specified, system will reboot.

Requirements
------------

Ubuntu 16.04 or greater.

Role Variables
--------------

- `update_date` - A systemd formattted date/time to update.
- `reboot` - Boolean value if the system should reboot or not.

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: test
  remote_user: ubuntu
  gather_facts: yes

  roles:
    - role: instance.automated_updates
      update_date: 'Tue, 07:00'
      reboot: true
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
