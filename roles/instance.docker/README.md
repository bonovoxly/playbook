instance.docker
=========

Installs Docker on Ubuntu 16.04. Ensures that Docker is started.  Restarts if storage config changes.

Requirements
------------

Requires Ubuntu 16.04 or greater.

Role Variables
--------------

- `docker_key_server` - The Docker Apt key server.
- `docker_id` - The Docker Apt ID.
- `docker_graph` - The Docker graph directory.
- `docker_storage_driver` - The Docker storage driver.

Dependencies
------------

None

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - role: instance.install_docker
           docker_key_server: http://yourkeyserver.com
           docker_id: 1234567890abcdef
           docker_graph: /opt/docker
           docker_storage_driver: btrfs
```

License
-------

BSD

Author Information
------------------

Bill Cawthra - https://blog.billyc.io/
