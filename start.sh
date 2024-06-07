#!/bin/bash

# build dropbase/worker
docker image rm dropbase/worker
docker build -t dropbase/worker worker/.

# Start containers
docker-compose up