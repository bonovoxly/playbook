instance.controller
=========

Configures the Kubernetes controller plane nodes.

Requirements
------------

- Must be an EC2 instances, as it uses the EC2 facts to get the current IP address.

Role Variables
--------------

- `env` - the Environment tag passed in. Used for identification/labeling.
- `token_csv` - username and password variable for configuring kubectl access.  Default values are provided and should NOT be used.  It is recommended to create an Ansible vault file with different credentials to override these.
- `volume_path` - the path to store the CFSSL files on.  Defaults to `/data`.

Dependencies
------------

- `instance.cfssl_kubernetes` - for SSL certificates.  

Example Playbook
----------------

N/A

License
-------

BSD

Author Information
------------------

Bill Cawthra - http://bonovoxly.github.io/
