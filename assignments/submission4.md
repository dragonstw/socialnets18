# Assignment 4: Networks over time
Habteab Yohannes


## Introduction
This lab involves studying about temporal analysis and the importance of bridge in email communication. Previously we have done a static email data from core network and in this lab we have a temporal version.
## Methods
1. First I converted the text file into .csv 
2. Open the data in gephi
3. Gephi has a filtering function. In the filter select attributes 
> timestamp and then drag the timestamp into queries below the filter box. 
4. Set the slider starting at time 12,096,00, at time 18,144,000 and at time 24,192,000 respectively

## Results
Clustering coefficient: 0.352

Average degree: 25.283

Network Diameter: 7

Avg. Path legnth: 2.653

Nodes: 986

Edges: 24929

At 12,096,00

![screenshot1](sc1.png)
At 18,144,000

![screenshot2](sc2.png)
At 24,192,000

![screenshot3](sc3.png)

## Discussion
As we see from the graph, there is 1 weakly connected component. This usually represent bridges. The strongly connected components are 184. Biridges are efficient for email communication for weakly connected components. Otherwise, for strongly connected components because they already know each other it doesnt matter.
## Conclusion
From doing this assignment I gain expecrience about networks that change over time and how to filter by timestamp and I have more knowledge about bridges how they link with weak or strongly connected component.