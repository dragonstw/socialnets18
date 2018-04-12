# Assignment 2: Detecting Communities
<Fikir> <Awoke>


## Introduction
The aim of this lab is to teach us about community detection and partitioning and to help us in using different algorithms and tools inorder to partition communities. so i have looked at two different socialnetworks and done the community detections, the methods i used and results i found during this assignment is listed below.

## Part 1: Email-EU-core network
### Methods
On preparing the data i used gephi tool to partition the graphs and for community detection. So by importing the graphs into gephi it made it easy for me to partition the graph. The algorithm i choose is called splitting modularity and louvain algorithm. The reason that i choose this algorithm is because it is simple, efficient and easy-to-implement for identifying communities in a network. It worked perfectly with the directed graphs.  
### Results
As i have used the louvain algorithm the distribution of community size in the algorithm-communities is represented by a percentage on the modularity class. The first largest algorithm-community is 13.23% and the second one is 7.26%. While in the ground-truth communities the community distribution is also represented by a percentage in the department class. Here the first largest community is 10.85% and the second one is 9.15%.
I have not found other statistics that characterize the two communities. After looking at 1-2 largest algorithm-communities vs. ground-truth-communities 0.186 portion of the nodes overlap.

Community Distribution Statistics:

Average Degree = 12.722

Average Weighted Degree = 25.444

Modularity = 0.414

Network Diameter = 7

Average Clustering Cofficient = 0.186

Average Path Length = 2.653

Graph of Algorithm-community

![Alt text](emailnew.svg)

### Discussion
Community detection is a fundamental task of network science that seeks to describe the large-scale structure of a network by dividing its nodes into communities, based only on the pattern of links among those nodes. And we identify networks with explicitly labeled functional communities to which we refer as ground-truth communities. They are detecting different aspects of the network. It is as i expected. 

## Part 2: YouTube social network
### Remark
In the part 2 of the assignment i got in to a problem when tring to get the graph in to gephi. As the data is a much bigger data my machine was not able to load it.First i was able to load the youtube.top5000.cmty data in to gephi but then when i tried to import the youtube.ungraph data it was not able to load it and open it in gephi. So for that reason i could not get the right modularity class.   
### Methods
...
### Results
...
### Discussion
... 

## Conclusion
While doing this assignment i have gone through different difficulties in understanding and analizing the data and also during the writeup. But finally i have been able to understand and  prepare the above writing.
Generally i have learned how to partition communities and about community detection.  