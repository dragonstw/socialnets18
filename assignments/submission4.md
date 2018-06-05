# Assignment 4: Networks over time
Fikir Awoke


## Introduction
In Learning Social Network through out this semester we have looked and done different assignments on social networks, Communities and Random networks. And in this assignment we are analysing the part called Growing networks or Networks over time which show as how networks evolve over time. 

## Methods
While doing this assignment I was not able to use snap.py library because of some problems in installation and opening of the files. so I switched to Gephi tool and imported the email temporal file in to it by dividing the numbers into source, target and time. To find the results asked and the temporal analysis I used the statistics and filter table in Gephi, I also used excel for calculating the mean and standard deviation values.  
## Results

Total Number of nodes= 986

Total Number of Edges= 24929

Number of Weakly connected components= 1

Number of Strongly connected components= 184
 
Average clustering coefficient= 0.352

Average path lenght= 2.653

Average Node Degree= 25.283

![PNG_image](Original temporal.png)


For the email-Eu-core-temporal data I found the mean and standard deviation of time for a new edge to form by importing the data into excel and calculating based on the formula provided by excel.

	Mean = 209.005 and Standard deviation = 40756.87

clustering coefficients within communities	

	Community 0 (2.64% of the total)= 0.009
	Community 1 (7.71% of the total)= 0.042
	community 2 (8.72% of the total)= 0.042
	community 3 (3.14% of the total)= 0.023
	community 4 (4.87% of the total)= 0.025
	community 5 (12.37% of the total)= 0.06
	community 6 (3.04% of the total)= 0.02
	community 7 (21.7% of the total)= 0.084
	community 8 (5.78% of the total)= 0.026
	community 9 (10.14% of the total)= 0.048
	community 10 (2.74% of the total)= 0.019
	community 11 (3.65% of the total)= 0.026
	community 12 (3.04% of the total)= 0.016
	community 13 (9.43% of the total)= 0.041
	community 14 (1.01% of the total)= 0.001

Temporal Analysis

	First starting at time 12,096,000 :
	The Average clustering coefficient becomes 0.332 
	The Average node degree becomes 21.523
	The Average path length becomes 2.686
	Number of Weakly connected components becomes 38
	Number of Strongly conneted components becomes 213

![PNG_image](12096000 time.png)

	Then starting at time 18,144,000 :
	The Average clustering coefficient becomes 0.324 
	The Average node degree becomes 20.139
	The Average path length becomes 2.709
	Number of Weakly connected components becomes 60
	Number of Strongly conneted components becomes 237

![PNG_image](18144000 time.png)

	Then starting at time 24,192,000 :
	The Average clustering coefficient becomes 0.300 
	The Average node degree becomes 17.879
	The Average path length becomes 2.767
	Number of Weakly connected components becomes 75
	Number of Strongly conneted components becomes 252

![PNG_image](24192000 time.png)

## Discussion

	Question: Are "bridge" people more efficient or less efficient at email communication?

According to the results found above bridge people are less efficient in email communication. This is because as listed on the above results when the starting time increases the Average path lenght also increases, this shows us the decline in bridge person, as a result the role of this bridge people in connecting many different people will also decrease.
On the other hand as the Average clustering coefficient decreases with an increasing starting time in the results it will likely show as the decrease in well connectance of the edges and the number of edges, so this will inturn affect the role of a bridge person in connecting different others. so i concluded that bridge people are less efficient at email commuication.
But this does not mean they are not efficient, it means they are helpfull but not enough.

## Conclusion
During this assignment I have learned and analized how networks change over time. As this is our last assignment for this course, I would like to say that I have learned a lot about social Networks and I appreciate your effort in teaching us. 