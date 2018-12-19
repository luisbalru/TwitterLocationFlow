# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|

  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  config.vm.network "private_network", guest: 80, host: 80
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  # use local ssh key to connect to remote vagrant box
  config.vm.provider :azure do |azure, override|
    azure.vm_image_urn = 'canonical:UbuntuServer:16.04-LTS:16.04.201701130'
    azure.location = 'uksouth'
    azure.tcp_endpoints = '80'
    azure.vm_name = "twitterlocationflow"
    azure.resource_group_name= "twitterlocationflow"
    azure.tenant_id = ENV["AZURE_TENANT_ID"]
    azure.client_id = ENV["AZURE_CLIENT_ID"]
    azure.client_secret = ENV["AZURE_CLIENT_SECRET"]
    azure.subscription_id = ENV["AZURE_SUBSCRIPTION_ID"]

  end

  # Provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "provision/playbook.yml"

  end

end
