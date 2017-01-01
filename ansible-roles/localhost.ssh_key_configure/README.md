localhost.ssh_key_configure
=========

This role configures the AWS SSH keyfile in `~/.ssh/` directory.

Requirements
------------

None.

Role Variables
--------------

- `vault.ansible_ssh_key_file` - the path to the SSH private key file.  
- `vault.ansible_ssh_key_contents` - the contents of the SSH private key file.

Dependencies
------------

None

Example Playbook
----------------

See `bastionhost.yml` or `openvpn.yml`.

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
