# ITSC-5C22: Social Network Analysis
******************* 

Addis Ababa Institute of Technology

Spring Semester 2018

## Course Details

### Instructors
[**Stephen Wu**](https://sites.google.com/site/stephentzeinnwu/)
* Email: wu dot stephen dot t at gmail dot com
* LinkedIn: [stephentzeinnwu](http://linkedin.com/in/stephentzeinnwu)
* Office: PB103 Pharmacy Campus
<!-- * Twitter: @just\_stw\_it -->

Hat tip to Dr. Venkateswarlu Sunkari, who taught a previous version of this course at AAIT.

### When & Where
* M 8:00 - 10:00am | Lecture NB111 | (Originally T 8:00 - 10:00am)
* Th 8:30 - 12:30pm | Lab NB111

Office Hours:
* By appointment (contact via [Slack message](https://aaititsc.slack.com/messages) or e-mail)


### Course Description & Goals
This course will use social network analysis; both its theory and computational tools, to make sense of the social and information networks that have been fueled and rendered accessible by the internet.

Everything is connected: people, information, events and places, all the more so with the advent of online social media. A practical way of making sense of the tangle of connections is to analyze them as networks. In this course you will learn about the structure and evolution of networks, drawing on knowledge from disciplines as diverse as sociology, mathematics, computer science, economics, and physics. Online interactive demonstrations and hands-on analysis of real-world data sets will focus on a range of tasks: from identifying important nodes in the network, to detecting communities, to tracing information diffusion and opinion formation.

The course structure is based on the [techied](http://bit.ly/techied) framework.

### Textbook & Tools
* Required: D. Easley, J. Kleinberg. [Networks, Crowds, and Markets: Reasoning About a Highly Connected World](http://www.cs.cornell.edu/home/kleinber/networks-book). Cambridge University Press, 2010. 
    - The whole book is available online.
    - Referred to in the schedule below as E&K
* Optional: M. O. Jackson, [Social and Economic Networks.](https://www.stanford.edu/~jacksonm/netbook.pdf). Princeton University Press, 2008.
    - This is a bit more technical than E&K, containing lots of good math definitions
    - Referred to in the schedule below as MOJ
* [Gephi](http://gephi.org/) is a tool for visualizing and manipulating graphs that we will use in our assignments.
* [NetLogo](http://www.ladamic.com/netlearn) is a tool that can be used for modeling & simulating networks.


## Schedule and Assignments
The following dates are holidays or the classes are cancelled for other reasons:
* 5th Apr
* 9th Apr
* 17 May
* 21 May
* 14 June

| # | Topic | Concepts | Reading | Activity | Materials | Notes |
| --- | --- | -------- | ------- | -------- | --------- | ----- |
| 1 | Networks: What and Why? | nodes, edges, adjacency matrix | E&K 1-2.1 | [0:Setup](assignments/assignment0.md) | [slides](resources/01_Introduction.pptx) | Discuss this Syllabus |
| 2 | Graph Theory | connected components, node degree, paths, diameter, breadth-first search | E&K 2.1-2.4 | [0:Setup](assignments/assignment0.md) | [slides](resources/02_GraphTheory.pptx) |  |
| 3 | Network Structure | giant component, cliques, bridges, local bridges, triadic closure, strong and weak ties | E&K 3.1-3.5 | [1:Facebook](assignments/assignment1.md) Download, visualize, calculate metrics | [slides a](resources/03_NetworkStructure.pptx), [slides b](resources/03b_NodeLevelMetrics.pptx) | Assignment 1 due 29th Mar |
| 4 | Communities | clustering, community structure, modularity | E&K 3.6, MOJ 13.2 | [2:Community detection](assignments/assignment2.md) <br> in real-life networks | [slides](resources/04_Communities.pptx) |  |
| 5 | Community Detection | hierarchical clustering, stochastic block models  | MOJ 13.2 | | [slides](resources/05_CommunityDetection.pptx) | Assignment 2 due 12th Apr |
| 6 | Random Network Models | probability review, binomial distribution, Poisson (Erdos-Renyi) | MOJ 1.2.3, 4; E&K 20.1-20.2 | [3:Random Networks in NetLogo](assignments/assignment3.md) | [slides](resources/06_RandomGraphs.pptx) |  |
| - | **_Midterm_** |  |  |  | [Review slides](resources/MidtermReview.pptx) | Exam on 26th April |
| 7 | Homophily & Affiliation | homophily, selection, social influence, affiliation, focal closure, membership closure, Schelling model | E&K 4.1-4.6 |  | [slides](resources/notavailable.md) |  |
| 8 | Small worlds, optimization, formation, search | small worlds, geographic networks, decentralized search |  | Detect small-world, simulate search | [slides](resources/notavailable.md) |  |
| 9 | Contagion, opinion formation, coordination, and cooperation | simple contagion, threshold models, opinion formation |  | Simulate impact of network structure | [slides](resources/notavailable.md) |  |
| 10 | Ethics in Social Network Analysis |  |  |  |
| 11 | Applications of Social Network Analysis | multiple applied domains |  | Explore domain-specific networks | [slides](resources/notavailable.md) |  |
| 12 | Online social networks | social media industry |  | Read recent SNA research | [slides](resources/notavailable.md) |  |
| - | **_Final_** |  |  |  |  |  |


## Communications
* You should sign up for the [**AAIT ITSC Slack group**](https://aaititsc.slack.com/) (I'll send an invite) for communication with the professor and with other students.
* Furthermore, this syllabus and all other class documentation and assignments will be available on the [**socialnets18**](https://github.com/dragonstw/socialnets18) git repository.


## Course Policies
### Course Grade
* 40% Lab Activities 
* 20% Midterm Exam & Quizzes
* 30% Final exam
* 10% Participation (attendance, interaction in class)

For assigned Lab Activities, two things should be mentioned:
* All assignments must be turned in by the due date. Students who leave _any one assignment_ unfinished at the end of the term will receive an `Fx` score for the whole course.
* You can drop one of your assignment grades (i.e., it will not count toward your final score).

Letter grades are given at 5-point intervals:
* A+       90-100
* A        83-90
* A-       80-83
* B+       75-80
* B        68-80
* B-       65-68
* C+       60-65
* C        50-60
* C-       45-50
* D	   40-45
* Fx	   30-40
* F	   0-30

A grading rubric will be posted along with each assignment (Lab Activity), explicitly calling out several areas your assignment should address.  An effort is made for this grading to be balanced, gauging your effort, learning, and of course, competency.

### Attendance & Participation
Physical attendance at lectures & labs is expected.  However, you can miss 3 days for any reason (e.g., sickness, death of a _friend's_ family member) with no consequence to your participation grade.  Please discuss any extenuating circumstances (e.g., death in _your_ family, severe illness or injury) with the instructor.
 
    Missed classes:  ____________   ____________   ____________ 

Additionally, when the instructor (Dr. Stephen) is late to class or cancels without advance notice, each student will gain an additional excused tardy or absence.

Beyond the excused absences, missing or being late to classes will incur some penalty on your Participation grade. (There are things in life that are more important than class; your grade will reflect the trade-off that you are taking when you skip class.)

During lectures & labs, we will learn through groups and a variety of active learning techniques.  Participation in these activities is also part of your grade (part of the 10%).  


### Late Work
You can submit a Lab Activity after the deadline and receive 75% of the credit.

You are encouraged to contact the instructor if there is an extenuating circumstance and you know the work may be late.  
 
 
### Group Work, Attribution, Plagiarism, and Academic Honesty
Group work and learning from peers on the homework assignments is encouraged.  Frequently, you will find that you accelerate your learning when you learn from peers, and you internalize concepts when you teach them to peers.  Helping your peers should be done in the private `socialnets18` Slack channel, so that we can give you credit for helping each other out.

How does this work with academic honesty and plagiarism?  On any graded assignment: every sentence or equation you write, every line of code that you turn in, you must understand and produce yourself — no cut and paste.  Thus, when doing group work, you should not use anything directly from the meeting, e.g., notes, scrollback in an interactive Python session, cut-and-pasting a chat session.  Everything (code and explanations) should be internalized and re-typed/produced for the actual assignment.

If you are essentially using someone else's idea (even having internalized and retyped/rewritten it), you must give attribution to the source (where it came from) and fully/explicitly describe it in words.

If you utilize others' work without understanding it or without attribution, this will constitute *plagiarism* and you will immediately receive an **Fx** grade for the course.  You may also be censured by the university, with potential ramifications such as suspension or dismissal from your program.

Course participants are expected to maintain academic honesty in their course work. Participants should refrain from seeking past published solutions to any assignments. Literature and resources (including Internet resources) employed in fulfilling assignments must be cited, or they will be considered plagiarism as well.

