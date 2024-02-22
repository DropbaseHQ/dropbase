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

## Structure of Dropbase Apps

- Apps
  - Page
    1. Tables
    2. Widget
       - UI Components
    3. Functions (data fetching functions or scripts)

## Why Dropbase?

1. Build fullstack internal apps with just Python; there’s no need work with frontend libraries, frameworks, or code
2. Easily import your existing Python scripts and libraries and leverage third party libraries like pandas and numpy in your apps
3. Secure platform with granular app permissions, role based access control, self-hosted deployments, and source-available distribution

## Demo Videos

- [Data editor](https://youtu.be/R1cHO9lMRXo)
- [Customer approval](https://youtu.be/A1MIIRNkv3Q)
- [Email notification system](https://youtu.be/2uLjazAezrU)
- [Admin panel](https://youtu.be/if0E8oC0Qc4)

## Get Started

1. Create an account at https://app.dropbase.io/
2. Follow instructions for local setup at: https://docs.dropbase.io/setup/developer (or see below for a quick local setup guide)

## Quick Local Setup Guide

### 0. Pre-requisites

- Sign up for Dropbase account
- Install Docker. We strongly recommend using [Docker Desktop](https://www.docker.com/products/docker-desktop/), especially if you're on Apple M chips. Alternatively, you can install `docker` and `docker-compose`.
- Have internet access.

### 1. Clone the `dropbase` repo

```bash

git clone https://github.com/DropbaseHQ/dropbase.git

```

The `dropbase` directory (root) will contain the following important subdirectories:

- demo: Contains docker files to spin up a sample Postgres database with seed data
- workspace: Your apps code and files

Github repo at [Dropbase Worker](https://github.com/DropbaseHQ/dropbase).

### 2. Create a .env file

In the root directory (`dropbase`), create a `.env` file, paste the following context, then save it:

```text

DROPBASE_TOKEN='YOUR_WORKSPACE_TOKEN'
DROPBASE_API_URL="https://api.dropbase.io"

```

### 3. Install requirements and start servers

In your terminal, run the following commands from the root directory (`dropbase`)

```bash

chmod +x start.sh
./start.sh

```

### 4. Create your first Dropbase app

Go to the Dropbase App Dashboard `localhost:3030/apps` from your browser and click on the Create app button to create your first Dropbase app.

## Deploy to your server

The Dropbase components come in the form of Docker containers. If you wish to implement them on your server, you can consult our [ansible scripts](./scripts/ansible) for deployment guidance.

