#!/bin/bash
if [ ! -f ./env/bin/activate ]; then
  virtualenv env
  source ./env/bin/activate
  pip install -U boto boto3 ansible pip-review setuptools
else
  source ./env/bin/activate
fi

if [ ! -d ansible-container ]; then
  git clone https://github.com/ansible/ansible-container.git
fi

cd ansible-container
git pull
python ./setup.py develop

echo "updating PIP packages..."
pip-review -a
echo "ansible-container installed and configured."
echo "run 'source ./env/bin/activate'."
