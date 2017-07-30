# Stuffs requirements

- An AWS account with a configured administrator user, with access and secret keys configured.
- SSH public key uploaded to AWS, in this case named `dev` (a Terraform and Ansible variable).
- Terraform v0.8.7 (https://www.terraform.io/downloads.html)
- Ansible 2.2.1.0 (installed via pip)
- AWS CLI tools and Boto - `aws-cli/1.11.2 Python/2.7.12 Linux/4.9.8-moby botocore/1.4.60` (installed via pip)

Additional requirements, if the OpenVPN instance is to be used:

- An OpenVPN client, such as Tunnelblick.

# Terraform deployment

[The Terraform files can be found here](https://github.com/bonovoxly/terraforms/tree/master/stuffs). In this case, I left the bucket public, to make a demo/proof of concept easier to play with.  Obviously, in a real production environment, you won't want this public. A couple files to modify include:

- `s3.tf` - this has the public S3 bucket settings.  
- `policy.json` - this file is the template for the S3 bucket policy. It allows public web read-only access.
- `variables.tf` - modify the S3 bucket name.

- Terraform:

```
cd terraforms/stuffs
terraform plan
terraform apply
```

This creates an OpenVPN instance and example instances, such as a "web" instance and a "db" instance. The example instance is an old AMI, which has out of date packages. It creates an S3 bucket (again, public readable, not a production quality setting, but it's useful for the demo) that will serve the Hugo generated web pages.

# Ansible deployment

- Ansible playbook:

```
cd playbook/ansible-playbooks
ansible-playbook openvpn_terraform.yml -e "env=corp keypair=id_mod" # note this playbook will modify the local ~/.ssh/config to allow SSH proxying
ansible-playbook -i inventory/stuffs_demo stuffs-example-instance.yml -e "env=corp"
```

And with this, the test environment should be deployed.  SSH to an instance (note, SSH proxy config is applied to `~/.ssh/config`) if you are interested in verifying.

The real guts is the next step, the `stuffs.yml` playbook, which will gather the facts on all instances it finds with the `Environment=corp` AWS tag:

```
ansible-playbook -i inventory/stuffs_demo stuffs.yml -e "env=corp"
```
