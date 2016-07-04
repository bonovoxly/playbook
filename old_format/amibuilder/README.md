# amibuilder.yml playbook

This playbook builds an customized AMI from a base image.  It is used for pre-baking AMIs for various roles. In this example, it only builds a "nginx" role.

Example run:

```
ansible-playbook -i inventory/localhost --vault-password-file ~/.ansible/vault_amibuilder amibuilder.yml -e "ROLE=nginx"
```

# ansible-vault

The Ansible vault file is kept under ```group_vars/all/vault.yml```.  It has the following structure:

```
vault:
  aws_secret_key: SECRET_KEY
  aws_access_key: ACCESS_KEY
  ansible_ssh_key_file: "{{ ansible_env.HOME }}/.ssh/keyfile"
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
