# ansible-playbooks

- **[bastion_host](https://github.com/bonovoxly/playbook/tree/master/ansible-playbooks/bastion_host)** - A playbook that creates a NAT instance to act as a bastion host to internal instances ([blog post here](http://bonovoxly.github.io/2016-07-05-bastion-host-private-vpc-aws)).
- **[openvpn](https://github.com/bonovoxly/playbook/blob/master/ansible-playbooks/openvpn.yml)** - A playbook that deploys a personal OpenVPN server ([blog post here](http://bonovoxly.github.io/2016-12-30-personal-aws-vpn-using-openvpn)).
- **[openvpn_terraform](https://github.com/bonovoxly/playbook/blob/master/ansible-playbooks/openvpn_terraform.yml)** - Using Terraform to first provision, a playbook that deploys a personal OpenVPN server ([blog post here](http://bonovoxly.github.io/2016-12-30-personal-aws-vpn-using-openvpn)).
- **[kubernetes](https://github.com/bonovoxly/playbook/blob/master/ansible-playbooks/kubernetes.yml)** - A playbook that configures a Terraform deployed Kubernetes stack ([blog post here](http://bonovoxly.github.io/2017-02-27-another-terraform-ansible-kubernetes))
- **[stuffs](https://github.com/bonovoxly/playbook/blob/master/ansible-playbooks/stuffs.yml)** - A playbook that gathers inventory data on all instances and generates a static web page inventory using Hugo ([Blog post here](http://bonovoxly.github.io/2017-03-14-stuffs-inventory-tool)).


# Prerequisites

- Ansible 2.1 (or greater)
- AWS CLI tools
- AWS access/secret key configured
- SSH key configured (with the public key uploaded to AWS)
- AWS SSH key pair - this should be set in the `ansible.cfg` file.
- An `ansible.cfg` file (your settings may vary):

```
# Example ansible.cfg
[defaults]
inventory = ./inventory
roles_path = ../ansible-roles

[ssh_connection]
control_path = %(directory)s/ssh-%%C
```

- Configure your AWS access and secret keys as environment variables:

```
export AWS_ACCESS_KEY_ID=123yourkey789
export AWS_SECRET_ACCESS_KEY=1234567tiyrsecret456789
```

The `vault` variable requirements have been removed.

# AWS policy

Consider restricting policies accordingly, but in general, these playbooks require the Administrator policy.
