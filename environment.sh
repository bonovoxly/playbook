#!/bin/bash
# this installs the AWS CLI and Ansible in a Python virtual environment
# requires that virtualenv be installed
if [ ! -f ./env/bin/activate ]; then
  virtualenv env
  source ./env/bin/activate
  pip install -U boto ansible aws
fi


echo "Ansible installed and configured."
echo "Note that some Ansible modules will not find boto in a virtual environment.  It is recommended to install boto using 'sudo pip install boto'."
echo "run 'source ./env/bin/activate'."
