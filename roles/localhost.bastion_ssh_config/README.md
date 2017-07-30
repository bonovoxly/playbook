localhost.bastion_ssh_config
=========

Updates the `~/.ssh/config` file.  Does the following:
- Touches the `~/.ssh/config` file.
- Removes previous entries out of `~/.ssh/config` by searching for text within the comments `# {{ marker_vars|default(vpc.resource_tags.Organization) }}`. Note that `marker_vars` can be passed into the role to override the default.
- Adds a SSH proxy command within `# {{ marker_vars|default(vpc.resource_tags.Organization) }}`.
- The bastion host to use is passed in to the role using the `bastion_public_dns_name` variable.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules. Uses the AWS CLI.

Role Variables
--------------

- `vpc`
  - The `vpc` dictionary.
- `ec2_facts`
  - From the role `aws.ec2_facts`.
- `bastion_vars` - the hostname or IP address of the bastion host to use. This is passed in as `bastion_public_dns_name`, which is set from the role `aws.bastionhost`.
- `route53.domain` - the domain suffix.  For the Oregon region, it's `compute.internal`.  For Northern Virginia, it's `ec2.internal`.

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
    - role: aws.ec2_facts
      filters:
        "tag:Organization": b_dev
    - role: localhost.bastion_ssh_config
      bastion_vars: "{{ hostname }}"
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
