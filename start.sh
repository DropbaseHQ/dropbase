#!/bin/bash

#Check if dropbase/worker:latest docker image is present
if [[ "$(docker images -q dropbase/worker:latest 2> /dev/null)" == "" ]]; then
  #Image not found. Pull it from docker registry
  echo "Image not found. Building dropbase worker image..."
  docker build -t dropbase/worker:latest worker/.
else
  echo "Image found"
fi

# Set the HOST_WORKSPACE_PATH to the current directory to be used by dropbase-server
export HOST_WORKSPACE_PATH=$(pwd)

# Start containers
docker-compose up