# Assignment 2: Detecting Communities
Alula Tsegaye

## Introduction
people can be connected because of different reasons like they may share certain attributes, properties, in different aspects in life as a result communities are detected.
As Social network analysis investigates diffrent social structures through the use of networks and graph theories. we use it to classify different the following communities.
The following are emails exchanged among people found in diffrent departments.

## Part 1: Email-EU-core network
### Methods
I used The Louvain Method for community detection since it's a method used by gephi tool which i prefered to use to extract communities from large networks like EU core networks. 
The inspiration to use this method of community detection is the optimization of Modularity as the algorithm progresses. Modularity 
is a scale value between -1 and 1 that measures the density of edges inside communities to edges outside communities.
### Results
ranking made for both communities by degree attribute
I used the force atlas layout since its principle is easy as linked nodes
attract each other and non-linked nodes are repelling eachother.
#1. In ground truth communities, 32 communities were discovered After running the modularity and by implementing the partition. A random color has been set for
 the top 11 deparmtments. community 1 ranges in with the biggest with 95.85% where as other communities outside the top 11
 (21 communities) are 0.1% each hence each are set with the same color.
##other metrics for ground truth communities
#1.average path length= 3.02
#2.avg. clustering coefficient = 0
#3.modularity= 0.921, which is meaningful given its greater the 0.4 
#2. for the algrorithm communities there are 92 communities detected out of which the top five communities ranked include communities 1,2,4,3,7 repectively with values 7.06%,4.78%,3.28%,3.08%,2.59%
##metrics
#1.average path length= 2.65
#2.avg. clustering coefficient = 0.372
#3.modularity= 0.417

### Discussion
With in the organisation there are different communities detected hence, in ground truth communities every member in the organisation is a member of one of the departments found in the organization
so diffrent department related informational emails are exchanged with other departments and the other way round. the graphs are a similar in the manner 
in which they are set up but different in which connection is the priorty in algorithm communities.
