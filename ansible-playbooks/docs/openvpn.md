# openvpn.yml

- Sign up and register for an AWS account.
- After creating the account, create an IAM user.  
- Give this user the Administrator role (or restrict the policy if needed).  
- Create an AWS access/secret key pair.  Save them somewhere safe.  Export them as environment variables:
```
AWS_ACCESS_KEY_ID=YOURACCESSKEY
AWS_SECRET_ACCESS_KEY=YOURSECRETKEY
```
- Optional - create the SSH key pair (optional - modify your ansible.cfg as needed, if you save it to a non-default path).

```
# it will prompt you if a key already exists.  
ssh-keygen -t rsa -b 4096
```

- Save your SSH private and public key to your favorite password manager for future reference.
- Install Ansible.  This requires `virtualenv`. You can do this with brew or whatever your preferred package manager is.  This uses's OS X's default:

```
# install virtualenv
sudo pip install virtualenv
# install Ansible and other needed packages (runs from the base directory of the playbooks repo)
./environment.sh
# activate the virtualenv
sourece ./env/bin/activate
# change to the ansible-playbooks directory 
cd ansible-playbooks
```

- Run the `create_vpc.yml` playbook. This will create a VPC, subnets, security groups, and all the other things needed for AWS.  Example that can be used:

```
ansible-playbook vpc_create.yml -e "env=dev"
```

**Note - sometimes availability zones are "full".  Modify `vars/dev_aws/aws.yml` accordingly.**

- Finally, to deploy the OpenVPN server:

```
ansible-playbook openvpn.yml -e "env=dev public_ip=true instance_type=t2.micro"
```

**Note the instance type extra variable.  This overrides the default `t2.nano` instance size.  Free tier is only applicable to `t2.micro`.**

- Import the `user.ovpn` into your preferred VPN client. Test accordingly.
