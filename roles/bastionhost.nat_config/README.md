bastionhost.nat_config
=========

Installs `iptables` and `iptables-persistent`.  Configures `sysctl` for IP forwarding.

Requirements
------------

None.

Role Variables
--------------

- `vpc.cidr_block`
 - Use this variable to define what network can route through the bastionhost instance.
- `iptables-nat.j2`
 - The Jinja template for configuring `iptables`.

Dependencies
------------

None.

Example Playbook
----------------

See [bastionhost.yml](https://github.com/bonovoxly/playbook/blob/bastionhost/ansible-playbooks/bastionhost/bastionhost.yml)

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
