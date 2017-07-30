aws.ec2
=========

Creates any number of EC2 instances based upon a list of dictionaries. Does the following:
- Gets subnet facts for each dictionary in the `ec2` list.
- Based on the list of dictionaries of the result (`ec2_vpc_subnet_facts`) and the list of dictionaries in `ec2`, creates instances in the appropriate subnets.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules.

Role Variables
--------------

- `vpc.region`
  - VPC region, defined in the `vpc` dictionary.
- `ec2`
  - A list of dictionaries containing instance settings.

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
  - role: aws.ec2
    filters:
      "tag:TagValue": KeyValue
  - role: aws.bastionhost
  - role: aws.securitygroups
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
