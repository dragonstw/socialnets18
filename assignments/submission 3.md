# Assignment 3: Detecting Communities

ENdalkachew Ayalew


## Introduction 

This assignment focuses on how we can work with a random networks.and also how we can  


## Part 1: Small Worlds

### Methods

In order to analyze and work with the random networks i used Netlogo by downloading from the internet. Netlogo is a multi-agent programmable modeling environment that helps for working on simulations with random networks.and i used rewire-one and rewire-all for visualizing the distributions of the small world network.Rewire-one button basically performs a task of removing the connected one end of a node and attach it to other end of the same node.In addition to that, Rewire-all button simply rearrange the whole connected edges and re attach them.


### Results

The clustering coefficient at the beginning of a Watts-Strogatz model with 50 nodes is 0.5

The average path length is 6.633 and

The diameter is 13

while clicking the rewire-one button i have analyzed that both of the clustering coefficient and the average path length decreased from 0.5 to 0.07 and 6.633 to 2.867 consecutively.


![Graph Image](rewire-one.png)


And while clicking the rewire-all button the following results appeared.

clustering coefficient=0.249

average path length=3.147

![Graph Image](rewire-all.png)


As the rewiring performs the original connected nodes will be disconnected and they will be connected randomly to other nodes so the shapes of the plots will be changing as the rewiring happens.


### Discussion

Because as we rewire the nodes, we are disconnecting the original existing links and connect it to new nodes so this will decrease the clustering coefficient of the graph.

As i mentioned above 
As the rewiring performs the original connected nodes will be disconnected and they will be connected randomly to other nodes so the shapes of the plots will be changing as the rewiring happens.



## Part 2: Segregation

### Methods

This model from netlogo basically demonstrates the effect of similarity, and the Density Slider performs the occupancy (occupied) density of the existing neighborhood. and also the % similar wanted slider is simply the slider that controls and manages the percentage of same-color agents that each agent wants among its neighbours.


### Results

![Graph Image](go-once.png)

While clicking the Go once button within 88% density ,30% %-similar-wanted and 79628 number of agents i have found the following results

% similar = 58.5

Number of unhappy = 7706

% unhappy = 9.7

![Graph Image](go.png)

With the same context while clicking the go button and wait till the end within the same information as the above, i have been able to show the following results.

% similar = 73.7

Number of unhappy = 0

% unhappy = 0

### Discussion

From this model i was able to analyze how the agents can be changed by the different factors we have seen on the above that have different functionality on the netlogo simulation of the segregation model.

## Part 3: Giant Component

### Methods

On this model we are able to analyze how quickly a giant component arises if we grow a random network.

On the start we will have nodes without any connections then it will create a connection with to random nodes. As the model runs those nodes that are connected to each other will create a small chain components.those components will merge together and create a giant component.

### Results

while i setup the number of nodes to 80 i have been able to see the followin result and the Giant component size is 80


![Graph Image](Giant component.png)

And i was able to change the color of the giant component by changing the following text code.

![Graph Image](change code.png)

### Discussion

In general we have been able to change the code to give us our own implementation and i was able to manage and analyze what made this model run and operate as i wanted it to produce a giant component with a given numbers of nodes.
