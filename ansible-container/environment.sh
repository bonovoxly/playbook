#!/bin/bash

if [ ! -f ./env/bin/activate ]; then
  virtualenv env
  source ./env/bin/activate
  pip install boto ansible setuptools ansible-container
fi

echo "ansible-container installed and configured."
#echo "Setting exports... fixes some timeouts."
#export DOCKER_CLIENT_TIMEOUT=120
#export COMPOSE_HTTP_TIMEOUT=120

echo "run 'source ./env/bin/activate'."
