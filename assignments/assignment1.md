### Introduction

we did this lab to get into more in depth with network analysis. on this lab we will visulaize our facebook network using a tool called gephi. We will analyse how we are connected with our facebook friends and how our friends are connected to each other too.

### Methods

At first, i have faced some difficulties downloading my facebook network with lost circle using my person computer, so i tried to download it on the lab computer and it finally worked for me.

After i was done with downloading the graphml file using lost circles. i start editing my graph on gephi to give more sense and for better visualiztion. I used some of the methods and filters on gephi to edit my graph. After i finished editing, i export the file as svg as instructed and attached it down below on the result section.

### Result

1. What percent of your friends are connected (through any number of links) to most of your other friends?
		
		0.04

	a. What metric or concept is expressed by this number?
			
		connectance
2. Find the person with most friends in common with you. How many friends do they share with you?
		
		268

	a. What metric or concept is expressed by this number?
		
		node degree
	
3. On average, how many Facebook friends do your friends have?
		
		22.842

	a. What metric or concept is expressed by this number?
		
		avg node degree
 
4. Overall, how well-connected are your friends to each other? Give an answer between 0 and 1.
		
		2.559

	a. What metric or concept is expressed by this number?
		
		clustering coeffiecent
	
5. Considering possible random pairs of friends in your network, on average how close/far are your friends?

	fdasfasd

	a. What metric or concept is expressed by this number?
	
		characterstic path length

	b. Recall that you are connected to each node in the graph, though this is not shown explicitly in your data. However, not everyone else in the graph is directly connected to each other. Are you more often the shortest link between two of your friends? Or do most of your friends already know each other?
		
		i am more often the shortest link beetween my friends

6. how many friends do you have in your facebook network?
	
		(nodes - 1) = 564  we substract 1 from the nodes to remove our node from the count
	
![Network](C:\myGit\project\socialnets18\assignments\yohannes.svg)
![fdas](https://github.com/dragonstw/socialnets18/blob/develop-yohannes0842/assignments/yohannes.svg)

### Discussion

 ** connectance ** is how connected the network is so we will calculate this by using the formula => avg node degree(k)/ V - 1   where k = (2 * E) / V

** node degree ** - is the one with most friends in common with me. First of degree means the neighbour of a node so to get the one who has the most mutual friend with me i will go to the data laboratory in gephi and take the one with the highest node degree from the data.

** Avg node degree ** is the average of all node degrees.

** clustering coeffiecient ** is a measure of how complete the neighborhood of a node is. 

** characterstic path length ** is the average shortest path length or average distance. To calculate the average distance we can use the formula 
	L = 1 / (v (v - 1))

I chose to present my network this way because it give more sense since i put all the groups together using modularity class. This class will group the communities in my graph together by setting different color for the communities. And also i used the layout Fruchterman Reingold. And also i use the filter Giant Component to remove the single nodes so that the graph looks better when i export it.
