#Name: Alula Tsegaye

#Introduction
This lab is mainly useful to implement the things we learnt on lecture classes
like the network structure and graph theory and all the metrics in it. So we
are going to to implement the metrics on real-time facebook data by analysing it.
#Methods
#1 Connectance: is the proportion of possible links between nodes that are realized(links).
 So i calculated by using the formula:  K/v-1.
K= average node degree
v= vertices(nodes)
#2 Node degree: the degree of a node in a network is the number of connections it has to other nodes and the degree distribution 
is the probability distribution of these degrees over the whole network. In this question in order to find the friend with most mutual
friends with me. i calculated the number connections and degree distribution.
#3 Average Node degree: is closely related to network density. Since the question is about average number of facebook friends i have 
i will calculate the average number of connections to me. To calculate we can use the formula: K = 2E/V where:
E = number of Edges
V = number of vertices 
#4 Clustering Coefficient: In graph theory, a clustering coefficient is a measure of the degree to which nodes in a graph tend to cluster together.

#5 Characteristic (average) path length: is a concept in network topology that is defined as the average number of steps along the shortest paths for all possible pairs of network nodes. 
It is a measure of the efficiency of information or mass transport on a network.
To calculate the average path length use the formula: L = 1/V(V-1) Where:
V = Number of possible node pairs.
#Results
Network Diameter: is the longest graph distance between any two nodes :-7
Graph Density: how close the networking is to complete:- 0.053
Connected Components: a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph. For example, 
the graph shown in the illustration has three connected components:-23
Average clustering coefficient: 0.354
Average Degree: 7.671
Average Weighted Degree: 12.027
Average path length: 3.055

#Discussion of Results:
#1 In this case inorder to find out how connected my friends are to most of my other friends i used
the metric is connectance because it measures how connected a node is.
#2 Since the question is about average number of facebook friends i have 
i will calculate the average number of connections to me.
#3 Since the question is about average number of facebook friends i have 
i will calculate the average number of connections to me.
#4 So in order to find how well connected your friends are to each other, the most clustered part of the network where each nodes(freinds) are well connected to each other have similar attributes
like for example they went to the same high school and etc. The opposite goes for nodes that are separated from others having different unique attributes compared to others.  
#5 In our case to figure out how close my facebook friends are i need to calculate the average path length to know if i am the shortest link or not.

# For the network i used the Yifan hu multilevel layout because it is a very fast algorithm with a good quality on large graphs. It combines a force-directed
model with a graph coarsening technique (multilevel algorithm) to reduce the complexity. The repulsive forces on one node from a cluster of distant nodes are approximated by
a Barnes-Hut calculation, which treats them as one super-node. It stops automatically.