aws.iam
=========

Creates private and public routes, based on AWS tags.  Does the following:
- Creates a VPC Internet Gateway.
- Creates the private routes, using the bastionhost instance ID.
- Creates the public route, using the created VPC Internet Gateway.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules.

Role Variables
--------------

- `vpc.region`
  - VPC region, defined in the `vpc` dictionary.
- `iam`
  - A list of dictionary IAM roles.

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
  - role: aws.iam
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
