# Assignment 3: Detecting Communities
<Nahom> <Asnake>


## Introduction
In this assignement I have went though the netlogo program and saw in detail of how things worked from our social analysis class, I have also been able to go though the netlogo program and have a deeper understanding of how the application worked by modifying the program and see the effects as I did. 
## Part 1: Small Worlds
### methods
After reading the netlogo user manual and going through the examples including the commands and procedures, I experimented by altering the 
procedures . Then I continued by first understanding the difference between observer, turtle, reporter and patch also how they are reflected
on the model. For instance the rewire one procedure is used by to detach the link from one node and connecting it to another node(rewiring it)
this procedure is written to also handle request from the rewire-all procedure and the nodes are graphically represented by the turtles. To further
explain the code '''if count turtles != num-nodes [
    setup
  ]'''
makes sure that that the amount of turtles reprented in the model are equal with the amount of nodes specified by the setting if not it will invoke
the setup procedure which will make sure that the model is properly setup with the setting. The variables '''' set rewire-one? true
  set rewire-all? false''' will determine whether the button rewire-one or rewire-all is pressed. '''let potential-edges links with [ not rewired? ] '''
  sets up the potential-edges variable with list from 'links' that are not in 'rewired?' variable which means it will set it up with links that are 
  not rewired   '''ifelse any? potential-edges [''' will check if there is at list one potential-edge i.e. it will check if there exists at least one
  that is not rewired if all of them are rewired then it goes to the else statatement which is '''[ user-message "all edges have already been rewired once" ]'''.
But if not this gets executed (I will make a java comment for expanation)
'''ask one-of potential-edges [  /// from an observer it picks one of the potential-edges to give them orders
     
      let node1 end1 /// the first end of the edge will be make the node 
      if [ count link-neighbors ] of end1 < (count turtles - 1) // this performs a check whether the node is connected to every other node 
      [
        ;; find a node distinct from node1 and not already a neighbor of node1
        let node2 one-of turtles with [ (self != node1) and (not link-neighbor? node1) ] // this picks a node for every other nodes that are not connected to node1 and 
        // it self
        ask node1 [ create-link-with node2 [ set color cyan  set rewired? true ] ] // create the link with node2
        set number-rewired number-rewired + 1  // counter for number of rewirings
        die
      ]
    ]
    let connected? do-calculations  // do-calculations returns whether the graph is connected or not and also recalculates the adl, cc, diameter(In my case)
    update-plots // this procedure update the model graphically

    '''
It took me a long time and lots of errors to understand, the distance-from-other-turtles contains a list of lists (multidimentional) when the find-path-length is called 
this list is populated with a distance from each node to every other node so the maximum of this distances will be the diameter of the graph. So in the do-calculations
'''set diameter max [max distance-from-other-turtles] of turtles''' will find the largest distance(i.e diameter) which I shall later use in the monitor. I have also declared the variable in the global including the diameter lattice. 

### Results
At the beggning it had a clustering coeficient of 0.5 , average-path-length of 6.633, and a diameter of 13. 
![Small-worlds]('picture-with-model picture with rewire.png')
The plots are made by normalizing the reported data by the lattice. In our model at the begging of the model the values are as described above and these values are also
recorded on the lattice when we called the setup procedure.  So the rewire one network properties shows us fraction-of-edge-rewired against the normalization of the three
attributes(diameter...) as we hit the rewire one button the fraction-of-edges rewired will increase(x axis) and normalzation of the values varry in regard to the graph created . The normalization will always be one at the begginng because we are dividing it with the initial value when we setup the network as the current values change when we hit the rewire one button. And as for the rewire all button its against the rewiring probablity that we set so it wont change if we don't change it.

### Discussion
The clustering coefficient changes as nodes are rewired, because it calculates how good each node's neighbor's are connected to each other therefore if we change the edges their is a good chance that these values change. And the rewire all show a distribution of metrics when we run it because it rewires nodes according to the rewiring-probablity. Since the rewiring affects the cc, apl, and diameter the distribution also gets changed in regard to the graph created. The plots are shaped the way they are because as I described in the results section. The rewire one network properties shows us fraction-of-edge-rewired against the normalization of the three
attributes(diameter...) as we hit the rewire one button the fraction-of-edges rewired will increase(x axis) and normalzation of the values varry in regard to the graph created . The normalization will always be one at the begginng because we are dividing it with the initial value when we setup the network as the current values change when we hit the rewire one button. And as for the rewire all button its against the rewiring probablity that we set so it wont change if we don't change it.


## Part 2: Segregation

### Methods
Before I changed the tollerance, I imagined that a maximum of intollerance(similar wantedness) would result in the visualization completly separating the red agents from the blue agents and resulting in distinct grouping of the agents so as I increased the value of intollerance, similar grouping increased and when I reached 75 the result was a disctinct similarity grouping. I have also been working on tring to understand the code and how it's reflected on the model by tweaking some variables and procedures.I have changed the grid to 150 and tried playing with the neighbors as described on the hint what I did was I added the blue neigbors with the red neighbors subtracted from the 8 which gave me the resutls the amount of empty neighbors but this had a flow because it did not account for the once that were aligned with the grid which had only 5 possible neigbors.  


## #Results
I have set the values as the book and rerun with the modified code but the results were not exaclty the same and mine count not finish the models because of the modified code.

### Discussion
I found the model interesting in many ways, one thing is that in a case where each agent wants 30% same color neighbors the agents in average endup with a 70% same-color-neighbors so few individuals preference will lead to a significant segregation. And I also found even at a density of 99% its possible to keep all the population happy when the similar wantedness is set to less than or equal to 60% but even after that we can keep the unwanted population less than 10 percent all the way upto 80 percent. 

## Part 3: Giant Component
### Methods
I ran the model with the default setting and also tweaking the num-nodes I also changed the layout toggle to off and saw the effect as well I also saw the effect of the the redo layout toggle button. I also set the speed to slow and saw how the links forming afected the giant component and how the plot reacted.I also found that the model was much faster when using continious than ticks

### Results and Discussion
I have changed the numofnodes several times and I have been able to observe the size of the network and how fast it grew one interesting fact is that the giant components composes of all nodes in a maximum of 10 connections pernode mostly less than 5 even though the edges randomly form as described in the documentation.By the time that the run is over, the clustering cooficient will be exactly one. And the connection pernode will be equal to the num-node. 


## Conclusion
In conclusion I have leaned a lot from this assignement and tried many models as well that are not required in the assignment. 










