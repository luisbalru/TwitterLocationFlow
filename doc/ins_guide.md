# Installation Guide

Due to the fact that Azure is the IaaS I have used, an Azure's account and a subscription will be neccesary.

In this repository, you can find a directory called scripts. Someone who starts using
this app needs to create a Graph Database. In this case, CosmosDB has been chosen. gremlin-db.sh script
creates the database and a new graph needed in the installation.

0) `$ az login`

1) `./scripts/gremlin-db.sh`

Then, you will need a resource group.

2) `./scripts/rg.sh`

After this, you need to create a service principal

3) `./scripts/service_principal.sh`

Credentials given after the Service Principal's creation must be written down in .bashrc file:

`export AZURE_TENANT_ID = tenant ` 
`export AZURE_CLIENT_ID = appId`  
`export AZURE_SUBSCRIPTION_ID = password`

Finally, your account is ready to install the app.

4) `./scripts/install.sh`

Running

5) `./scripts/run.sh`

And kill it

6 `./scripts/kill.sh`
