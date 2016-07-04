# playbook - Ansible Playbooks (new organization)
A collection of Ansible playbooks developed.  New structure has been created:
- [ansible-playbooks](https://github.com/bonovoxly/playbook/tree/master/ansible-playbooks) directory - containers folders of playbooks.
- [ansible-roles](https://github.com/bonovoxly/playbook/tree/master/ansible-roles) directory - all shared roles.

Credentials are stored in an Ansible vault, usually in ```vars/vault.yml```.  Vault file is not uploaded.

- **[amibuilder](https://github.com/bonovoxly/playbook/tree/master/amibuilder)** - A playbook that builds role-based AMI images from a base AMI.
- **[awsbackup](https://github.com/bonovoxly/playbook/tree/master/awsbackup)** - A playbook that snaphots selected instances, including rotation logic.
- **[bastion_host](https://github.com/bonovoxly/playbook/tree/master/bastion_host)** - A playbook that creates a NAT instance to act as a bastion host to internal instances.
- **[ec2_vpc_route_table_issue_test](https://github.com/bonovoxly/playbook/tree/master/ec2_vpc_route_table_issue_test)** - A playbook that exercises a minor ec2_vpc routing NAT bug, when the NAT instance is deleted.
- **[rancher_demo](https://github.com/bonovoxly/playbook/tree/master/rancher-demo)** - A playbook that creates a [Rancher](http://rancher.com/) demo instance, with a Docker hosts.
