# Assignment 2: Detecting Communities
sophonias bekele


## Introduction
This Lab help me to visualize communities in larger networks like amazon,youtube etc.. 
  


## Part 1: Email-EU-core network
### Methods
1. download email-Eu-core.txt and email-Eu-core-department-labels.txt
2. edit .txt format to csv and Add headers like NODEID,DEPARTMENt,Source and target
3. I import spreadsheet email-Eu-core-department-labels.csv as Node Table and email-Eu-core.csv as Edge Table into Gephi
4. After importing i run Avgerage weighted degree and do size ranking using weighted-in-degree value
5. then i run Fruchterman-Reiheavyngold layout and Force Atlas2 layout 
6. finaly i did partition based on department


### Results
![email](email.png)


ground truth is based on heavy corelation and algorthm is based on internal connectivity

* Ground truth-communities
 :-Average degree = 0.999, Modularity = 0.921, Average weighted degree = 0.999 etc..
* algorithm-communites
:-Modularity = 0.415, graph Density = 0.025, connected components = 20 etc..

In Ground truth-communities there is less communities in the modularity section of statistics
In algorithm-communites there is more node overlap

![email](plot.png)


### Discussion
In running both ground-truth-communities and algorithm-communities there is some stastics in case of ground truth there is 1005 nodes and 1005 Edges but incase of algorithm communites there is 1005 nodes and 25,571 Edges and also in the modularity section in ground truth there is less communities than in algorithm also when we other statistics there is some big difference in the data.


## Part 2: YouTube social network
### Methods
1. Download com-youtube.ungraph.txt and com-youtube.top5000.txt
2. Edit .txt format to csv and Add headers like Source and target
3. I import spreadsheet om-youtube.ungraph.csv as Node Table and com-youtube.top5000.csv as Edge Table into Gephi
4. After importing i run Avgerage weighted degree and do size ranking using weighted-in-degree value
5. beacause of performance issue i did not complete from this part

### Results


### Discussion


