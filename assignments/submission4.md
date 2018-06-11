# Assignment 4: Networks over time
Misle Amha


## Introduction
Unlike from the previous assignments on static network, this assignment describes and leads us to dynamic networks which grow over time. This makes networks more interesting and help to discover more. 

## Methods
Similar to the previous assignments i used gephi tool to demonstrate the graph and get the statistics, as it makes it easy for me to use. I got the results below from the statistics table on gephi. And by sharing ideas with my class mates i got to calculate the clustering cofficient of communities by using filtering and also done the temporal analisis with the same procedure.  

## Results
At first when the email-eu-core-temporal graph is imported to gephi it has a 986 number of nodes with 24929 number of edges. And the connected components are categorized into strongly and weakly connected nodes which has the value of 184 and 1 respectively. The Average path lenght and  Network Diameter as calculated on the statistics has 2.653 and 7 respectively. The major metric which is the Average clustering coefficient is equal to 0.352.

The clustering coefficient within communities show the following distribution, there are fifteen number of communities with modularity of 0.664 from 0 to 14:

-community 14 = 0.042

-community 13 = 0.025

-community 12 = 0.036

-community 11 = 0.043

-community 10 = 0.028

-community 9 = 0.02

-community 8 = 0.001

-community 7 = 0.034

-community 6 = 0.023

-community 5 = 0.016

-community 4 = 0.007

-community 3 = 0.061

-community 2 = 0.024

-community 1 = 0.079

-community 0 = 0.037


The following is the picture of the graph that is seen at first:
![PNG_image](img1.png)

The Mean value is equal to 209.005 and the Standard deviation is equal to 40756.87 as calculated in Microsoft excel.

The Temporal analysis in the step 4 is shown below:

-When the starting time is 12,096,000 as given we get the following results that differ from the original:

Strongly connected components = 214

Weakly connected components = 38

Average path lenght = 2.689

Network Diameter = 6

Average clustering coefficient = 0.331

![PNG_image](first img.png)

-When the starting time is 18,144,000 as given we get the following results that differ from the above:

Strongly connected components = 238

Weakly connected components = 60

Average path lenght = 2.709

Network Diameter = 6

Average clustering coefficient = 0.322

![PNG_image](second.png)

-When the starting time is 24,192,000 as given we get the following results that differ from the above:

Strongly connected components = 252

Weakly connected components = 75

Average path lenght = 2.767

Network Diameter = 6

Average clustering coefficient = 0.3

![PNG_image](third img.png)

-So as seen in the above statistics an increase in the starting time results in a decrease in Average clustering coefficient and an increase in Average path lenght when filtered.

## Discussion
For the Question, which asks if bridge people are more or less efficient in email communication, My answer is bridge people are less efficient in communicating different people in a network of email. I said this because the benefits of this bridge people is less in creating a well connected environment.

## Conclusion
From this assignment i have learned about growing networks and how the change of networks overtime affect the distribution and connectedness of a network.