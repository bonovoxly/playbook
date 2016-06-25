# bastion host example playbook

This playbook builds 3 instances: A NAT instance and two internal instances.  It does this while configuring the localhost to be able to SSH to all three instances using the NAT instance as an SSH proxy.

There are two playbooks:  ```bastion_host.yml``` and ```bastion_host_advanced.yml```. The advanced script regenerates the SSH fingerprint for each host (in the future).

Example run:

```
ansible-playbook bastion_host.yml
```

This playbook is also written without pulling implicit variables.  No more automatically loading `host_vars/127.0.0.1/`. Changing the way I do things...

# Prerequisites

- Ansible 2.1
- AWS CLI tools
- Requires the Ansible roles Git repo - https://github.com/bonovoxly/ansible-roles .  These roles should be two directories away (`../../ansible-roles`).
- Recommended to run this from a Docker container...

# ansible-vault

The Ansible vault file is kept under `vars/vault.yml`.  It has the following structure:

```
vault:
  aws_secret_key: SECRET_KEY
  aws_access_key: ACCESS_KEY
  key_pair ssh_private_key_name # needs uploaded to AWS key pair
  ssh_users: |
    list of ssh public keys for users you want to provide access to
  # SSH key infoconfiguration
  ansible_ssh_key_file: "{{ ansible_env.HOME }}/.ssh/ssh_private_key_name"
  ansible_ssh_key_contents: |
    -----BEGIN RSA PRIVATE KEY-----
    KEYDATA
    -----END RSA PRIVATE KEY-----
```

Embedding the SSH key in the Ansible Vault keeps the entire project very modular.


# AWS policy

The following is the AWS policy used to run this playbook.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeAvailabilityZones",
                "ec2:RunInstances",
                "ec2:TerminateInstances",
                "ec2:CreateImage",
                "ec2:CreateTags",
                "ec2:StopInstances",
                "ec2:StartInstances"
            ],
            "Resource": "*"
        }
    ]
}
```
