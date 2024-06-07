<p align="center">
  <a href="https://www.dropbase.io">
    <img src="https://assets-global.website-files.com/5f2c87246b17fcf662282594/6125a1fa1160592fd373d33b_Dropbase%20logo%20website.svg" width="200px" alt="Dropbase logo" />
  </a>
</p>

<h2 align="center">Build custom internal software faster with AI</h3>

<p align="center">
<a href="https://dropbase.io">Website</a> · <a href="https://docs.dropbase.io/">Docs</a> · <a href="https://docs.dropbase.io/quickstart">Quickstart</a> · <a href="https://docs.dropbase.io/category/demos">Demos</a> · <a href="https://docs.dropbase.io/setup/workspace">Sign up</a> · <a href="https://docs.dropbase.io/setup/developer">Local Setup</a><p>

<p align="center">
  <a href="https://dropbase.io" target="_blank">
      <img src="https://docs.dropbase.io/assets/images/dropbase_app-4082f07b1cdba1a5f3f5cf56e8d7676c.png" alt="Dropbase hero" />
  </a>
</p>

# Overview

Dropbase helps you build custom internal software faster with AI. Developers can quickly build anything from admin panels, billing dashboards, and internal engineering tools that can fetch data and trigger action accross any internal or external service.

Existing low-code/no code tools lack flexibility, confine devs to building app logic by filling up UI forms, and have big learning curves. Dropbase uses AI to generate app code that you can verify and/or edit. We combine the convenience of an app builder with the flexibility of code, making it easy to build and customize, while learning to use the product as you see how the AI generates code using the Dropbase web framework.

## Why Dropbase?

1. Write any custom business logic with code
2. Local-first, self-hosted. No creds are shared with us
3. Dropbase lives in your codebase, making it easy to import or resuse custom scripts/libraries
4. Everything in Dropbase is file-based so you could transfer apps by just sharing a zip file of your app directory
5. It's built on Python and you can import any PyPI package. No need to hassle with frontend libraries/code

## Get Started

### 0. Pre-requisites

- Install Docker. We strongly recommend using [Docker Desktop](https://www.docker.com/products/docker-desktop/), especially if you're on Apple M chips. Alternatively, you can install `docker` and `docker-compose`.

### 1. Clone the `dropbase` repo

Clone the Dropbase repository

```python
git clone https://github.com/DropbaseHQ/dropbase.git
```

### 2. Add server.toml and worker.toml files

In Dropbase root directory, create `server.toml` and `worker.toml` files:

`server.toml` contains environmental variables for the server

```bash
host_path = "" # absolute path to your working directory w/o trailing slash e.g. "/Users/jimmyechan/dev/dropbase"
openai_api_key = "" # required to use Dropbase AI features

# optional
host_mounts = [] # list of paths to directories you want to mount to the worker. use to bring your custom scripts/libraries
redis_host = "redis" # redis server's host address. keep `redis` to use built-in one
task_timeout = 300 # number of seconds before worker task times out
```

`worker.toml` contains environmental variables for the worker. This includes database sources, API keys, or access token to third party services.

To include API keys or tokens, add a name for the token and enter your string token. Though not required, adding a descriptive name helps Dropbase AI infer the key to use

```bash
stripe_key = "rk_test_123"
mailgun_api_key="abc123"
```

To include database sources, use the following format: `database`.`database_type`.`database_nickname`

For example, if you want to add a `postgres` database to a list of sources and use `my_source` as its nickname, add the following:

```bash
[database.postgres.my_source]
host = "localhost"
database = "postgres"
username = "username"
password = "password"
port = 5432
```

A `demo` sqlite database is included in the files directory, so you can use it out of the the box by adding the following to your `worker.toml`.

```bash
[database.sqlite.demo]
host = "files/demo.db"
```

NOTE: built-in demo requires database.sqlite.demo to be present in worker.toml

### 3. Start the server

Start the server by running start.sh

NOTE: when starting the server for the first time, make start.sh executable

```bash
chmod +x start.sh
```

You can start the server by running

```bash
./start.sh
```

### 4. Create your first Dropbase app

Go to the Dropbase App `http://localhost:3030/apps` from your browser and click on the `Create app` button to create your first Dropbase app.
