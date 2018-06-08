# Assignment 2: Detecting Communities
Habteab Yohannes

## Introduction
The system shows a data about who emailed whom and how people are interconnected. For example, if one person is connected to another, both of them are considered nodes, and their connection is like department. 

## Part 1: Email-EU-core network
### Methods

Gephi is used to parse the graph from the file, first excel is required to import for gephi, then gephi will provide the necessary information. The algorithm is based on default gephi algorithms.
### Results
The modularity class is in node partition and it shows percentages of node parttion for each department the component ID is decreasing and there is few gaps between the nodes.
the modularity result is 
Modularity: 0.416
Modularity with resolution: 0.416
Number of Communities: 26

### Discussion
The distribution degree shows less density and lower population in the departments. Also the ground-truth is not implemented here but it is used to describe strongly connected components.
In general the nodes have fewer gaps between each other, some nodes probably have connections with a neighbor node of their target/source.
 Additionally, all of the edges are directed graphs because it is used to show communications.