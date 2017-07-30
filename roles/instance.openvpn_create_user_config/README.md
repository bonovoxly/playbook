instance.openvpn_create_user_config
=========

Creates a user OpenVPN config file and copies it locally to the Desktop. Uses the Docker image found here: https://hub.docker.com/r/modops/openvpn-openvpn/

Requirements
------------

Docker installed and the custom OpenVPN Docker container installed.

Role Variables
--------------

-`openvpn_user` - The OpenVPN user to create a public/private key pair for, as well as the OpenVPN configuration file.

Dependencies
------------

The `instance.openvpn_configure` role must be used to deploy OpenVPN.  The OpenVPN Docker image based on https://hub.docker.com/r/modops/openvpn-openvpn/ must be used.

Example Playbook
----------------

See `openvpn.yml` playbook.

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
