# ansible-playbooks

Previous playbooks used implicit variable loading.  Trying to avoid that with these playbooks, as all playbooks now have to explicitly load variables using the `load_variables` role. Credentials are stored in an Ansible vault, usually in ```vars/vault.yml```.  Vault file is not uploaded.

- **[bastion_host](https://github.com/bonovoxly/playbook/tree/master/ansible-playbooks/bastion_host)** - A playbook that creates a NAT instance to act as a bastion host to internal instances ([blog post here](http://bonovoxly.github.io/2016-07-05-bastion-host-private-vpc-aws)).
- **[openvpn](https://github.com/bonovoxly/playbook/blob/master/ansible-playbooks/openvpn.yml)** - A playbook that deploys a personal OpenVPN server ([blog post here](http://bonovoxly.github.io/2016-12-30-personal-aws-vpn-using-openvpn)).


# Prerequisites

- Ansible 2.1 (or greater)
- AWS CLI tools
- AWS access/secret key configured
- SSH key configured (with the public key uploaded to AWS)
- AWS SSH key pair

# ansible-vault and required secret variables

Many/most of these playbooks require multiple secrets, including AWS access keys, AWS secret keys, SSH private keys, and IP addresses. Often times, these vary by environment.  Note the `openvpn.yml` playbook uses the `mod` environment, and will load the `vars/mod_aws/vault.yml` vault file.  It has the following structure (but can vary):

```
vault:
  aws_access_key: ACCESS_KEY
  aws_secret_key: SECRET_KEY
  key_pair: AWS_SSH_KEY_NAME
  # SSH key configuration
  ansible_ssh_key_file: "{{ ansible_env.HOME }}/.ssh/awskey"
  ansible_ssh_key_contents: |
    -----BEGIN RSA PRIVATE KEY-----
    KEYDATA
    -----END RSA PRIVATE KEY-----
```

- `aws_access_key` - the AWS access key.
- `aws_secret_key` - the AWS secret key.
- `key_pair` - the name of the SSH public key that is uploaded to AWS.
- `ansible_ssh_key_file` - the path to the SSH key file.  Should match `ansible.cfg`.
- `ansible_ssh_key_contents` - the private SSH key data.

Embedding the SSH key in the Ansible Vault keeps the entire project very modular.


# AWS policy

Consider restricting policies accordingly, but in general, these playbooks require the Administrator policy.
