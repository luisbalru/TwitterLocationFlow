# -*- mode: ruby -*-
# author: Luis Balderas Ruiz
# project: TwitterLocationFlow

Vagrant.configure('2') do |configuracion|

  configuracion.vm.box = 'mv-iv'
  configuracion.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
  configuracion.vm.network "private_network", guest: 80, host: 80
  configuracion.ssh.private_key_path = '~/.ssh/id_rsa'

  configuracion.vm.provider :azure do |az, override|
    az.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest'
    az.vm_size = 'Standard_F1'
    az.location = 'uksouth'
    az.tcp_endpoints = '80'
    az.vm_name = "twitterlocationflow"
    az.resource_group_name= "tlf-iv"
    az.tenant_id = ENV["AZURE_TENANT_ID"]
    az.client_id = ENV["AZURE_CLIENT_ID"]
    az.client_secret = ENV["AZURE_CLIENT_SECRET"]
    az.subscription_id = ENV["AZURE_SUBSCRIPTION_ID"]

  end

  configuracion.vm.provision "ansible", run:"always" do |ansible|
    ansible.playbook = "./provision/playbook.yml"

  end

end
