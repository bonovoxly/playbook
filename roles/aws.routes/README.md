aws.routes
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
- `subnet_facts`
  - From the role `aws.vpc_facts`.
- `vpc.private_route`
  - VPC private route, defined in the `vpc` dictionary.
- `vpc.public_route`
  - VPC public route, defined in the `vpc` dictionary.
- `bastionhost_instance_results.tagged_instances.0.id`
  - The results of creating the bastionhost instance.

Dependencies
------------

- `aws.bastionhost`
- `aws.vpc_facts`

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
  - role: aws.vpc_facts
    filters:
      "tag:TagValue": KeyValue
  - role: aws.bastionhost
  - role: aws.routes
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
