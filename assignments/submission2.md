# Assignment 2: Detecting Communities
<Fikir> <Awoke>


## Introduction
The aim of this lab is to teach us about community detection and partitioning and to help us in using different algorithms and tools inorder to partition communities. so i have looked at two different socialnetworks and done the community detections, the methods i used and results i found during this assignment is listed below.

## Part 1: Email-EU-core network
### Methods
On preparing the data i used gephi tool to partition the graphs and for community detection. So by importing the graphs into gephi it made it easy for me to partition the graph. The algorithm i choose is called splitting modularity and louvain algorithm. The reason that i choose this algorithm is because it is simple, efficient and easy-to-implement for identifying communities in a network. It worked perfectly with the directed graphs.  
### Results
As i have used the louvain algorithm the distribution of community size in the algorithm-communities is represented by a percentage on the modularity class. The first largest algorithm-community is 23.88% and the second one is 17.51%. While in the ground-truth communities the community distribution is also represented by a percentage in the department class. Here the first largest community is 10.85% and the second one is 9.15%.
I have not found other statistics that characterize the two communities. After looking at 1-2 largest algorithm-communities vs. ground-truth-communities 0.372 portion of the nodes overlap.

Community Distribution Statistics:

Average Degree = 25.444

Average Weighted Degree = 25.444

Modularity = 0.413

Network Diameter = 7

Average Clustering Cofficient = 0.372

Average Path Length = 2.653

Graph of Algorithm-community

![Alt text](emailnew.svg)

### Discussion
Community detection is a fundamental task of network science that seeks to describe the large-scale structure of a network by dividing its nodes into communities, based only on the pattern of links among those nodes. And we identify networks with explicitly labeled functional communities to which we refer as ground-truth communities. They are detecting different aspects of the network. It is as i expected. 

## Part 2: YouTube social network
### Methods
In partitioning the graphs i used gephi, the same tool i used for the Email-EU-core data. I also choose the Louvail algorithms for the same reasons and also as this youtube network is a much larger network than the first one this algorithm is better for identifiying communities in larger networks. This graph is undirected graph unlike the first one. 
### Results
The first largest algorithm-community represented in the modularity class is 18.14% and the second one is 14.93%.

Community Distribution Statistics:

Average Degree = 1.525

Average Weighted Degree = 1.706

Modularity = 0.792

Network Diameter = 9

Average Clustering Cofficient = 0.069

Average Path Length = 3.119

After looking at 1-2 largest algorithm-communities vs. ground-truth-communities 0.069 portion of the nodes overlap.
### Discussion
Community detection is a fundamental task of network science that seeks to describe the large-scale structure of a network by dividing its nodes into communities, based only on the pattern of links among those nodes. And we identify networks with explicitly labeled functional communities to which we refer as ground-truth communities. They are detecting different aspects of the network. It is as i expected. 

## Conclusion
While doing this assignment i have gone through different difficulties in understanding and analizing the data and also during the writeup. But finally i have been able to understand and  prepare the above writing.
Generally i have learned how to partition communities and about community detection.  