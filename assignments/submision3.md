# Assignment 3: Detecting Communities
feysel meftuh
ID-ATR/3043/06

## Introduction
The assignment is about random networks. how connected are people to other people in the world. 

## Part 1: Small Worlds
### Methods
The procedure in rewire-one: first select one random edge of all the connections between the nodes, then switch one end of that selected edge to another node while the other end remains in the same position. so what rewire-one does is generate a new connection between nodes by selecting a random connection and made a new connection out of it by rewiring one end of that edge to a new node. In context of the network rewiring means changing the wiring made first and make a new wiring. 
### Results
Clustering Coefficient = 0.5 
 
Average-path-length = 6.633 
 
Diameter = 13

![Alt text](Smallw.JPG)

This is the image of the plot after trying rewire-one and rewire-all many times: 

![Alt text](Smallw all one.JPG)

After all this rewiring we got the 
 
Clustering Coefficient = 0.111 
 
Average-path-length = 2.958 

The first rewire-one plot shows first decreasing graph, at last it remains on the same position. on the second one it shows a vertical shape. 

### Discussion
As the nodes are rewired the clustering coefficient change this is because the node pairs and the neighbors of nodes change as the rewiring takes place. The plots are shaped the way they are based ont the values that determine them, on the rewire-one the x-axis shows the fraction of edges that are rewired so far while in the rewire-all the x-axis shows the probability of rewiring as shown after rewire-all. 
 

## Part 2: Segregation
### Methods
By using density we can manage the density of the neighborhood. To manage the percentage where agents want to have as a neighbor we used the %-similar-wanted. 
 
### Results
At first setup using 88% of density and 30% of similar-wanted we have 
 
%similar = which represent the average of same color neighbors all around the agents. 
 
num-unhappy = that indicating number of unhappy agents. 
 
%unhappy = same also indicates percent of unhappy agents which get smaller same color neighbors than they needed. 
 
After we clicked go once the values change based on the agents movement and we get: 

%similar = 49.9 
 
num-unhappy = 386 
 
%unhappy = 17 
 
 After we clicked go the values become: 
 
%similar = 72.5 
 
num-unhappy = 0 
 
%unhappy = 0 
 
![Alt text](segregation.jpg)
 
As shown here in the graph the % similar value is almost on the same percent through time. The number of unhappy shows a decreasing graph starting from the top and at last it becomes 0. 

### Discussion
We have got 0 on the number and percent of unhappy agents this is because all agents have got30% of neighbors that are similar to them as they wanted. 
 
## Part 3: Giant Component
### Methods
On working with giant component model we found nodes with no edges connecting them. While doing the next step on making a giant component out of those nodes we picked 2 random nodes at a time and create a connetion between them. As this process goes by and end we will get a giant component where every node can be reached starting from every other node in the network. 
 
### Results
With the num-nodes of 80 we will get a giant component size equal to 80 with the following growth. 

![Alt text](giant.jpg)

The growth of the giant component with 80 nodes shows an increasing fraction in giant component through out the connection per node increases. 
 
By changing the num-nodes into 24 we will be able to see the connection that made the giant component with a giant component size of 24. This is illustrated below: 
 
![Alt text](size24.jpg)
 

### Discussion
We can get a giant component from random networks. On the giant component we got from a random connection of nodes, each node will be reachable from any other node. 
 

## Conclusion

Through out this assignment i was not able to complete every aspects of the questions because of some contradictions and lack of information guiding the assignment. However, i have learned about random networks .
