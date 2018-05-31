# Assignment 4: Networks over time

Yohannes Endale

## Introduction

On this Lab i have looked at networks and how they evolve over time by adding edges (links) over time. And for this lab i used a tool called **Gephi** and two **Python** library called `snap.py` and `networkx`.


`snap.py` is a Python interface for SNAP. **SNAP** is a general purpose, high performance system for analysis and manipulation of large networks.


`NetworkX` is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

## Methods

First i familiarize my self with snap.py and NetworkX library on python and I start the project using snap library for network analysis of the `email-Eu-core-temporal` data.


i used Girvan Newman community detection algorithm on snappy to detect how many communities are thier in the `email-Eu-core-temporal` data but i was not able to get a result because the data is too big i have waited the program to run for more than 8 hours. The code i used to get the number of comminities in snap is down below



```
import snap

Graph = snap.LoadEdgeList(snap.PNGraph, "email-Eu-core-temporal.txt", 0, 1)

CmtyV = snap.TCnComV()

modularity = snap.CommunityGirvanNewman(Graph, CmtyV) # to find the modularity

for Cmty in CmtyV:
    print "Community: "
    for NI in Cmty:
        print NI
print "The modularity of the network is %f" % modularity

```

Then by using **Gephi** i have got a value of **26 communities** in the `email-Eu-core-temporal` data.




## Results

Using networkx library on python i have calculated number of components and the clustering coefficient and also other statisctics.

```
import networkx as nx
from networkx.algorithms import community


graph = nx.read_edgelist('hello.txt',create_using=nx.Graph(),nodetype=int)

print 'Number of Connected Components - ',nx.number_connected_components(graph)
print 'Average Clustering - ',nx.average_clustering(graph)
print 'Is the graph fully Connected - ',nx.is_connected(graph) #return true if the graph is fully connected
print 'Has bridges',nx.has_bridges(graph)

```

![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/result1.png)
<!-- ![Network](C:\myGit\project\socialnets18\assignments\images\result1.png) -->


Image at time 12,096,000
<!-- ![Network](C:\myGit\project\socialnets18\assignments\images\time1.png) -->
![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/time1.png)

Image at time 18,144,000
<!-- ![Network](C:\myGit\project\socialnets18\assignments\images\time2.png) -->
![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/time2.png)

Image at time 24,192,000
<!-- ![Network](C:\myGit\project\socialnets18\assignments\images\time3.png) -->
![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/images/time3.png)




 Stastitics 			  | At Time 12096000 | At Time 18144000 | At Time 24192000 
--------------------------| -----------------| -----------------| ----------------
nodes        			  | 986(100%) 	  	 | 986(100%)        | 986(100%)
Edges 		 			  | 3101(11.44%)	 | 4963(19.91%)     | 7300(29.28%)
Average Degree            | 3.145            | 5.033   		    | 7.404
Average Weight Degree     | 6.097            | 11.04       		| 20.655
modularity    			  | 0.415            | 0.345   		    | 0.322
Avg Clustering Coefficent | 0.034            | 0.056   		    | 0.08
Connected Componet 		  | 251              | 194     			| 153
Avg Path Length			  | 4.137            | 3.566   		    | 3.215
Network Diameter	   	  | 10 			 	 | 8       			| 8



## Discussion

A bridge person in an organization connects many different people. So that bridge person are more efficient connecting people. For example if one person want to send a message to a different communinity and he didn't know that person directly he was going to send the message using the bridge person that is between his community and the other community. So for the abouve reason bridge persons are important. 
And also bridge persons are less efficient because it would have been easier to send the message using direct communication rather than bridge communication in the concern of speed and security.


## Conclusion

At first it was difficult for me to install snap.py library on python because of python 2.7.x compatibility but after some tryies i was able to install the library and the next hard thing was to get the result of number of communities because it was taking much time as i described it above of the methods section.

On this lab i was able to learn two new python libraries calles snap.py and networkx for analysing networks.
