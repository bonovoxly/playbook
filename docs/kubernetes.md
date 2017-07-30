# Kubernetes requirements

The following software was used to create the Kubernetes system:

- An AWS account with a configured administrator user, with access and secret keys configured.
- SSH public key uploaded to AWS, in this case named `dev` (a Terraform and Ansible variable).
- Terraform v0.8.7 (https://www.terraform.io/downloads.html)
- Ansible 2.2.1.0 (installed via pip)
- AWS CLI tools and Boto - `aws-cli/1.11.2 Python/2.7.12 Linux/4.9.8-moby botocore/1.4.60` (installed via pip)

Additional requirements, if the OpenVPN instance is to be used:

- An OpenVPN client, such as Tunnelblick.

# Kubernetes quickstart

Be advised, this playbook will modify the running hosts `~/.ssh/config`.  This allows it to SSH proxy traffic through the OpenVPN instance.  This way, remote access can be achieved via SSH without VPN.  

- Export the AWS access and secret keys:

```
export AWS_ACCESS_KEY_ID=youraccesskey
export AWS_SECRET_ACCESS_KEY=yoursecretkey
```

- Upload the preferred SSH public key to AWS.  For this document, the name `dev` will be used as an example.  
- From the `terraform` directory, edit the `variables.tf` and configure accordingly. Modify the `keypair` to match the AWS SSH key name uploaded previously.
- Plan your infrastructure:

```
terraform plan
```

- Review the proposed changes. Deploy:

```
terraform apply
```

- On to the Ansible section. Configure the `ansible.cfg` appropriately (refer to `ansible.cfg.EXAMPLE` as a reference).  Configure the private key file variable to whatever the private key file that was used in the Terraform section.  
- Wait a few minutes for the instances to come up and for the AWS System Log to populate. **Note** - the Ansible playbook relies on scraping the AWS System Log for the SSH key.  The Ansible role `localhost.aws_ssh_keys` runs this. This job may miss, due to AWS issues with the System Log.  See the **Bugs, Issues, and Future Improvements** below for more information on this.
- Once the AWS infrastructure has been deployed, the Ansible playbook from the `playbooks` directory run:

```
# The env variable should correspond to the env variable used in Terraform, which defaults to `dev`.
# The keypair should map to the local SSH key that was used in Terraform.
# Note that if the `localhost.aws_ssh_keys : Import SSH public keys - public IP addresses.` task can miss the SSH public key, it is most likely due to a bad AWS system log.
cd playbooks
ansible-playbook -i inventory/kubes kubernetes.yml -e "env=dev keypair=dev"
```

- Again, if you get prompted for an SSH fingerprint, either the log hasn't updated yet or AWS did not handle it properly.  If the log never shows up, you can terminate or just blindly accept.

- Once the playbook completes, you should have an OpenVPN access point, a CFSSL x509 certificate generation service, and an internal Kubernetes cluster DNS, complete with a Weave CNI daemonset, and kube-dns.  There should be an OpenVPN profile on the desktop, as well as a kubeconfig.

# bugs, issues, and future improvements

- The Ansible playbook scans the AWS system console for the SSH public key for every instance found with the `Environment={{ env }}` tag.  It is a secure way of acquiring the SSH fingerprint without just blindly accepting it upon the initial SSH connection. However, sometimes, especially when deploying multiple instances at the same time via Terraform, the system log is blank when the instance is initially deployed. This will cause the SSH public key to not be imported into `known_hosts`.  Currently, the way to correct that is to terminate the instance and redeploy it, as it only seems to happen on the initial provision and usually when provisioning a bunch of instances at the same time.
- Terraform destroy will get stuck with the EBS volume attachments (appears to be a bug) - https://github.com/hashicorp/terraform/issues/4643. Have to stop/term the instance first.
- Issues with terraform destroy and the EBS volumes.  Instances must be shutdown/terminated before terraform destroy will work.
- Create a DNS entry that contains all controller plane instances, with a health check or a Route53 entry containing all three controllers.  Currently controller[0] is the only instance that is used.
- Add the Kubernetes dashboard.
- Add Route53 support for the Terraform/Ansible deployment of Kubernetes, to include support for custom FQDNs (like `*.kubes.local`).
- Add documentation on upgrading and adding additional nodes.
- Add autoscaling nodes.
- Add the route53 service to automatically configure Route53 DNS settings - https://github.com/wearemolecule/route53-kubernetes
- Rewrite the Ansible playbook to use Terraform's dynamic inventory script - https://github.com/CiscoCloud/terraform.py
- As soon as they support it, add in the fsType for StorageClass and dynamic persistent volume claims - https://github.com/kubernetes/kubernetes/pull/40805
- Consider a different method for SSL key distribution. It currently fetches the SSL key pairs and then uploads them to the hosts, leaving potential SSL key data on the Ansible host.
- Add the network traffic inside of the components, such as the traffic within the etcd cluster.
- Add network diagram that describes the Weave overlay network and how the pods communicate through that.
- Consider a "pull model" configuration.  In this setup, all instances would pull either from some AWS CodeCommit or S3 repository and run the proper configuration. This could simplify the process, where only Terraform is needed to create the instances with a user script that could kick off the instance configuration.  The push model is a personal preference, and both methods are reasonable.
