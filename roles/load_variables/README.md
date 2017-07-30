load_variables
=========

Loads a list of variables.  Very straightforward.

Requirements
------------

None.

Role Variables
--------------

- `variables`
 - The list of variables are passed in when the role is called.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: localhost
  connection: local
  gather_facts: yes

  roles:
    - role: load_variables
      variables:
        - vars/aws_infrastructure.yml
        - vars/bastionhost.yml
        - vars/internal_instances.yml
        - vars/vault.yml
```


License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
