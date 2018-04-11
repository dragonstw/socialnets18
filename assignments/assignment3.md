# Assignment 3: Random Networks with NetLogo

In this assignment, we'll get a feel for working on simulations with random networks. 

[NetLogo](https://ccl.northwestern.edu/netlogo/) is a modeling tool that makes this fairly intuitive (and it can be used for lots of other stuff too). Before doing the rest of this assignment, it's worth it to work through some of the [User Manual](https://ccl.northwestern.edu/netlogo/docs/) (or [pdf](https://ccl.northwestern.edu/netlogo/docs/NetLogo%20User%20Manual.pdf)): e.g., the Sample Model and Tutorials #1, #2, and #3.

As before, you'll submit an `assignments/submission3.md` file via your branch. Please name it and your `develop-<firstname><lastname>` branch correctly, and put it in the right directory. Again, you can submit a plot as a `.png` file or other format, as long as it shows up satisfactorily in Github, AND the overall size of ALL your supporting files is less than 1MB. Make sure your image links work in your `.md` file, _after_ pushing to the remote branch on GitHub.

Write a general **Introduction** discussing what you thought the main point of the assignment was, and what you learned from it.  The other portions will be Part-specific. We'll start with a more-guided exploration and move to less-guided.

## Part 1: Small Worlds
First, let's look at the classic Watts-Strogatz model of the small-worlds phenomenon. 
* Open a Small Worlds simulation. `File` -> `Models Library` -> `Sample Models` -> `Networks` -> `Small Worlds`
* Experiment with the model to get a feel for what is happening
* Add a `diameter` Monitor to the interface, and write the relevant code calculating the diameter of the graph.
* Plot the normalized diameter against the fraction of edges rewired and against the rewiring probability.

In your `assignments/submission3.md` file, write a **Methods** section, including:
1. What you did (and anything you needed to do accmplish the below portions)
2. In your own words, explain the `rewire-one` procedure and what it does, line by line. Also describe what rewiring means in the context of the network.
3. Include any important code snippets from NetLogo implementing the `diameter`. (Remember, you can open and close code blocks in your `submission3.md` file by putting 3 backticks \`\`\`.)

Answer the following questions in your **Results** section.
1. What are the clustering coefficient, average path length, and diameter at the beginning of a Watts-Strogatz model with 50 nodes?
2. Include images of the two plots after trying `rewire-one` and `rewire-all` many times. Be careful to explain what you're presenting in the text of your report.
3. Describe the overall shape of the plots.

Answer the following questions as part of your **Discussion** section.
1. Why does the clustering coefficient change as nodes are rewired?
2. Why does the `rewire-all` version show a distribution of metrics when you run the model with the same settings?
3. Why are the plots shaped the way they are?



## Part 2: Segregation
Next, let's take a look at the Schelling model of geographic segregation. Read about this model in Chapter 4.5 of [our class text book](http://www.cs.cornell.edu/home/kleinber/networks-book).

Open a Segregation simulation. `File` -> `Models Library` -> `Sample Models` -> `Social Science` -> `Segregation`.
Use a 150x150 grid and 88% density, similar to what's shown in the textbook.

Come up with Methods, Results, and Discussion that answer the following questions:
* What do you observe when you vary how tolerant an agent is of being in the minority? Does this match up with your expectations?
* Can you recreate the results from E&K 4.5? What do you learn from this? _Hint: Introduce a variable to place a limit on how many empty neighbors an agent can have._
* Is there anything else interesting that you notice about the model?


## Part 3: Giant Component
Finally, let's look at the phenomenon of giant components.

Open a Giant Component simulation. `File` -> `Models Library` -> `Sample Models` -> `Networks` -> `Giant Component`.

Observe how the model works with the default setup. Change at least one thing _in the code_, quote the code change, and show something interesting in your writeup.





## What to submit
Submit a writeup in a single `assignments/submission3.md` file. It should look something like this:
```
# Assignment 3: Detecting Communities
<yourname> <fathersname>


## Introduction
...

## Part 1: Small Worlds
### Methods
...
### Results
...
### Discussion
...

## Part 2: Segregation
### Methods
...
### Results
...
### Discussion
...

## Part 3: Giant Component
### Methods
...
### Results
...
### Discussion
...

## Conclusion
```


## Acknowledgements
Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.


## Due
Thursday, 26th April, 2018 @ 8:30am.

## Rubric: /100

* /10 Is there a full report with all sections?
* /10 Is the writing style clear and convincing?
* /36 Part 1: Small Worlds
    * /4 Methods: Description of work
    * /4 Methods: Explain `rewire-one` procedure
    * /4 Methods: `diameter` implementation
    * /4 Results: Initial metrics
    * /4 Results: Plots with unambiguous specification of numbers
    * /4 Results: Shape of the plots
    * /4 Discussion: Clustering coefficient changes explained
    * /4 Discussion: `rewire-all` distribution explained
    * /4 Discussion: Shape of the plots explained
* /24 Part 2: Segregation
    * /6 Answered how minority tolerance changes the result of the graph
    * /12 Successfully recreated E&K 4.5 results, and described
    * /6 Interesting points about the model, showing that you've explored
* /20 Part 3: Giant Component
    * /4 Observation of the simulation with default setup
    * /8 Meaningful code modification
    * /8 Report results & discuss results of code modification


**Comments**:


