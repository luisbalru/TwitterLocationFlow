## Welcome to TwitterLocationFlow

In this page you will be able to find the progress in my Virtual Infrastructure project!! Here you have some information:

### About the project

Enjoy the interactions flow between Twitter's users around a topic! Choose whatever word or hashtag you are keen on and discover in a world map where are people who are tweeting about that topic. Besides, if there are conversations between Twitter users about the topic you like, you will see in the map arcs or flows between the users.

### Tools
Python will be the programming language used. Basically, the data structure which lie beneath my app is a graph, so I'm using a graph database to warehouse my information. I have choosen *Neo4j* due to the fact that is Open Source, supports ACID and I will be able to use it buil-in REST web API interface.  

Privacy Twitter's policy must be taken into account so I just want to warehouse the user's location but **NOT** his/her nick nor the whole content of the tweet. Those tweets which form part of a conversation will be treated as a link of union between the speakers.  

To summarize, I consider to deploy three microservices:   

	- A first microservice focused on the user interface.  
	- A second microservice (the core) where I warehouse the information in the Neo4j Graph Database.  
	-Finally, a third microservice who is encharged of representing the points, arcs in the map and the flow of information.  
 
### License

This project is under [GNU general public licence](https://choosealicense.com/licenses/gpl-3.0/) with the so called _copyleft_ that **allows**:

    Commercial use
    Distribution
    Modification
    Patent use
    Private use

With these **conditions**:

    Disclose source
    License and copyright notice
    Same license
    State changes

