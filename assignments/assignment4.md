# Assignment 4: Networks Over Time
We've described networks that are static in terms of node attributes, context of network structure, and communities. In this lab, we get a chance to look at a network and how it evolves over time.

Treat this assignment like a project -- you will have more time to complete it (2 1/2 weeks + 2 lab periods), and you will be somewhat self-directed.

There are some simple statistics that you can calculate in Steps 2 and 3, but these are a minor part of the assignment. The **MAIN QUESTION** that you should try to answer is this:

* _A "bridge" person in an organization connects many different people. Are "bridge" people more efficient or less efficient at email communication?_

Note that the grading of this assignment will be similar to a written research paper -- see below for the criteria.


## Step 1: Familiarize yourself with a new library: `Snap.py` or `pandas` (Suggested)
While this assignment is completable using tools that we've previously explored elsewhere in this class, I recommend you use `snap.py` (pronounced "snappy") or `pandas`.

**Option 1**: First, install the SNAP Python library (`Snap.py`). Get familiar with the tools with some of [the documentation](http://snap.stanford.edu/snappy/index.html); make sure you can load it up in a Python 2 environment. I recommend using a [jupyter notebook](http://jupyter.org), so that you can visualize the results of your calculations inline, but don't let this distract you from learning the `Snap.py` library.

**Option 2**: Use the `pandas` library, a statistical package available at [???](). This is not exactly tuned for network operations, but you should be able to complete the assignment using the tools provided. You'll have to implement some of the typical graph functions.

**Option 3**: You can still use Gephi and Excel or similar, you'll just have to switch between programs and know what you're doing.


## Step 2: Community Detection (Suggested)
As in our previous assignment, run a Community Detection algorithm on the full graph. (Note that many students in Assignment 2 erroneously used the _ground-truth_ graph instead of combining with the actual graph of edges.) Record which community each node is in.


## Step 3: Simple statistics (Suggested)
Download [the temporal version of the email network](http://snap.stanford.edu/data/email-Eu-core-temporal.html) that we looked at in Assignment 3. This has the time (in seconds) from the first email connection in the temporal network. Whether using `Snap.py` or another tool to look at:

* How many components are present (don't count isolates)?
* What is the clustering coefficient of the graph? What are the clustering coefficients within communities?
* Consider the amount of time between a new edge forming _anywhere_ in the network. In particular, consider each edge's creation to be an event. What is the time between each event? (The format of the text file is not sorted for this purpose when you get it. There should be no negative numbers.) **Plot the distribution** and include a _.png_ file. In your plot, consider using a log-scale x-axis (i.e., take the log)
* What is the mean and standard deviation of time for a new edge to form?
* Do these differ significantly between the communities that you have discovered?


## Step 4: Temporal Analysis
Take 3 snapshots of the network, e.g., starting at time 12,096,000 (20 weeks), then at time 18,144,000 (30 weeks), then at time 24,192,000 (40 weeks). One way to do this is to create 3 separate graphs which only have edges created before these timestamps.

It is now your job to answer the one question posed in the introduction. Namely:
* _A "bridge" person in an organization connects many different people. Are "bridge" people more efficient or less efficient at email communication?_

Good luck!



## What to submit
Submit a writeup in one `assignments/submission4.md` file. PLEASE EXPORT YOUR IMAGES AT 320x320 OR SIMILAR, STAYING UNDER 1MB, AND CHECK WHETHER THEY ARE LINKED CORRECTLY ON GITHUB.

The writeup should look something like this -- don't split up by Steps:
```
# Assignment 4: Networks over time
<yourname> <fathersname>


## Introduction
...

## Methods
...

## Results
...

## Discussion
...

## Conclusion
```



## Acknowledgements
Data set is from:
* Jure Leskovec and Andrej Krevl. SNAP Datasets: Stanford Large Network Dataset Collection, 2014. Accessible at: [http://snap.stanford.edu/data](http://snap.stanford.edu/data).


## Due
Monday, 28th May, 2018 @ 1:30pm.

## Rubric: /100

* /20 Originality: How original is the approach or problem explored? You can score high for originality even if the results don't show anything.
* /20 Clarity: Is it clear what was done, what the results were, what the conclusions were?
* /20 Substance: Was enough work done? Does it say something meaningful? Is there a full report where all the work is described?
* /20 Correctness: Is the technical approach sound and well-chosen? Can you trust the claims of the paper?
* /20 Attribution: Was related/others' work properly attributed?

**Comments**:


