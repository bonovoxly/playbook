instance.node
=========

Deploys the Kubernetes nodes (kubelets). Deploys the Kubernetes CNI plugin. Configures kubectl on the nodes as well.

Requirements
------------

- Must be an EC2 instances, as it uses the EC2 facts to get the current IP address.

Role Variables
--------------

- `docker_version` - the Docker version to use.
- `env` - the Environment tag passed in. Used for identification/labeling.
- `kubernetes_cni_version` - the Kubernetes CNI version to use.
- `kubernetes_version` - the Kubernetes version to use.
- `token_csv` - username and password variable for configuring kubectl access.  Default values are provided and should NOT be used.  It is recommended to create an Ansible vault file with different credentials to override these.


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
