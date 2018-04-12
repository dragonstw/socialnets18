# Assignment 2: Detecting Communities
Geleta Firdissa 

## Introduction
This shows a network of communications between different people through email. A directed graph shows nodes, to which the email is sent or communicated. The graph is partitioned into 33 nodes.   
## Part 1: Email-EU-core network
### Methods
First, the node and class data is downloaded and partitioned into Gephi format csv, by importing it. Gephi partitions the rows into the id and department, and finally we save the Gephi file output. CSV is a good format for analyzing the algorithms.

The modularity class displays the algorithm used as “Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre, Fast unfolding of communities in large networks, in Journal of Statistical Mechanics: Theory and Experiment 2008 (10), P1000.” 

Fast unfolding of communities shows a better detection than modularity detection methods. Most importantly, for extracting large network communities, because modularity may not list out all possible nodes if there are too many.

### Results
The size – modularity class graph shows a very widely distributed and less dense distribution. There are 27 communities, and the resolution used is 1.0, this means very low modularity with resolution. 

Ground truth is simply, a way of being sure that a hypothesis is correct and accurate. Therefore, the nodes with highest degree of separation or recombination, and its modularity have the same result with ground-truth algorithm. And the algorithm deals with strongly-connected departments.

### Discussion
Since ground truth is used as a way of eliminating data that are not provable or statistically inaccurate. 
Therefore, when this is used it shows fewer outputs, lesser nodes in most cases. 
The other community-detection algorithms provide all information from the imported CSV, while this is good to provide data as-is, not accurate for training a system.

