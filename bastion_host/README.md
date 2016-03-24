# bastion host example playbook

This playbook builds 3 instances: A NAT instance and two internal instances.  It does this while configuring the localhost to be able to SSH to all three instances using the NAT instance as an SSH proxy.

There are two playbooks:  ```bastion_host.yml``` and ```bastion_host_advanced.yml```. The advanced script regenerates the SSH fingerprint for each host.

Example run:

```
ansible-playbook bastion_host.yml
```

# ansible-vault

The Ansible vault file is kept under ```host_vars/127.0.0.1/vault.yml```.  It has the following structure:

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
