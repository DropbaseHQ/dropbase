deploy:
    ifndef host
        $(error host is not defined. Please provide your server address.)
    endif
    ifndef user
        $(error user is not defined. Please provide user to login into the server.)
    endif
    ifndef token
        $(error token is not defined. Please provide the dropbase workspace token.)
    endif

	ansible-playbook deploy-to-vm.yml -i $(host), -e "ansible_user=$(user)" -e "ansible_password=$(password)" -e "ansible_ssh_private_key_file=$(ssh_key_file)" -e "workspace_token=$(token)"
