instance.cfssl
=========

Configures CFSSL on an instance. 

Requirements
------------

- Must be an EC2 instances, as it uses the EC2 facts to get the current IP address.

Role Variables
--------------

- `env` - the Environment tag passed in. Used for identification/labeling.
- `volume_path` - the path to store the CFSSL files on.  Defaults to `/data`.

Dependencies
------------

- `instance.cfssl_kubernetes` - for SSL certificates.  

Example Playbook
----------------

N/A.

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io
