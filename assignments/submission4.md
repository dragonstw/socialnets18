# Assignment 4: Networks over time
Tinsae Getachew


## Introduction
Assignment four is about growing networks over time. The network we are given is the Euemail network but now it has time added to it. I need to calculate the averagepath length, bridges, clustering coefficient and determine number of communities.

## Methods
I used Gephi because it is the tool we used in previous assignments and is easy to use. The .txt file was changed to .csv and the header were changed to Source, target & time.

## Results
The values of the different matrices; Modularity: 0.666, Number of Communities: 15, Diameter: 7, Average Path length: 2.67, Number of Weakly Connected Components: 1, Number of Strongly Connected Components: 182.

I used the time as a filter to see the graphs at different times. Here is what I calculated for 20 weeks, 30 weeks and 40 weeks;

20 weeks average path length 4.546 and coefficient 429
![](week20.png)
30 weeks average path length 3.937 and coefficient 354
![](week30.png)
40 weeks average path length 2.165 and coefficient 309
![](week40.png)

Different communities clustering coefficient values 1 = 0.862, 2 = 0.204, 3 = 0.422, 4 = 0.208, 5 = 0.214, 6 = 0.435, 7 = 0.562, 8 = 0.621, 9 = 0.342, 10 = 0.755, 11 = 0.686, 12 = 0.454, 13 = 0.326, 14 = 0.264, 15 = 0.648.
![](module.png)

## Discussion
There are different nodes and links that develop over time. The answer for the question is that a bridge person is more efficient in communication and here is why. The number of components decreases as the time increases at the same time this means number of bridges increase too. The average path length decreases this time. A graph with a lower average pathlength is efficient.

## Conclusion
I enjoyed this assignment very much even though it was challenging. The data type was new and it was interesting seeing how the graph can have different properties at different times. And it was nice to see that you can get relevant data from real life scenarios.