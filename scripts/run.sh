#!/bin/bash

cd ..
vagrant up --provider=azure
vagrant provision
fab -f ./despliegue/fabfile.py -H vagrant@twitterlocationflow.uksouth.cloudapp.azure.com InstalarApp
fab -f ./despliegue/fabfile.py -H vagrant@twitterlocationflow.uksouth.cloudapp.azure.com IniciarApp
