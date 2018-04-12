***********
# Submission 2: Detecting Communities

### **yohannes Endale**

## Introduction
This lab is about Detecting Communities. On this lab i look at two different social networks.  The first network i look at is a "who-talks-to-whom" (actually, who-emails-whom) snapshot from a European research institution. The second network is a network of YouTube users. The tools are optional but i use gephi for analysis and partitioning.

## Part 1: Email-EU-core network

### Methods

For this assignment i used a tool called called **Gephi** to partition and analyse the graph from the given data. The data come from a nice collection of networking data sets hosted by the Social Network Analysis Project (SNAP) group at Stanford University.

The first thing i did is apply a filter called **Giant Component** that will get rid of nodes that are single and floating on the outside. Nodes that  doesn't do too much for this analysis.
Then i start calculating some metric in order to start my analysis and partition. Next to reflect the metrics in the actual graph view, i have play around with some of the algorithm and i chose the **modularity class** algorithm. 
>The reason i chose modularity class algorithm is it scan the density of the connections between the nodes, and the nodes that are more densely connected to one another are considered to belong to the same community.

I also gave the modularity class a ranking size of 5-40 so that i can have differnt sizes of nodes. and also gave it differnet kind of colors.

Then i chose the layout called **Fruchterman Reingold** for the ground-truth-communities. The reason i chose this layout is because the ground-truth-communities doesn't have that much Edges so that Fruchterman Reingold layout can show the nodes and edges clearly. 

![Network](C:\myGit\project\socialnets18\assignments\gtc1.png)
![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/gtc1.png)

And for the algorithm-communities i choose **ForceAtlas 2** layout.
>The way ForceAtlas algorithm works is that the nodes with the higher degree are pulled toward the nodes with the highest degree.

So using this i get a nice layout where clusters are organized around nodes with the highest degree, while the communtites that are formed around them are pushed away from each other.

![Network](C:\myGit\project\socialnets18\assignments\al1.png)
![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/al1.png)


### Result

Ground-truth | algorithm-community | Stastitics
-------------| ------------------- | ----------
79.6% visible| 98.11% visible      | nodes
1            | 25.915              | Average Degree
1      		 | 25.915              | Average Weight Degree
0.904        | 0.196               | modularity
0 			 | 0.379               | Average Clustering Coefficent
0.001 		 | 0.026 			   | Graph Density


Yes, their are other other statistics that characterize the two types of communities and this are **graph density, modularity and also average degree**.

The node overlap for the algorihtm-communities is **0.379** and 
The node overlap for the ground-truth-communities is **0**. For the ground-truth-community their is no node overlap meaning one node have only one community and also each node has one out-degree.

### Discussion

When we compare both communities the agorithm-communities have 24 communities and the ground-truth-communities have 7 communities.

when we look at the average degree for both communities it is **1** and **25.915**. This shows as that for the ground-truth-communities the number of nodes and number of edges are equal giving the value of **1**, when we divide them. And for the agorithm-communities the average degree is **25.915**.

when we look at the modularity for the ground-truth-communities most of the nodes are in a community as we can see on the graph so that gave as a big value close to 1.

## Part 2: YouTube social network
### Methods

For this assignment i used a tool called called **Gephi** to partition and analyse the graph from the given data. The data come from a nice collection of networking data sets hosted by the Social Network Analysis Project (SNAP) group at Stanford University.


The first thing i did for algorithm-communities is apply a filter called **Giant Component** that will get rid of nodes that are single and floating on the outside. Nodes that  doesn't do too much for this analysis.
Then i start calculating some metric in order to start my analysis and partition. Next to reflect the metrics in the actual graph view, i have play around with some of the algorithm and i chose the **modularity class** Attributes filter so that i can only show the higher percentage communities since the data is big. so i ignor the modularity class below 1% and now i can only see 60% of the nodes and 67% of the edges using modularity filter.

Then i chose the layout called **ForceAtlas 2** for the algorithm-communities. 
>The way ForceAtlas algorithm works is that the nodes with the higher degree are pulled toward the nodes with the highest degree.

So using this i get a nice layout where clusters are organized around nodes with the highest degree, while the communtites that are formed around them are pushed away from each other.

![Network](C:\myGit\project\socialnets18\assignments\al2.png)
![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/al2.png)

And for the ground-truth-communities i choose **Fruchterman Reingold** layout. The reason i chose this layout is because the ground-truth-communities only have 10  Edges and 10 nodes so that Fruchterman Reingold layout can show the nodes and edges clearly and i also gave it label to identify the ndoes easily. 

![Network](C:\myGit\project\socialnets18\assignments\gtc2.png)

![Network](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/gtc2.png)

### Results

Ground-truth | algorithm-community | Stastitics
-------------| ------------------- | ----------
79.6% visible| 98.11% visible      | nodes
0.9          | 1.525               | Average Degree
0.9    		 | 1.706               | Average Weight Degree
0            | 0.735               | modularity
0 			 | 0.086               | Average Clustering Coefficent
0.1 		 | 0    			   | Graph Density


The node overlap for the algorihtm-communities is **0.086** and 
The node overlap for the ground-truth-communities is **0**.  For the ground-truth-community their is no node overlap meaning one node have only one community and also each node has one out-degree.

### Discussion

When we compare both communities the agorithm-communities have 33 communities after applying the modularity algorithm choosing only communities with higher degree and the ground-truth-communities have 0 communities.

when we look at the average degree for both communities it is **0.9** and **1.525**. And we get this by dividing the Edges with the Nodes.

when we look at the modularity for the ground-truth-communities all of the nodes doesn't have a community as we can see on the graph. 

Since the network was big it wasn't easy to choose any algorithm because some of the algorithm take the higher percentage of nodes part it was hard changing the layout since it need a good memory and processor. So because of this i have to reduce the size of the nodes first to change the layout and chose one that displays the graph easily.

## Conclusion

On this lab Assignment we are able to analyze a big size of nodes and look at some new algorithms to analyze network data. And we have look at differnet community detection methods.

And yes there Were differences between Part 1 and Part 2 the first one is the computer memory and processor, for Part 1 since the nodes aren't that much i have played with differnt algorithm easily and look at different algorithms, layout and filters too. but for the second one their were lot of limitation to check different algorithm.

Another difference in this two social network is the way their nodes are connected in the ground-truth-community for part 1 all of the nodes have only one out-degree this shows as sending of one email to another node. But for part 2 their are different number of out-degrees.

When detecting communities in this two graph it was easy to identify departments or communities for part 1 but for part even though i try to reduce the size of nodes it is not easy to identify communities on the graph.

