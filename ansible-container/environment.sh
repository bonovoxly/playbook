#!/bin/bash
if [ ! -f ./env/bin/activate ]; then
  virtualenv env
  source ./env/bin/activate
  pip install -U boto boto3 ansible pip-review setuptools
#  pip install -U ansible-container
else
  source ./env/bin/activate
fi

if [ ! -d ansible-container ]; then
  git clone https://github.com/ansible/ansible-container.git
fi

cd ansible-container
git pull
python ./setup.py develop

echo "ansible-container installed and configured."
echo "Setting exports... fixes some timeouts."
export DOCKER_CLIENT_TIMEOUT=120
export COMPOSE_HTTP_TIMEOUT=120

echo "run 'source ./env/bin/activate'."
