#!/bin/bash

# build dropbase/worker
docker image rm dropbase/worker
cd worker
docker build -t dropbase/worker .
cd ..

# Set the HOST_WORKSPACE_PATH to the current directory to be used by dropbase-server
export HOST_WORKSPACE_PATH=$(pwd)

# Start containers
docker-compose up