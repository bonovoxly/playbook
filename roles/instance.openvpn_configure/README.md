instance.openvpn_configure
=========

Configures the OpenVPN service.

Requirements
------------

Docker installed.

Role Variables
--------------

- `INTERFACE` - the interface that OpenVPN will NAT to.  This is used when the container is run:
```
# configure iptables
${INTERFACE:=eth0}
iptables -t nat -I POSTROUTING -o $INTERFACE -j MASQUERADE
```

Dependencies
------------

- Docker installed.
- Configures a systemd service (this was tested using Ubutnu 16.04). Requires that Docker be installed, in this case, it uses the `instance.docker` role.

Example Playbook
----------------

See `openvpn.yml` playbook.

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
