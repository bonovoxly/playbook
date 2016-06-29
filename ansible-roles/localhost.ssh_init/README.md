localhost.ssh_init
=========

Retreives the SSH keys for all instances and adds them to the localhost's `~/.ssh/known_hosts` file.  Does the following:
- Touches the `~/.ssh/config` file.
- Removes previous entries out of `~/.ssh/config` by searching for text within the comments `# {{ vpc.resource_tags.Organization }}`.
- Adds a SSH proxy command within `# {{ vpc.resource_tags.Organization }}`.
- Removes all commented `~/.ssh/known_hosts` entries with `# {{ vpc.resource_tags.Organization }}`
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
    - role: localhost.ssh_init
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
