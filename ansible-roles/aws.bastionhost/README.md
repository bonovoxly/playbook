aws.bastionhost
=========

Establishes the AWS settings for a bastion/NAT host.  Does the following:
- Creates the bastionhost security group.
- Tags the security group.
- Gets the bastionhost subnet ID.
- Creates the bastionhost instance.
- Sets the `bastion_public_ip` fact.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules.

Role Variables
--------------

- `vpc.region`
  - VPC region, defined in the `vpc` dictionary.
- `vpc.image`
  - Ubuntu 16.04 AMI image for `us-west-2`.
- `securitygroups_bastionhost`
  - Security group dictionary.
  - `securitygroups_bastionhost.name`
  - `securitygroups_bastionhost.rules`
  - `securitygroups_bastionhost.tags`
- `vpc_id_fact`
  - VPC ID fact, acquired from the role `aws.vpc_facts`.
- `ec2_bastionhost`
  - The bastionhost EC2 dictionary.

Dependencies
------------

- `aws.vpc_facts`

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
    - role: aws.bastionhost
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
