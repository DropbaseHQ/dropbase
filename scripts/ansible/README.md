## Dropbase deployment using Ansible

### Prerequisites

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

```bash
make deploy \
  token=dropbase_workspace_token \
  host=your_server_ip \
  user=your_server_user \ 
  password=your_server_user_password # only for user/password authentication
```
