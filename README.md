# playbook - Ansible Playbooks (new organization)
A collection of Ansible playbooks developed.  New structure has been created:
- [ansible-playbooks](https://github.com/bonovoxly/playbook/tree/master/ansible-playbooks) directory - containers folders of playbooks.
- [ansible-roles](https://github.com/bonovoxly/playbook/tree/master/ansible-roles) directory - all shared roles.

Credentials are stored in an Ansible vault, usually in ```vars/vault.yml```.  Vault file is not uploaded.

Playbooks:
- **[bastionhost](https://github.com/bonovoxly/playbook/blob/master/ansible-playbooks/bastionhost.yml)** - A playbook that creates a bastion host, allowing SSH access to private instances within a VPC.

Old format:
- **[amibuilder](https://github.com/bonovoxly/playbook/tree/master/old_format/amibuilder)** - A playbook that builds role-based AMI images from a base AMI.
- **[awsbackup](https://github.com/bonovoxly/playbook/tree/master/old_format/awsbackup)** - A playbook that snaphots selected instances, including rotation logic.
- **[ec2_vpc_route_table_issue_test](https://github.com/bonovoxly/playbook/tree/master/old_format/ec2_vpc_route_table_issue_test)** - A playbook that exercises a minor ec2_vpc routing NAT bug, when the NAT instance is deleted.
- **[rancher_demo](https://github.com/bonovoxly/playbook/tree/master/old_format/rancher-demo)** - A playbook that creates a [Rancher](http://rancher.com/) demo instance, with a Docker hosts.
