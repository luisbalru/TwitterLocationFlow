## Welcome to TwitterLocationFlow

[![Made with Love and Open Source](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://www.gnu.org/licenses/gpl-3.0.en.html) [![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.png?v=103)](https://opensource.org/licenses/GPL-3.0/)

[![Twitter](https://github.frapsoft.com/social/twitter.png)](https://twitter.com)

In this page you will be able to find the progress in my Virtual Infrastructure project!! Here you have some information:

### About the project

Enjoy the interactions between Twitter's users around a topic, word or hashtag! Choose whatever word or hashtag you are keen on and discover in a world map where are people who are tweeting about that topic. Besides, if there are conversations between Twitter users about the topic you like, you will see in the map arcs or flows between the users.

### Links

[Official repository website](https://luisbalru.github.io/TwitterLocationFlow/)    
[Despliegue](https://iv1819-twitterlocationflow.herokuapp.com/)

Contenedor DockerHub `docker pull luisbalru/twitterlocationflow`

Contenedor Zeit: https://twitterlocationflow-beql36dlw.now.sh 

### Tools
 - Python (Flask)
 - Heroku (Paas). [Why Heroku?](doc/why-heroku.md)
 - Docker/DockerHub
 - Zeit

### Installation

`pip install -r requirements.txt`

### Documentation

[API Documentation](doc/API.md)  
[Heroku Setup](doc/Heroku.md)
[Procfile Doc](doc/Procfile-doc.md)
[Automated build DockerHub](doc/ab-dockerhub.md)
[Zeit installation/deployment](doc/zeit-deploy.md)


### Tests

[![Build Status](https://travis-ci.org/luisbalru/TwitterLocationFlow.svg?branch=master)](https://travis-ci.org/luisbalru/TwitterLocationFlow)

### Run the tests

`pytest`

### Run the main program

`python3 TwitterGraph.py`

### License

Here you can find the [Licence](https://github.com/luisbalru/TwitterLocationFlow/blob/master/LICENSE)
