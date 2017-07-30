# playbook - Ansible Playbooks
A collection of Ansible playbooks I've developed.  I've reworked the layout to be more in line with [Ansible best practices](http://docs.ansible.com/ansible/latest/playbooks_best_practices.html). The old format is a dedicated branch [found here](https://github.com/bonovoxly/playbook/tree/playbook2.0).

Ansible playbooks:
- **[bastionhost](https://github.com/bonovoxly/playbook/blob/master/bastionhost.yml)** - A playbook that creates a bastion host, allowing SSH access to private instances within a VPC ([blog post here](https://blog.billyc.io/2016/07/05/using-a-bastion-host-to-access-a-private-vpc-in-aws/)).
- **[openvpn](https://github.com/bonovoxly/playbook/blob/master/openvpn.yml)** - A playbook that creates an personal OpenVPN server.
  - [Blog post here](https://blog.billyc.io/2016/12/30/personal-aws-vpn-using-openvpn/)
  - [README here](https://github.com/bonovoxly/playbook/blob/master/docs/openvpn.md)
  - [Docker container created via Ansible-container](https://github.com/bonovoxly/containers/tree/master/openvpn)
- **[vpc_create](https://github.com/bonovoxly/playbook/blob/master/vpc_create.yml)** - A playbook that creates a VPC, with associated subnets and routes. Note, this may conflict with the `bastionhost` playbook, as that requires interaction with AWS routing.
- **[stuffs](https://github.com/bonovoxly/playbook/blob/master/stuffs.yml)** - A playbook that gathers inventory data on all instances and generates a static web page inventory using Hugo ([Blog post here](https://blog.billyc.io/2017/03/14/stuffs---an-aws-inventory-tool/)).


Ansible-container:
- **Moved here - https://github.com/bonovoxly/containers**

Old format:
- **[amibuilder](https://github.com/bonovoxly/playbook/tree/playbook2.0/old_format/amibuilder)** - A playbook that builds role-based AMI images from a base AMI.
- **[awsbackup](https://github.com/bonovoxly/playbook/tree/playbook2.0/old_format/awsbackup)** - A playbook that snaphots selected instances, including rotation logic.
- **[ec2_vpc_route_table_issue_test](https://github.com/bonovoxly/playbook/tree/playbook2.0/old_format/ec2_vpc_route_table_issue_test)** - A playbook that exercises a minor ec2_vpc routing NAT bug, when the NAT instance is deleted.
- **[rancher_demo](https://github.com/bonovoxly/playbook/tree/playbook2.0/old_format/rancher-demo)** - A playbook that creates a [Rancher](http://rancher.com/) demo instance, with a Docker hosts.
