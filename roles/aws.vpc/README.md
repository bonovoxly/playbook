aws.vpc
=========

Builds an AWS VPC with subnets.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules.

Role Variables
--------------

Variables required are:

- `vpc.region`
  - VPC region, defined in the `vpc` dictionary.
- `vpc.cidr_block`
  - The VPC CIDR block. Usually a /16.
- `vpc.gateway`
  - The Internet gateway.  Yes or No.
- `vpc.resource_tags`
  - Dictionary of AWS tags.
- `vpc.subnets`
  - A list of dictionaries.
- `vpc.subnets.cidr`
 - The subnet CIDR address.
- `vpc.subnets.az`
  - The availability zone.
- `vpc.subnets.resource_tags`
  - Tags for the subnets.
- `vpc.subnets.resource_tags.Name`
  - Name of the subnet.
- `vpc.subnets.resource_tags.Route`
  - This is used to determine NAT or Internet gateway routing.

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
    # Create and configure VPC
    - role: aws.vpc
```
License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
