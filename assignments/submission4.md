# Assignment 4: Networks Over Time
Natnael Getachew


## Introduction
In Assignment 4 we will need to explore and proof that "if bridges are better or less in email communication" as i got to explore snappy and panda i faced a lot more cahallenges so i moved to using Gephi and excell

### Methods
At first i tried to identify a bridge so used Excel filter in the All department list and also for dep 1
then after that filter out the bridge and cheack the time of email exchange



### Results
By looking at the filter range department one has a range of nodes from 0 to 319.so my plan to identify bridge was if a node is a bridge it will have less nodes localy within the department and more with the rest

As i move by trial and error at node 7 i foud that it has 4 links outside its department and few more within the department

Next is time exchange between the nodes so i took node 416,418,810 the nodes email exchange outside his department nodes and compared the result

| SRC| DES | TIME |
| --- | --- | -------- |
| 416 | 7 | 30373416 |
| 418 | 7 | 19767849 |
| 810 | 7 | 14292888 |

| SRC| DES | TIME |
| --- | --- | -------- |
| 7 | 416 | 30356021 |
| 7 | 418 | 8595198 |
| 7 | 810 | 14048140 |

### Discussion
As we can see in the result bridges are better at email communication since the interval is close

## Conclusion
Finally using one node to prove that a bridges are agoodcommunication is not enough but repeating this step for many local brdges will prove the case 

## Attribution
Our proffessor stephen Wu for pointing out on using Excel to proof the concept