# ansible-playbooks

Previous playbooks used implicit variable loading.  Trying to avoid that with these playbooks, as all playbooks now have to explicitly load variables using the `load_variables` role. Credentials are stored in an Ansible vault, usually in ```vars/vault.yml```.  Vault file is not uploaded.

- **[bastion_host](https://github.com/bonovoxly/playbook/tree/master/ansible-playbooks/bastion_host)** - A playbook that creates a NAT instance to act as a bastion host to internal instances.


# Prerequisites

- Ansible 2.1
- AWS CLI tools

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
