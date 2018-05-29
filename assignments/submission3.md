# Assignment 3: Detecting Communities

Yohannes Endale


## Introduction


On this assignment i worked on simulations with random networks using three example givin by my instructor. This examples are **Small worlds**, **Segregation**, and **Giant Component**. I used a tool called `NetLogo`. 



## Part 1: Small Worlds
### Methods

When doing this project first i play around with some of the metics to get a feel for whats is happening. And since i didn't worked on small worlds phenomenon on NetLogo before, I experimented on some of the merics using only 10 nodes because its was much easier to recognizing what is happening and to be able see the `rewire` functionality and other functionality's appears on the plot.
After i play around with the small world phenomonen, first thing i did is write the code for the `Diameter` and also i add the interface for the `Diameter`.


#### Line by line explanation for `rewire-one` procedure

```
to rewire-one //created function for rewire-one

  if count turtles != num-nodes [ //check if number of turtle is setup if not run setup first
    setup
  ]

  // record which button was pushed
  set rewire-one? true // since rewire-one was pushed will set it to true
  set rewire-all? false // and false for rewire-all

  let potential-edges links with [ not rewired? ] //for potential edge links with not rewired
  ifelse any? potential-edges [ //for any potential-edges
    ask one-of potential-edges [ // take only one potential-edges
      let node1 end1 //for node1 the edge will remian the same
      if [ count link-neighbors ] of end1 < (count turtles - 1) // if the edge is not connected to everybody
      [
        let node2 one-of turtles with [ (self != node1) and (not link-neighbor? node1) ] // find a neighbor for node1 that is not already connected
        ask node1 [ create-link-with node2 [ set color cyan  set rewired? true ] ] // create edge with the newer node

        set number-rewired number-rewired + 1 // count number of rewirings

        die // remove old edge
      ]
    ]
    let connected? do-calculations //calculate connected nodes
    update-plots //update the plot
  ]
  [ user-message "all edges have already been rewired once" ] // alert if all edges have been rewired 
end // end the function
```




On the context of the network **rewire** means changing one end of a connected pair of nodes and keeping the other end the same.

#### Code for the `Diameter` Procedure: 
```	
Extensions
[
  nw
]

to diameter
  show max [max[NW:distance-to myself] of other turtles] of turtles
end
```


### Results

The Result of `Clustering Coefficient`, `Average Path Length`, and `Diameter` at the beginning of a Watts-Strogatz model with **50 nodes** and with `rewiring-probability` of **0.30** is:-

	Clustering Coefficient = 0.5
	Average path length = 6.633
	Diameter = 13


#### Images of `rewire-one`

<!-- Figure 1 	![Network](C:\myGit\project\socialnets18\assignments\images\default.png) -->
Figure 1 	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/default.png)


**Figure 1** is the view before we apply any method and all the nodes have two closest neighbors both on the right and the left.

<!-- Figure 2	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-one1.png) -->
Figure 2	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-one1.png)

After using the `rewire-one` method we can see that only one node is rewired using the `rewire-one` method and it has disconnected its edge from the closest neighbor and connected to another node that is more further. and same thing applys for both **Figure 3** and **Figure 4**.

<!-- Figure 3	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-one2.png) -->
Figure 3	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-one2.png)


<!-- Figure 4	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-one3.png) -->
Figure 4	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-one3.png)

<!-- Figure 5	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-one4.png) -->
Figure 5	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-one4.png)

<!-- Figure 6 	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-one5.png) -->
Figure 6 	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-one5.png)

On the above **Figure 5** and **Figure 6**, i use the `reiwire-one` botton many time so the node has found neighbor-to-neighbor connection that the yellow button representing. 



When we use the `rewire-one` method the result of the **clustering-coeffiecient** and the **average-path-length** will reduce when we click the `rewire-one` button, this is because of the probability of neighbors being neighbors to each other is decreasing.


when we decrease the `rewiring-probabiliy` value the number of nodes that gets rewired will also decreases.


##### Images of `rewire-all`


<!-- Figure 7	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-all1.png) -->
Figure 7	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-all1.png)

<!-- Figure 8	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-all2.png) -->
Figure 8	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-all2.png)

<!-- Figure 9	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-all4.png) -->
Figure 9	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-all3.png)

<!-- Figure 10	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-all3.png) -->
Figure 10 	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-all4.png)

<!-- Figure 11	![Network](C:\myGit\project\socialnets18\assignments\images\rewire-all5.png) -->
Figure 11 	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/rewire-all5.png)

The `rewire-all` method re-creates the initial network and rewires all the edges with the current `rewiring-probability`.
as we can see in the above **Figures 7-11** all nodes are rewired. And on **Figure 10** and **Figure 11** their is neighbor-to-neighbor connection represented by the yellow line connecting the two nodes.







### Discussion
<!-- Figure 12	![Network](C:\myGit\project\socialnets18\assignments\images\dm.png) -->
Figure 12	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/dm.png)

The **clustering coefficient** changes when we rewire because the probability of the neighbors being neigbors to each other changes when we rewire.

For example when we use the `rewire-one` method the value of the **clustering coefficient** reduces and its because of the random node that gets rewired will be rewired to another node that is fewer step away from its neighbours.
and the probability of neighbors connecting to each other will decrease. we can see this on the above **Figure 12** the blue dots that is the **clustering coefficint** decreasing.


The `rewire-all` version show a distribution of metrics when i run the model with the same settings because it visits all edges and tries to rewire them. The `rewiring-probability` slider determines the probability that an edge will get rewired. Running `rewire-all` at multiple probabilities produces a range of possible networks with varying `average-path-lengths` and **clustering coefficients**.As indicated in **Figure 12**.


These two plots are separated because the x-axis is slightly different. On the `rewire-one` x-axis is the fraction of edges rewired so far, whereas the `rewire-all` x-axis is the **rewiring-probability**.



## Part 2: Segregation
### Methods

By using the default metrics that is a **150x150 grid**, and **88%** `density`, and also **30%** `similar-wanted` i observed `%-similar` is around **50%** because each agents starts with an equal number of **unhappy agents** around them. but after i click the `go` button `num-unhappy` agents will be **0** and `%-similarity` increases to around **74%** using differnet number of agents. The reason for `%-similarity` result giving almost around **74%** is because we set `%-similar-wanted` to **30%**. If we increase the number of `%-similar-wanted` the `%-similarity` also increases.

### Results


```
density = 88%
%-similar-wanted = 30%
\# agent = 2306 
% similar = 49.3
num-unhappy 406
% unhappy 17.6
```

using the above values the result will change to

```
% similar = 73.7
num-unhappy = 0
% unhappy = 0
```
### Discussion

I have observe some intersting things on the segregation model,one thing i noticed is when i set the `%-similar-wanted` to 100% it took more than 3000 ticks and there was still 99% unhappy agents this is because its trying to make all the agents happy and i dont think it will be achived.
and also i observe when i increse `%-similar-wanted` to higher percentage the `%-similar` also increases with it.



## Part 3: Giant Component

### Methods

When i observe how the model with the default setup i noticed  at first all the nodes are not connected. But when we push the go once button or go button they start connecting to each other and their is no priority for the nodes to be connected to each other they chose a random node to connect to. And i also noticed that the Giant Component plot value increases when a new node is added to the big Giant Component. And also when i press the redo layout button the layout will start changing, to improve the previous layout.

### Results

The `layout` procedure (function) shows how the nodes are connecting when we click the `go once` button or `go` button and it gives the user which nodes are connecting and how the **Giant Component** is forming. Down below is the default code for the layout 

```
to layout
  if not layout? [ stop ]

  repeat 10 [
    do-layout
    display  
  ]
end
```

I have made change to the `repeat` value which was **10** to **2** and the layout started creating the nodes much faster but a poor layout. And also i have set the value of `repeat` to **20**, at this time it took more time and gives a more clear layout. 


**changed codes**
```
//seting the value to 2

to layout
  if not layout? [ stop ]

  repeat 2 [
    do-layout
    display  
  ]
end

//seting the value to 20

to layout
  if not layout? [ stop ]

  repeat 20 [
    do-layout
    display  
  ]
end
```
### Discussion

i noticed on the `Growth of the giant component` plot that when a node is connecting to a node that is already in the **Giant Component** the y-axis (Fraction in giant component) value stays constant but when a new node is added to the **Giant Component** the value of y-axis increases. And after all new nodes are connected to the **Gaint component** the y-axis will stay constant to the value of 1.


<!-- Figure 13	![Network](C:\myGit\project\socialnets18\assignments\images\d1.png) -->
Figure 13	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/d1.png)

`Growth of the giant component` plot at **ticks 12**

<!-- Figure 14	![Network](C:\myGit\project\socialnets18\assignments\images\d2.png) -->
Figure 14	![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/d2.png)


`Growth of the giant component` plot at **ticks 28**
this show that the y-axis value stayed at 1 after all new nodes are connected to the **Giant Component**.

## Conclusion

In this assignment i learn about the small worlds phenomenon, the idea that a person is only a couple of connections away from any person in the world. And also if a network has a Giant Component, that means almost every node is reachable from almost every other node. And i have take a look at Random networks with different example and how they communicate.