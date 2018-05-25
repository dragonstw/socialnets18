# Assignment 2: Detecting Communities

In this assignment, we will look at two different social networks and consider the ramifications of our community detection decisions. This assignment will be more self-directed and subjective, ending in a write-up. However, the writing needs to be analytical and address specific points (see the grading Rubric at the bottom), and it needs to be based on actual work. Don't wait until the last minute, or your writing will be terrible.

The **data** will come from a nice collection of networking data sets hosted by the Social Network Analysis Project (SNAP) group at Stanford University.

This time you'll get to choose the **tools** you use for analysis. Here are some options:
* [Gephi](https://gephi.org/users/download/). As we saw in Assignment 1, this is a nice tool for quickly visualizing and getting basic statistics on a network.
* [Snap.py library](http://snap.stanford.edu/snappy/index.html#download). Provided by Stanford's SNAP group, this library allows you to manipulate graphs from Python code (though originally written in C++). Visualization through `gnuplot` and `graphviz`.
* [MS Excel NodeXL template](https://archive.codeplex.com/?p=nodexl). Also based on Stanford's SNAP tool, this library allows you to interact with graph data via Microsoft Excel, and is accessible to non-programmers. You can download the Basic version.

(You are not expected to write your own community detection algorithm from scratch, but of course you are welcome to do so for your own enrichment. Unfortunately, this kind of code will not be graded. In your writeup's Methods section, you should explain in detail what you did.)


## Part 1: Email-EU-core network
The first network we will look at is a "who-talks-to-whom" (actually, who-emails-whom) snapshot from a European research institution.  Thus, it is a directed graph, where a link implies the sending of at least 1 email during the observation time period. Only people and emails within the organization are included in the data set. Furthermore, each person in the organization is a member of exactly one of 42 departments in the institute.
* [Node & class data](http://snap.stanford.edu/data/email-Eu-core-department-labels.txt.gz). The nodes have a simple numeric ID and a department ID. In analyzing communities, we might consider the department ID to be a _ground-truth_ partition.
* [Edge data](http://snap.stanford.edu/data/email-Eu-core.txt.gz). Formatted as a source numeric ID and target ID. Each directed edge indicates that email(s) were sent.

Download this data and use your tool of choice to partition the graph into your own communities. Play around with different algorithms and parameters until you find one that can show something interesting, which you can then describe in your writeup.

Then, write a writeup of what you find, answering (at least) the following questions:
* **Methods**: What tools did you use to partition the graphs? How did you prepare your data (if at all)? What algorithm did you choose? Why? How did this deal with a directed graph data?
* **Results**: What is the distribution (i.e., table or plot\*) of community sizes in the algorithm-communities vs. ground-truth-communities? Are there other statistics that characterize the two types of communities? Look at the 1-2 largest algorithm-communities vs. ground-truth-communities, what portion of the nodes overlap? 
* **Discussion**: Compare and contrast the community detection and the ground-truth communities. Are they capturing the same aspects of the network? Is this what you would expect, given where the data came from and the algorithm that you used?

\*For this assignment, you can submit a plot as a `.png` file or other format, as long as it shows up satisfactorily in Github, AND the overall size of ALL your supporting files is less than 1MB.


## Part 2: YouTube social network
The second network we will be using is a network of YouTube users. Users are able to form friendships with one individual, or groups with multiple individuals. Note that this network is significantly larger than the first, with over 1M nodes and almost 3M edges. Expect algorithms to be slower, more memory to be required, etc. This is one reason we started with a smaller network -- it's often better to start small and figure out what you're doing. (Note: If your computer is unable to handle the size of this network, consider switching to the [DBLP](http://snap.stanford.edu/data/com-DBLP.html) or [Amazon](http://snap.stanford.edu/data/com-Amazon.html) network and explain your choice.)
* [Class data](http://snap.stanford.edu/data/bigdata/communities/com-youtube.top5000.cmty.txt.gz). Each line contains the node IDs of members of the top 5000 communities -- no community IDs are specified. Again, these community IDs may be thought of as _ground-truth_ communities.
* [Edge data](http://snap.stanford.edu/data/bigdata/communities/com-youtube.ungraph.txt.gz). These are undirected edges between YouTube user IDs. It only contains edges between nodes in the largest connected component in the YouTube social network.

Again, download this data and use your tool of choice to partition the graph into your own communities. Play around with different algorithms and parameters until you find one that can show something interesting, which you can then describe in your writeup.

Again, write a writeup of what you find, answering (at least) the following questions:
* **Methods**: What tools did you use to partition the graphs? How did you prepare your data (if at all)? What algorithm did you choose? Why? _Also, did your methods differ from the Email-EU-core data, and if so why?_
* **Results**: What is the distribution (i.e., table or plot) of community sizes in the algorithm-communities vs. ground-truth-communities? Are there other statistics that characterize the two types of communities? Look at the 1-2 largest algorithm-communities vs. ground-truth-communities, what portion of the nodes overlap?
* **Discussion**: Compare and contrast the community detection and the ground-truth communities. Are they capturing the same aspects of the network? Is this what you would expect, given where the data came from and the algorithm that you used? _Also, how did the size of the network affect your choosing which results to write about and analyze?_


## What to submit
Submit a writeup in one `assignments/submission2.md` file. It should look something like this:
```
# Assignment 2: Detecting Communities
<yourname> <fathersname>


## Introduction
...

## Part 1: Email-EU-core network
### Methods
...
### Results
...
### Discussion
...

## Part 2: YouTube social network
### Methods
...
### Results
...
### Discussion
...

## Conclusion
```



## Acknowledgements
Data sets are from:
* Jure Leskovec and Andrej Krevl. SNAP Datasets: Stanford Large Network Dataset Collection, 2014. Accessible at: [http://snap.stanford.edu/data](http://snap.stanford.edu/data).
<!-- * J. Yang and J. Leskovec. Defining and Evaluating Network Communities based on Ground-truth. ICDM, 2012. -->
<!-- * Hao Yin, Austin R. Benson, Jure Leskovec, and David F. Gleich. "Local Higher-order Graph Clustering." In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2017. -->
<!-- * J. Leskovec, J. Kleinberg and C. Faloutsos. Graph Evolution: Densification and Shrinking Diameters. ACM Transactions on Knowledge Discovery from Data (ACM TKDD), 1(1), 2007. -->
<!-- The community detection algorithm is from: -->
<!-- * Blondel VD, Guillaume JL, Lambiotte R, Lefebvre E. Fast unfolding of communities in large networks. Journal of statistical mechanics: theory and experiment. 2008 Oct 9;2008(10):P10008. -->


## Due
Thursday, 12th April, 2018 @ 8:30am.

## Rubric: /100

* /10 Is there a full report with all sections?
* /10 Is the writing style clear and convincing?
* /40 Part 1: Email-EU-core
    * /8 Methods described adequately?
    * /8 Methods chosen intelligently?
    * /6 Results show community distribution statistics?
    * /4 Results show node overlap?
    * /8 Discussion really compares the 2 types of communities?
    * /6 Discussion brings up the data?
* /40 Part 2: YouTube
    * /5 Methods described adequately?
    * /5 Methods chosen intelligently?
    * /5 Results show community distribution statistics?
    * /5 Results show node overlap?
    * /5 Discussion really compares the 2 types of communities?
    * /5 Discussion brings up the data?
    * /10 Were differences from Part 1 described adequately?

**Comments**:


