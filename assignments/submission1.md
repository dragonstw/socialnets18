# Lab Report


### Introducton

	social networks is all about studying and analyzing the relationship and connection between different entites and
	saying that one of the major connection tools for us people is social media in which facebook holds great deal.
	in this asignment we will analyze our self and our friends in relation to one another to better understand how
	well we are connected to our friend and how each of our friends are connected among one another

### Methods

	to start off we have to get the data from facebook.com and since there were no available option provided by 
	facebook we had to use lost circles which is a chrome extenstion which will automaticaly grab your friends list
	and go through each of your friends one at a time to grab your mutual friends.

	once lost circle has finished going through your friends list the next step would be to export the data and
	analyze the data for that we used gephi which is a tool for analyzing graphs and perform calculations 
	based on the graph

	finally in my situation even though it downloaded my facebook friends compleatly it failed to retrive the eadges
	or the links between my friends compleatly and most of my friends are not connected and retrying the lost circles
	maytimes after clearing my data worked in grabing the correct data but i was not able to download the data as
	a graphml file anymore. due to that i used my first graph file to work on this assignment 

### Results

	while using gephi to analyze my data i was able to get the number of eadges and nodes which are 95 and 708
	respectivly and i was able to calculate the avarage degree, avarage clusturing cofficent
	and average path length which gives a result of 0.268 ,0 ,2.703

	furthermore in the data labratory secton i was able to find my facebook friends information along with the degree,
	betweenes centrality and other parameters of each of my friends

##### image uploaded
	![Network picture](https://raw.githubusercontent.com/dragonstw/socialnets18/develop-NatnaelGetachew/assignments/network_picture.svg)

### Discussion
	to elaborate and finalize my report the node degree is the number of eadges that a node has and the avarage node
	degree is the avarage of all nodes node degree. so we can know the highest amount of friends by looking at the
	highest node since the eadges represent the friendship and the avarage node degree will represent on avarage how
	much of our friends are conected to each other and the avarage path length is the avarage number of shortest path
	between nodes which inplies the inter connectedness of your friends to one another