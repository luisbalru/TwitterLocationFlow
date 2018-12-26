#!/bin/bash

fab -f ./despliegue/fabfile.py -H vagrant@twitterlocationflow.uksouth.cloudapp.azure.com KillApp
