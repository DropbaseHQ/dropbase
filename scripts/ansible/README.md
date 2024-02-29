## Dropbase deployment using Ansible

### Prerequisites

Make sure you have `.env` file on the project's root directory. The file must contain the 3 following environment variables:
```bash
DROPBASE_API_URL="https://api.dropbase.io"
DROPBASE_TOKEN='<your-dropbase-token>'
CORS_ORIGINS='["http://your-server-ip:3030", "http://www.your-server-ip:3030"]'
```

Make sure you have ansible installed on your machine where you will run the deployment. You can install ansible using
the following command:

```bash
pip3 install ansible 
```

It's recommended to authenticate to your server using a SSH key-pair. However, you are using username/password
authentication, make sure you have sshpass installed.

```bash
# on MacOS X
brew install hudochenkov/sshpass/sshpass

# on Ubuntu
apt-get install sshpass
```

### Deploy dropbase to your server

Before you deploy, make sure you can authenticate to the server using a user has sudo privileges. 

You should [enable passwordless sudo](https://timonweb.com/devops/how-to-enable-passwordless-sudo-for-a-specific-user-in-linux/) so that you don't have to enter the password every time the script runs a new step.

```bash
make deploy \
  host=your_server_ip \
  user=your_server_user \
  ssh_key_file=your_private_ssh_key_file # if you use a custom \
  password=your_server_user_password # only for user/password authentication
```
