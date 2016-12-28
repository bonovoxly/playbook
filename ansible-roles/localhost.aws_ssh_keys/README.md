localhost.aws_ssh_keys
=========

Retreives the SSH keys for all instances and adds them to the localhost's `~/.ssh/known_hosts` file.  Does the following:
- Removes all commented `~/.ssh/known_hosts` entries with `# {{ marker_vars|default(vpc.resource_tags.Organization) }}`
- Gets the SSH fingerprints for all instances using `aws ec2 get-console-output`.
- Imports the private and public IP address and fingerpints for those instances into `~/.ssh/known_hosts`.

Requirements
------------

Boto and any software required to run Ansible AWS cloud modules. Uses the AWS CLI.

Role Variables
--------------

- `vault.aws_secret_key`
  - AWS secret key.
- `vault.aws_access_key`
  - AWS access key
- `vpc`
  - The `vpc` dictionary.
- `ec2_facts`
  - From the role `aws.ec2_facts`.
- An optional `marker_vars` variable.

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
    - role: localhost.aws_ssh_keys
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
