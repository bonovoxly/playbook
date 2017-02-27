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

- On to the Ansible section. In the `playbooks/ansible-playbooks` directory, edit the `ansible.cfg`.  Configure the private key file variable to whatever the private key file that was used in the Terraform section.  
- Wait a few minutes for the instances to come up and for the AWS System Log to populate. **Note** - the Ansible playbook relies on scraping the AWS System Log for the SSH key.  The Ansible role `localhost.aws_ssh_keys` runs this. This job may miss, due to AWS issues with the System Log.  See the **Bugs, Issues, and Future Improvements** below for more information on this.
- Once the AWS infrastructure has been deployed, the Ansible playbook from the `playbooks/ansible-playbook` directory run:

```
# The env variable should correspond to the env variable used in Terraform, which defaults to `dev`.
# The keypair should map to the local SSH key that was used in Terraform.
# Note that if the `localhost.aws_ssh_keys : Import SSH public keys - public IP addresses.` task can miss the SSH public key, it is most likely due to a bad AWS system log.
cd playbooks/ansible-playbooks
ansible-playbook -i inventory/kubes kubernetes.yml -e "env=dev keypair=dev"
```

- Again, if you get prompted for an SSH fingerprint, either the log hasn't updated yet or AWS did not handle it properly.  If the log never shows up, you can terminate or just blindly accept.

- Once the playbook completes, you should have an OpenVPN access point, a CFSSL x509 certificate generation service, and an internal Kubernetes cluster DNS, complete with a Weave CNI daemonset, and kube-dns.  There should be an OpenVPN profile on the desktop, as well as a kubeconfig.
