# ansible-playbooks

Previous playbooks used implicit variable loading.  Trying to avoid that with these playbooks, as all playbooks now have to explicitly load variables using the `load_variables` role. Credentials are stored in an Ansible vault, usually in ```vars/vault.yml```.  Vault file is not uploaded.

- **[bastion_host](https://github.com/bonovoxly/playbook/tree/master/ansible-playbooks/bastion_host)** - A playbook that creates a NAT instance to act as a bastion host to internal instances.
