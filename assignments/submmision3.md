Name Daniel Bedore
Introduction
 In this lab I went through simulation of random network using modeling tool called Net logo and could understand it to some extent. This lab assignment has three parts like small world, segregation and giant component and using the tool which I mentioned earlier experiment Watts-Strogatz model of the small-worlds, Schelling model of geographic segregation and  giant component phenomenon.
In your own words, explain the `rewire-one` procedure and what it does, line by line. Also describe what rewiring means in the context of the network.
Part I
METHOD
first open the sample model and go through the re-wiring procedure. In re-wiring.
In the r-wire-one procedure what happen is it randomly select node in the network and make connection between them and in network context view rewiring means just assume there are node in network connected and when we re-wire it select nodes and make new wire between the nodes in the network.
RESULT 
result 
cc = o.5
ap length=6.63 this is before doing any re-wiring of either re-wire-one or re-wire-all.
after doing many times re-wire-one and re-wire-all the result is as follows 
for re-wire-one 
cc=0.03
apl=2.89
for re-wire-all
cc=0.059
apl=2.89
DISCUSSION
The clustering-coefficient as its name indicate connected components in the network so, it does change when re-wiring done to the network since re-wiring done nodes randomly selected.                                  
re-wiring nodes in the network means randomly connecting nodes available in this random network
so,re-wering occure therefore the cc value fluctuate since new connections are happening between
the nodes in the network.
the plot of shape is the way they are because  of re-wiring technique of the network. 
To calculate Diameter I wrote code that can calculate diameter in network and print result of it.the code I used is the following

to Diameter
  set Diamete[max distance-from-other-turtles] of turtles
end

PART II
method
in segregation as the similarity percentage increase in agiven 
desity percentag and percetage of similar wanted,the number of unhappy go to number zero.
result
in the result when desity and similarty percentag is 70 and 50 respectiviliy at begining of 
time zero 
%similarity is 49.8
#agent is 2290
number of unhappy is 966
and % unhappy is 42.18
but as time pass this initial pecentage and number changes.
at last time the result of all will be as fillow 
#agent is 2290 not changed 
%similarity is 88.26 increase
but both number and percentage of unhappy goes to or equals zero. 
discussion
finding similarity in the desity and wanted similarity the output is not to just extent or 
expectation that wanted the similarty shoud be that here in the output it icrease similarty 
percentage much than expected.

PART III
method 
in random network phenomenon the giant component formed by random selection of nodes and connecting them by edge.when we repeatedly do this then at last the reacheability of every nodes in the netwok will be easy and short since each nodes are connected each other nodes in network. 
result
in the section,when ever the nomber of nodes connecting each other either two or more than this the fraction in giant component increase and size of giant component increase at same time while increasing connection per nodes.
discusstion
in the network when randomly selected nodes connect each other and continuing this to the end of each connection pair,the this random network will result agiant component.

conclusion
this lab has three part and each of them are as follow small world,segregation and giant component in the network.working this lab
help me kmow each of them to the extent I can make them of.

