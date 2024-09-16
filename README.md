<p align="center">
  <a href="https://www.dropbase.io">
    <img src="https://assets-global.website-files.com/5f2c87246b17fcf662282594/6125a1fa1160592fd373d33b_Dropbase%20logo%20website.svg" width="200px" alt="Dropbase logo" />
  </a>
</p>

<h2 align="center">AI-Based Python Web App Builder</h2>

<p align="center">
<a href="https://dropbase.io">Website</a> · <a href="https://docs.dropbase.io/">Docs</a> · <a href="https://discord.gg/K4Hys7Czzp">Discord</a></p>

<p align="center">
  <a href="https://dropbase.io" target="_blank">
      <img src="https://cdn.prod.website-files.com/5f2c87246b17fcf662282594/661f0ba13ab0bb89a18de029_adminpanel-hero.webp" alt="Dropbase hero" />
  </a>
</p>

# Overview

Dropbase helps you build and prototype web apps faster with AI. Developers can quickly build anything from admin panels, back-office tools, billing dashboards, and internal engineering tools that can fetch data from data sources and trigger action across any internal or external service.

Existing low-code/no code tools lack flexibility, confine devs to building app logic by filling up UI forms, and have big learning curves. Dropbase uses AI to generate app code that you can verify and/or edit. We combine the convenience of a drag-and-drop app builder with the flexibility of code, making it easy to build and customize, while learning to use the product as you see how the AI generates code using the Dropbase web framework.

## Why Dropbase?

1. Write (or generate) any custom business logic with code.
2. Built-in web framework with pre-built UI components - no need to hassle with frontend libraries/code.
3. Local-first, self-hosted. No creds are shared with us.
4. Dropbase lives in your codebase, making it easy to import or resuse custom scripts/libraries.
5. Apps are portable: app folders can be zipped and shared to other Dropbase users
6. It's built on Python and you can import any PyPI package.

## Demo

### Build a simple app to search for customer orders and send slack messages

<a href="https://youtu.be/RaxHOjhy3hY">
  <img src="https://img.youtube.com/vi/RaxHOjhy3hY/maxresdefault.jpg" style="width:100%; max-width:100%; height:auto;">
</a>

### Build an orders app that uses charts

<a href="https://youtu.be/YWtdD7THTxE">
  <img src="https://img.youtube.com/vi/YWtdD7THTxE/maxresdefault.jpg" style="width:100%; max-width:100%; height:auto;">
</a>

## Get Started

### 0. Pre-requisites

- Install Docker. We strongly recommend using [Docker Desktop](https://www.docker.com/products/docker-desktop/), especially if you're on Apple M chips. Alternatively, you can install `docker` and `docker-compose`.

### 1. Clone the `dropbase` repo

Clone the Dropbase repository

```python
git clone https://github.com/DropbaseHQ/dropbase.git
```

### 2. Start the server

Start the server by running start.sh

**NOTE:** When starting the server for the first time, make `start.sh` executable.

```bash
chmod +x start.sh
```

You can start the server by running

```bash
./start.sh
```

### 3. Create your first Dropbase app

Go to the Dropbase App `http://localhost:3030/apps` from your browser and click on the `Create app` button to create your first Dropbase app.

## Enabling AI features

Dropbase uses LLM (gpt, sonnet) to provide AI Developer feature. To enable it, add your OpenAI or Anthropic api key into `server.toml`. Example:

```bash
[llm.openai]
api_key = "YOUR_API_KEY"
model = "gpt-4o"
```

**IMPORTANT:** If you add additional environmental variables, make sure to add them before LLM configurations (at the top-level table), since LLM configurations are defined as [table](https://toml.io/en/v1.0.0#table)

## Configuring Worker

`worker.toml` contains environmental variables for the worker. This includes database sources, API keys, or access token to third party services.

> [!IMPORTANT]
> If you're upgrading to dropbase-server >v0.6.0, please ensure that `worker.toml` is in your `workspace` directory.

To include API keys or tokens, add a name for the token and enter your string token. Though not required, adding a descriptive name helps Dropbase AI infer the key to use.

```bash
stripe_key="rk_test_123"
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

**NOTE:** The built-in demo requires `database.sqlite.demo` to be present in `worker.toml`.
