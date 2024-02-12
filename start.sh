#!/bin/bash

#Check if dropbase/worker:0.0.1 docker image is present
if [[ "$(docker images -q dropbase/worker:0.0.2 2> /dev/null)" == "" ]]; then
  #Image not found. Pull it from docker registry
  echo "Image not found. Pulling from Docker Registry..."
  docker pull dropbase/worker:0.0.2
else
  echo "Image found"
fi

# Set the HOST_WORKSPACE_PATH to the current directory to be used by dropbase-server
export HOST_WORKSPACE_PATH=$(pwd)

# Start containers
docker-compose up