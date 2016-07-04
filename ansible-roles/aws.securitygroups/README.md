aws.securitygroups
=========

Creates the AWS security groups based on a list of security group dictionaries.  Also relies on `aws.bastionhost` to get the source IP address for SSH access.

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
- `vpc_id_fact`
  - The VPC ID.
- `securitygroups`
  - A list of security group dictionaries.
- `bastionhost_instance_results.tagged_instances.0.private_ip`
  - The private IP address from creating the bastionhost instance.

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
      - vars/vault.yml
  - role: aws.vpc_facts
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

Bill Cawthra - http://bonovoxly.github.io/
