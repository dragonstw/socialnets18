# This is the assignment submission of Mekre Abate


#Start of program Output
-------------------------------
Please enter your full name: Mekre Abate
8120412000000005e020a3000416600544813c9153000300041002404d4e0200
-----------------------------
     0 abate
     0 mekre
-----------------------------

 69971 the
 58334 ,
 49346 .
 36412 of
 28853 and
 26158 to
 23195 a
 21337 in
 10594 that
 10109 is
  9815 was
  9548 he
  9489 for
  8837 ``
  8789 ''
  8760 it
  7289 with
  7253 as
  6996 his
  6741 on
     .
     .
     .
     1 no-driving
     1 buffs
     1 carbohydrate
     1 prodigall
     1 bombarding
     1 cut-to-a-familiar-pattern
     1 roars
     1 decorous
     1 1911-1912
     1 xenon
     1 digressions
     1 4.21
     1 dollarette
     1 fusty
     1 pigen
     1 mosaics
     1 northerly
     1 jawbone
     0 abate
     0 mekre

Using Python version 2.7.14
Using nltk version 3.2.5



#End of program Output
-------------------------------
## Description about the program

### The program first displays the input in hex, then the program copies each individual word in the brown library, which contains a million words, to a python library structure created by the "defaultdict" function. This dictionary has a property of adding new words to its collection when words that aren't in it are searched in it. This structure will have a key-value pair. The key being the word and the value being the frequency of that word in that library.

### Each word(split by blank space) that was inserted into the program by the user will be matched against the library created. If there are any matches, the word will be added to another list as is(keeping the key-value structure). If there are no matches the words will be added to a list and to the dictionary created with their value initialized to zero.


### After every word that has been inserted into the program has been checked, the list created will be displayed.
### After that the dictionary created in the program will display its elements in descending order based on frequency. It will display the 20 words with the highest frequency followed by the last 20 words with the lowest frequency
### The program will finalize by displaying the python and nltk version currently installed on a computer running the test_setup script.
