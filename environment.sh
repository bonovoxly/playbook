#!/bin/bash
# this installs the AWS CLI and Ansible in a Python virtual environment
# requires that virtualenv be installed
if [ ! -f ./env/bin/activate ]; then
  virtualenv env
  source ./env/bin/activate
  pip install -U boto ansible aws
fi

echo "ansible-container installed and configured."
echo "run 'source ./env/bin/activate'."
