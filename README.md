# playbooks
A collection of Ansible playbooks developed.  Credentials are stored in an Ansible vault, usually in group_vars/all/vault.yml.

- **amibuilder** - A playbook that builds role-based AMI images from a base AMI.
- **awsbackup** - A playbook that snaphots selected instances, including rotation logic.
- **ec2_vpc_route_table_issue_test** - A playbook that exercises a minor ec2_vpc routing NAT bug, when the NAT instance is deleted.
