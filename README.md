<p align="center">
  <a href="https://www.dropbase.io">
    <img src="https://assets-global.website-files.com/5f2c87246b17fcf662282594/6125a1fa1160592fd373d33b_Dropbase%20logo%20website.svg" width="200px" alt="Dropbase logo" />
  </a>
</p>

<h2 align="center">Build admin panels and internal web apps with Python</h3>

<p align="center">
<a href="https://dropbase.io">Website</a> · <a href="https://docs.dropbase.io/">Docs</a> · <a href="https://docs.dropbase.io/quickstart">Quickstart</a> · <a href="https://docs.dropbase.io/category/demos">Demos</a> · <a href="https://docs.dropbase.io/setup/workspace">Sign up</a> · <a href="https://docs.dropbase.io/setup/developer">Local Setup</a><p>

<p align="center">
  <a href="https://dropbase.io" target="_blank">
      <img src="https://docs.dropbase.io/assets/images/dropbase_app-4082f07b1cdba1a5f3f5cf56e8d7676c.png" alt="Dropbase hero" />
  </a>
</p>

# Overview

Dropbase is a developer-first platform to build internal web apps with just Python. It lets you easily import your existing Python libraries and scripts so you don’t have to rewrite them to fit our framework.

Build apps by selecting UI components from a list and binding them to data fetcher functions or Python scripts. Use State & Context objects to access and modify the UI state and context directly via Python functions. There's no need to write frontend code.

Dropbase has a highly opinionated app layout that speeds up app development and results in simple apps that effectively solve user problems. All apps consists of a table view and a widget sidebar. By placing table(s) in the table view and UI components in the sidebar widget, you can quickly build anything from admin panels, billing dashboards, and internal engineering tools.

Once you've built your apps, share them with other users via roles, groups, permissions, and granular controls.

## Why Dropbase?

1. Build fullstack internal apps with just Python; there’s no need work with frontend libraries, frameworks, or code
2. Easily import your existing Python scripts and libraries and leverage third party libraries like pandas and numpy in your apps
3. Secure platform with granular app permissions, role based access control, self-hosted deployments, and source-available distribution

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
