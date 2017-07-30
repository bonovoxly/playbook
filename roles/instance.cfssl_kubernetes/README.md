instance.cfssl_kubernetes
=========

Builds the SSL public/private key x509 certificates for Kubernetes.  Builds unique certificate pairs for each system in the Ansible groups `etcd`, `controller`, and `kubelet`. Certificate pairs include:

- `etcd` - for the etcd cluster to communicate with each other.
- `etcdclient` - for clients of the etcd cluster.
- `controller` - for the Kubernetes controller plane.
- `service-account` - for the Kubernetes service account key.
- `node` - for the Kubernetes kubelets.

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

Bill Cawthra - https://blog.billyc.io/
