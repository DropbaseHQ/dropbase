#!/bin/bash

# Set working directory path
WORKING_DIR=$(pwd)

# Define configuration file paths
SERVER_TOML="server.toml"
WORKER_TOML="workspace/worker.toml"

# Check and create server.toml if necessary
if [ ! -f "$SERVER_TOML" ]; then
  echo "Creating $SERVER_TOML..."
  cat <<EOL > "$SERVER_TOML"
host_path = "$WORKING_DIR"
host_mounts = []
redis_host = "redis"
task_timeout = 600

[llm.openai]
api_key = "YOUR_API_KEY"
model = "gpt-4o"

# For Anthropic models
# [llm.anthropic]
# api_key = "YOUR_API_KEY"
# model = "claude-3-5-sonnet-20240620"
EOL
else
  echo "$SERVER_TOML already exists."
fi

# Check and create worker.toml if necessary
if [ ! -f "$WORKER_TOML" ]; then
  echo "Creating $WORKER_TOML..."
  cat <<EOL > "$WORKER_TOML"
[database.sqlite.demo]
host = "files/demo.db"
EOL
else
  echo "$WORKER_TOML already exists."
fi

# check files/dev.db exists and create if necessary
if [ ! -f "files/dev.db" ]; then
  echo "Creating files/dev.db..."
  touch "files/dev.db"
else
  echo "files/dev.db already exists."
fi


# build dropbase/worker
docker image rm dropbase/worker
docker build -t dropbase/worker worker/.

# Start containers
docker compose up