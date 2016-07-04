ansible.groups_init
=========

Using the results of `ec2_facts`, adds the instances to the following groups:
- `instances_private` - all private IPs for instances that are found by `aws.ec2_facts`.
- `instances_public` - all public IPs for instances that are found by `aws.ec2_facts`.
- `{{ item.tags.Role }}_private` - all private IPs for instances in their `Role` group.
- `{{ item.tags.Name }}_private` - all private IPs for instances in their `Name` group.
- `{{ item.tags.Name }}_public` - all public IPs for instances in their `Name` group.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules. Uses the AWS CLI.

Role Variables
--------------

- `vault.aws_secret_key`
  - AWS secret key.
- `vault.aws_access_key`
  - AWS access key
- `ec2_facts`
  - From the role `aws.ec2_facts`.

Dependencies
------------

- `aws.ec2_facts`

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
        - vars/internal_instances.yml
        - vars/vault.yml
    - role: aws.ec2_facts
      filters:
        "tag:Organization": b_dev
    - role: ansible.groups_init
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
