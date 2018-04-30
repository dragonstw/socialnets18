# Assignment 3: Detecting Communities

Geleta Firdissa


## Introduction
Network properties rewire-one shows some fraction of rewired edges when pointer is on top of the box. The fraction keeps increasing up to 1 starting from 0. Similar pattern occurs for a network property Rewire-All. I clicked on rewire-one and it shows a clustering-coefficient of 0.491 and average path length of 4.632. I changed the number of nodes, and the diagram happens to decrease to the top, where the number of nodes are configured to. Also, there are two dots showing where the nodes are located, apl and cc (blue)

The lines(turtles) showed up. Similar to a turtle being drawn in a tkinter code, these lines correspond to fixed values of coefficient and path lengths, clustering coefficient - 0.5 and avg path length of 6.128, for 47 turtles. The initial metrics are 0.5 for coefficient and the average path length is 6.12 for those amount of turtles. This keeps increasing later on.

Rewire all shows a fairly complicated diagram. Similar in appearance of property, the dots happen to be incrementing as rewire-all is clicked repeatedly. This shows a certain incremental property of the relationship between nodes, such that the clustering coefficient and the number of nodes that couple up is constantly changing.


## Part 1: Small Worlds
### Methods
To calculate the diameter of the graph for rewire-one, is the same as calculating distance between two turtles. The turtle monitor shows distance from other turtles, as a series of numbers for different turtle values. The code is as follows:

turtles-own
[
  node-clustering-coefficient
  distance-from-other-turtles   ;; list of distances of this node from other turtles
]

distance from other turtles is defined here as a turtle local variable
The code that carries calculation for both distance and the path length is as found in this function..
```
to find-path-lengths
  ;; reset the distance list
  ask turtles
  [
    set distance-from-other-turtles []
  ]

  #code to initialize nodes here
  #code to initialize distance lists here
  while [k < node-count]
  [
    set i 0
    while [i < node-count]
    [
      set j 0
      while [j < node-count]
      [
        ;; alternate path length through kth node
        set dummy ( (item k [distance-from-other-turtles] of turtle i) +
                    (item j [distance-from-other-turtles] of turtle k))
        ;; is the alternate path shorter?
        if dummy < (item j [distance-from-other-turtles] of turtle i)
        [
          ask turtle i [
            set distance-from-other-turtles replace-item j distance-from-other-turtles dummy
          ]
        ]
        set j j + 1
      ]
      set i i + 1
    ]
    set k k + 1
  ]

end
```
### Results
Clustering coefficient is 0.479333 Average-path-length is 5.764 clustering-coefficient-of-lattice is 0.5 and average-path-length-of-lattice is 6.6326 when on rewire-one version. Note: this all depends on the rewiring probablity.
By default monitors only update on ticks unless the settings are set to other methods. This shows, there's a event listener attached to the monitors (the class) carrying out the activity done by the monitor. I discovered this when I set wrong values in the link monitor, it shows a java exeption error, issues with event handling.

### Discussion
The primary reason why clustering coefficients change when nodes are rewired is because, nodes represent the persons in the network and clustering coefficient measure the possibility of one node being friends with someone across the neighbor. So, if the neighbor changes neighbor, the clustering coefficient will be a variable that changes according to the neighbors friends to numerically depict how all his friends are close to the one that the neighbor is connected with.

The rewire one is a step that happens when one part of a connection(wire) is removed and reconnected to another. This is like something based on a probability, a rewiring pobablity. So this could often change the values of the rewiring and the coefficient also. The fist connection will be removed and connected to another node, the same edge happens to change directions but can not remove two nodes at once. That is why it's called rewiring. But rewire all is different because all edges become rewired and this means more than two nodes can be changed for a neighbor. The rewire all shows what happens if in all edges, a rewiring happens.

## Part 2: Segregation
### Methods
The setup button initializes all the values with equal amount for both agents. Then when I click go, the simulation begins and some rippling effect takes place so if an agent does not find a place beside it's own type, it goes somewhere closer. This happens under the control of the density range. Initially, many agents will be unhappy to what's happening.

### Results
17.4 % unhappy, almost close to 399 persons. And there are 2293 agents, which make up to close to half the population. These numbers show that, majority of the minority agent group are relatively tolerant. This is a little difference in outcome but still shows a tolerant group of people because they live close to a different color agent and there is no direction to choose from.
### Discussion
Each orange agent is not mixed inside a blue group and vice versa. This shows they want to live close to their own kind. This eventually creates a pattern. While trying to recreate E&K 4.5, let's say the threshold t is 3 using the same numbe of grids. But I modified the density to 75%, the blue represent one category of the agents. Similar to our previous simulation, the outcome is homogeneous. Each individual wants to live in an area close to a same person. in the last step the output of the re-creation if 50% similar is wanted in this case, is 0 unhappy agents and 86 % similar out of 10000 agents. This is afactor of lower density and percentage of similar wanted, after many steps.

## Part 3: Giant Component
### Methods
This plot shows a fraction in giant component for each connections in a node. When the number of nodes is assigned, he same number of nodes/persons will appear in the box. So we will experiment with a virtual simulation of real interactions, unlike the small world phenomenon. Initially, the growth of the giant component instantly and dramatically increased after a few connections per node, after one person hits up a closest neighbor and the other two are added from the nodes. The graph constantly keeps increasing connections until all the nodes are fully connected (no remaining edges).

### Results
Before I clicked on setup, I changed the default shape for turtle to dot, from person. this shows the turtle dots instead of persons. The turtle has it's own set of shapes. Also, I changed the size of each node. In the part of the code which requests a function to add-edge, I tried changing where node 2, one of turtles asks node1, to ask itself. I got an error message telling me a node can not link to itself. Also, it goes back if there is an edge where it wants to ask turtle, and picks another turtle which is free. While changing the node number to a person who is not next to the node, there will be a few nodes which are never going to meet because an error will occur again saying, a turtle can never link to itself. This occured when I defined a 3rd node, and named it node3 so that instead of ask node1, ask node3 shows that at some point there will be a connection to all (except node3) nodes, and one of the nodes will be itself. It shows an interesting idea that a node can link and get neighbor info only from his closest neighbor and the asking node itself self must be pre-identified so that it can never request data from itself(because this creates loop), so in a social network this case must never happen.

### Discussion
Giant component somehow depicts real life components and the relationship between each nodes. Compared to small world, the clustering here is relatively lower. In addition, the graph is random, but it contains a constant numerical value for each connection.