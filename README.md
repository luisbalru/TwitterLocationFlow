## Welcome to TwitterLocationFlow

[![Made with Love and Open Source](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.png?v=103)](https://opensource.org/licenses/GPL-3.0/)
[![Build Status](https://travis-ci.org/luisbalru/TwitterLocationFlow.svg?branch=master)](https://travis-ci.org/luisbalru/TwitterLocationFlow)
[![Twitter](https://github.frapsoft.com/social/twitter.png)](https://twitter.com)

In this page you will be able to find the progress in my Virtual Infrastructure project!! Here you have some information:

### About the project

Enjoy the interactions between Twitter's users around a topic, word or hashtag! Choose whatever word or hashtag you are keen on and discover in a world map where are people who are tweeting about that topic. Besides, if there are conversations between Twitter users about the topic you like, you will see in the map arcs or flows between the users.

### Links

[Official repository website](https://luisbalru.github.io/TwitterLocationFlow/)    

Contenedor: https://docker-tlf.herokuapp.com  


Heroku [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://iv1819-twitterlocationflow.herokuapp.com/)


[URL de despliegue en DockerHub](https://hub.docker.com/r/luisbalru/twitterlocationflow/)  

`docker pull luisbalru/twitterlocationflow`

[Zeit site](https://twitterlocationflow-wodotzcwyc.now.sh  )

Despliegue final: twitterlocationflow.uksouth.cloudapp.azure.com

### Tools
 - Python (Flask)
 - Heroku (Paas). [Why Heroku?](doc/why-heroku.md)
 - Azure (IaaS)

### Installation

In order to use my app, you will need to install in your local machine:

  - Python (Python3)
  - Azure Cli
  - Vagrant
  - Vagrant plugin for Azure
  - Ansible
  - Fabric

Besides, all requirements specified are needed:

`pip install -r requirements.txt`

Here you have the [installation guide](doc/ins_guide.md)

### How to use it?

Here you have a [user guide](doc/guide.md)

### Documentation

[API Documentation](doc/API.md)  
[Heroku Setup](doc/Heroku.md)  
[Procfile Doc](doc/Procfile-doc.md)  
[Automated build DockerHub](doc/ab-dockerhub.md)  
[Zeit installation/deployment](doc/zeit-deploy.md)  
[Heroku Deployment with Docker](doc/heroku-docker.md)  
[Creación y provisionamiento de máquinas](doc/provisionamiento.md)  
[Despliegue de la aplicación](doc/despliegue.md)


### Run the tests

`pytest`


### LICENSE

Here you can find the [Licence](https://github.com/luisbalru/TwitterLocationFlow/blob/master/LICENSE)
