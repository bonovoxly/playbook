# playbooks
A collection of Ansible playbooks developed.  Credentials are stored in an Ansible vault, usually in ```group_vars/all/vault.yml``` or host_vars/127.0.0.1/vault.yml```.

- **[amibuilder](https://github.com/bonovoxly/playbook/tree/master/amibuilder)** - A playbook that builds role-based AMI images from a base AMI.
- **[awsbackup](https://github.com/bonovoxly/playbook/tree/master/awsbackup)** - A playbook that snaphots selected instances, including rotation logic.
- **[bastion_host](https://github.com/bonovoxly/playbook/tree/master/bastion_host)** - A playbook that creates a NAT instance to act as a bastion host to internal instances.
- **[ec2_vpc_route_table_issue_test](https://github.com/bonovoxly/playbook/tree/master/ec2_vpc_route_table_issue_test)** - A playbook that exercises a minor ec2_vpc routing NAT bug, when the NAT instance is deleted.
- **[rancher_demo](https://github.com/bonovoxly/playbook/tree/master/rancher-demo)** - A playbook that creates a [Rancher](http://rancher.com/) demo instance, with a Docker hosts.
