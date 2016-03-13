# awsbackup.yml and awsbackup.py

This is both an awsbackup.yml playbook and the equivalent awsbackup.py python script.  I wanted to share both as they are nearly identical in functionality.

Example run:

```
ansible-playbook --vault-password-file ~/.ansible/myvaultpassword -i inventory/localhost awsbackup.yml -e "INCREMENTAL=daily COUNT=3"
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
                "ec2:CreateSnapshot",
                "ec2:CreateTags",
                "ec2:DeleteSnapshot",
                "ec2:CreateVolume",
                "ec2:Describe*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```
