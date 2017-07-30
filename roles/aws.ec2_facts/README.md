aws.ec2_facts
=========

Collects facts on instances in the region, based on filters passed in.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules.

Role Variables
--------------

- `vpc.region`
  - VPC region, defined in the `vpc` dictionary.
- `filters`
  - A dictionary value to limit results.  http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html

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
      - vars/vault.yml
  - role: aws.ec2_facts
    filters:
      "tag:TagValue": KeyValue
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
