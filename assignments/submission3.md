
#Assignment 3:  Detecting communities

Beytulah kedir


## introduction 
In this assignment, I have learned about random networks get feel for working on simulations with random network.

## Part 1: small worlds

##Methods

First in order to get the diameter, I press the “Add” button and on the interface and added the button according to the tutorial. then  I wrote the code 

~~~“to diameter
 show max [max[NW:distance-to myself] of other turtles ] of turtles
end” after adding the extension NW.~~~
The rewire-one procedure creates an edge between two nodes. Whenever we press it, it creates an edge between two nodes randomly. which means it changes one end of the randomly selected a connected pair of nodes, and keeps the other end the same.
Code snippet from net logo implementing the diameter
~~~
Extensions [nw]
to diameter
 show max [max[NW:distance-to myself] of other turtles ] of turtles
end “’
~~~

##Results

At the beginning of watts-strogatz model, the average path legth is 6.633, the clustering coefficient is 0.5 and the diameter is 13 with 50 nodes.

Plot Image of Rewire-one
![Alt text](rewire-one.png)
Some of the nodes have an edge to other random nodes

Plot image of Rewire-all
![Alt text](rewire-all.png)
The over all shape of the plot is completely different from the wire-one. All the nodes are connected at least with two other nodes.

##Discussion

Since clustering coefficient is the ratio of existing links connecting a node’s neighbors to the maximum possible number of such links, when we rewire, the maximum possible number of link increases.  So that the clustering coefficient becomes less.
The rewire-all version show a distribution of metrics because it visits all edges and tries to rewire them.
The plots shaped the way they are because of the values which determine them.

## Part 2: segregation

##Method

All of the agents want to live near some of their own. Any agent is not tolerant being in the minority and it’s expected since the model deals about this.  

##Results

The number of agents, %similar,num-unhappy and %unhappy is different whenever we press the setup button.
According to the E&K 4.5, when I use the 88%density  and %-similar-wanted 30% and press the go once button, %similar changes to 58.5, num-unhappy = 225 and %unhappy to 9.8 with 2291 agents. These values increases as we press the go once button and finally becomes 0

##Discussion

This model and also the simulation shows the effect of social influence in population clearly. It is also interesting to see these individual preferences ripple through the neighborhood.

## Part 3: Giant component

##Method

Just as described in the info, as the model runs small chain-like components are formed, where the members in each component are either directly or indirectly connected to each other. the Go ONCE button adds one new edge to the network. And when we press GO, it repeatedly add edges . the REDO LAYOUT button also runs the layout-step procedure continuously to improve the layout of the network.

##Result

I have added a simple code to disorder the node queue. When I press the walk button the nodes leave their place and the queue becomes messed up. here is the code
~~~
to walk
  move-turtles
  eat-grass
  tick
end
to eat-grass
  ask turtles [
    if pcolor = green [
      set pcolor black
      
    ]
  ]
end

to move-turtles
  ask turtles[
  right random 360
  forward 1
 
]
End
~~~
##Discussion

This model shows us how quickly a giant component  arises if we grow a random network. and we can add more other codes to see different kinds of actions.

##conclusion

in this assignment i have learned more about random networks and i have got a knowledge about "model of segrigetion" which is a new concept. and also i am happy to know about the programable modeling environment for simulating natural and social phenomena (NetLogo) whicch is also new to me.





