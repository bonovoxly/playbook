aws.vpc_facts
=========

Collects both VPC and subnet facts. Registers `subnet_facts` and `vpc_id_fact`.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules.

Role Variables
--------------

- `vault.aws_secret_key`
  - AWS secret key.
- `vault.aws_access_key`
  - AWS access key
- `vpc.region`
  - VPC region, defined in the `vpc` dictionary.
- `filters`
  - A dictionary value to limit results.  http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html
- `vpc.resource_tags.Environment`
  - Used to get the VPC ID.

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
    - role: aws.vpc_facts
      filters:
        "tag:TagName": TagValue
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
