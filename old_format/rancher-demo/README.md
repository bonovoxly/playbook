# rancher-demo playbook

This playbook builds a NAT instance, a Rancher server instance, a collection of Rancher hosts, and two ELBs. It deploys an ELK stack on Rancher, including GlusterFS, Convoy, and Route53.

Example run:

```
ansible-playbook rancher-demo.yml
```

# ansible-vault

The Ansible vault file is kept under ```host_vars/127.0.0.1/vault.yml```.  It has the following structure:

```
vault:
  admin_user: username
  ami_ssh_fingerprint: "ecdsa-sha2-nistp256 blahblahblahblahfingerprint" # AMI fingerprint.  Needs to be manually retreived ahead of time.
  aws_secret_key: SECRET_KEY
  aws_access_key: ACCESS_KEY
  ip: 'your_remote_ip_address' # where you are connecting from
  ip2: 'another IP address' # if you don't need it clear it out. Can be found in ```rancher-demo/host_vars/127.0.0.1/demo_aws_internal_instances.yml```.
  key_pair ssh_private_key_name # needs uploaded to AWS key pair
  region: us-west-2 # or east or whereever
  ssh_users: |
    list of ssh public keys for users you want to provide access to
  # SSH key infoconfiguration
  ansible_ssh_key_file: "{{ ansible_env.HOME }}/.ssh/ssh_private_key_name"
  ansible_ssh_key_contents: |
    -----BEGIN RSA PRIVATE KEY-----
    KEYDATA
    -----END RSA PRIVATE KEY-----
  rancher:
    route53_access_key: ACCESS_KEY # for modifying Route53 DNS
    route53_secret_key: SECRET_KEY
    ecr: |  # when using the ECR stack in Rancher, here's the place.
      {"environment": { "aws_access_key_id": "YOURACCESSKEY", "aws_secret_access_key": "YOURSECRETKEY", "aws_region": "us-west-2" }, "startOnCreate": true, "dockerCompose": "ecr-updater:\n  environment:\n    AWS_ACCESS_KEY_ID: ${aws_access_key_id}\n    AWS_SECRET_ACCESS_KEY: ${aws_secret_access_key}\n    AWS_REGION: ${aws_region}\n  labels:\n    io.rancher.container.pull_image: always\n    io.rancher.container.create_agent: 'true'\n    io.rancher.container.agent.role: environment\n  tty: true\n  image: objectpartners/rancher-ecr-credentials:1.0.0\n  stdin_open: true\n", "name": "ecr", "rancherCompose": ".catalog:\n  name: \"ECR Credential Updater\"\n  version: \"v1.0.0\"\n  description: \"Updates credentials for ECR in Rancher\"\n  uuid: ecr-1\n  questions:\n    - variable: \"aws_access_key_id\"\n      label: \"AWS Access Key ID\"\n      description: \"AWS API Access Key to use for obtaining ECR credentials\"\n      required: true\n      type: \"string\"\n    - variable: \"aws_secret_access_key\"\n      label: \"AWS Secret Access Key\"\n      description: \"AWS API Secret Key to use for obtaining ECR credentials\"\n      required: true\n      type: \"string\"\n    - variable: \"aws_region\"\n      label: \"AWS Region\"\n      description: \"AWS Region that hosts the ECR\"\n      default: us-west-2\n      required: true\n      type: \"string\"\necr-updater:\n  scale: 1\n", "externalId": "catalog://community:ecr:0" }
    localAuthConfig: | # This turns on local auth for Rancher.
      '{"type":"localAuthConfig","accessMode":"unrestricted","enabled":true,"name":"admin","username":"admin","password":"YOURSECRETPASSWORD"}'
    route53: |
      {"environment": { "AWS_ACCESS_KEY": "YOURACCESSKEY", "AWS_SECRET_KEY": "YOURSECRETEKEY", "AWS_REGION": "us-west-2", "ROOT_DOMAIN": "demo.aws.internal", "TTL": "299" }, "startOnCreate": true, "dockerCompose": "route53:\n  image: rancher/external-dns:v0.3.0\n  expose: \n   - 1000\n  environment:\n    AWS_ACCESS_KEY: ${AWS_ACCESS_KEY}\n    AWS_SECRET_KEY: ${AWS_SECRET_KEY}\n    AWS_REGION: ${AWS_REGION}\n    ROOT_DOMAIN: ${ROOT_DOMAIN}\n    TTL: ${TTL}\n  labels:\n    io.rancher.container.create_agent: \"true\"\n    io.rancher.container.agent.role: \"external-dns\"\n", "name": "route53", "rancherCompose": ".catalog:\n  name: \"Route53 DNS\"\n  version: \"v0.3.0-rancher1\"\n  description: \"Rancher External DNS service powered by Amazon Route53. Requires Rancher version 0.44.0\"\n  minimum_rancher_version: v0.44.0\n  questions:\n    - variable: \"AWS_ACCESS_KEY\"\n      label: \"AWS access key\"\n      description: \"Access key to your AWS account\"\n      type: \"string\"\n      required: true\n    - variable: \"AWS_SECRET_KEY\"\n      label: \"AWS secret key\"\n      description: \"Secret key to your AWS account\"\n      type: \"string\"\n      required: true\n    - variable: \"AWS_REGION\"\n      label: \"AWS region\"\n      description: \"AWS region name\"\n      type: \"string\"\n      default: \"us-west-2\"\n      required: true\n    - variable: \"ROOT_DOMAIN\"\n      label: \"Hosted zone\"\n      description: \"Route53 hosted zone name (zone has to be pre-created). DNS entries will be created for <service>.<stack>.<environment>.<hosted zone>\"\n      type: \"string\"\n      required: true\n    - variable: \"TTL\"\n      label: \"TTL\"\n      description: \"The resource record cache time to live (TTL), in seconds\"\n      type: \"int\"\n      default: 299 \n      required: false\n\nroute53:\n  health_check:\n    port: 1000\n    interval: 2000\n    unhealthy_threshold: 3\n    request_line: GET / HTTP/1.0\n    healthy_threshold: 2\n    response_timeout: 2000\n", "externalId": "system-catalog://library:route53:4"}
```

Embedding the SSH key in the Ansible Vault keeps the entire project very modular.


# AWS policy

The following is the AWS policy used to run this playbook.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeAvailabilityZones",
                "ec2:RunInstances",
                "ec2:TerminateInstances",
                "ec2:CreateImage",
                "ec2:CreateTags",
                "ec2:StopInstances",
                "ec2:StartInstances"
            ],
            "Resource": "*"
        }
    ]
}
```
