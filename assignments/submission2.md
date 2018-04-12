 #Assignment 2: Detecting Communities

Beytula kedir


## Introduction
In this assignment, we have understand the structure of the given two different complex social networks, and ultimately extracting useful information from them.

## Part 1: Email-EU-core network

### Methods
The tool that i used to partition the graph is gephi 0.9.2 which is previously used to analyse social network in assignment1. the data is already prepared. so i did not do anything to prepare the data. i was confused to choose the algorithm. however, my classmates told me to use the louvain method for community detection. i decide to use this algorithm because when i gather information about it i have found an article which says: "The Louvain method of community detection is an algorithm for detecting communities in networks that relies upon a heuristic for maximizing the modularity. The method consists of repeated application of two steps. The first step is a "greedy" assignment of nodes to communities, favoring local optimizations of modularity. The second step is the definition of a new coarse-grained network in terms of the communities found in the first step. These two steps are repeated until no further modularity-increasing reassignments of communities are possible. The Louvain method achieves modularities comparable to pre-existing algorithms, typically in less time, so it enables the study of much larger networks. It also generally reveals a hierarchy of communities at different scales, and this hierarchical perspective can be useful for understanding the global functioning of a network. Meanwhile, there are certain pitfalls to interpreting the community structure uncovered by the Louvain Method; these difficulties are actually shared by all modularity optimization algorithms. "and it deals with a directed graph properly.

### Results
I have got a coloured community partition when i apply the partition by modularity class after running modularity. from the desplayed statisticcs, some communities have relatively high number of nodes and others have average number of nodes.
when i apply the department method of partition(ground-truth-algorithm) the null reads as 50% and others are distributed fairly.  in the ground-truth-algorithm the largest community next to null is 5.42% and in modularity class, the largest community reads as 12.69%  and the next is 7.41%
![Alt text](department.svg)
![Alt text](modularity-class.svg)
![Alt text](department.png)
![Alt text](modularity-class.png)
### Discussion

when i compare the community detection and the ground-truth communities, they did not capture the same aspects of network. since they are different algorithms, the community detection method they use is also different. this makes the result slightly different.
 ## Conclusion
from this assignment i have faced more difficulties starting from trying to understand the question. and the algorithm. thats why i am going to push it lately. 

## Part 2: YouTube social network

i cant import the data totally!