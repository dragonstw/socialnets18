# Assignment0
***********
## Description

This code include two external modules that I install, this modules are **NLTK** and **Nilsimsa**.

- ** NLTK or Natural Language Toolkit ** is a suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language.

-  ** Nilsimsa ** is an anti-spam focused locality-sensitive hashing algorithm and the goal is to generate a hash digest of an email message such that the digests of two similar messages are similar to each other.

## Code Result
Please enter your full name: yohannes endale
a101023c14cc518510250a2004828880e02261084494125a15202d24000c20a4
-----------------------------
     0 endale
     0 yohannes
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
     0 endale
     0 yohannes
-----------------------------
Using Python version 2.7.14

Using nltk version 3.2.5

## Code Description
First the program will accept input from the user.
After accepting the input it will convert it to lower letter and split the words.
And then create empty list called ** name_frequency**.

we assigned the **defaultdict(int)** which holds all the words from nltk to **unigram_frequency**.
 
For word in the **nltk.corpus.brown** we start counting how frequently each word is used and store it on the variable called **unigram_frequency**.


For our input called **name_parts** we will check if its in the **unigram_frequency** or not. And if its not in the **nltk.corpus.brown** list we will set **unigram_frequency[name_part]** and **name_frequency[name_part]** equal to 0 meaning it will be added as new word with a key value of 0.

But if its in the **nltk.corpus.brown** we will set **name_frequency[name_part]** equal to **unigram_frequency[name_part]** meaning the word is in the list so no need to add it to the list.

Then we sort the list.

First it will print out the hexdigest() for our input called **name** using the module nilsimsa. it uses Nilsimsa to convert the string to hexadigits.

Then prints out the **name_parts** from the user input and frequency(key) of the word in the list.

Then it will display the top 20 most frequntly used words
and the least 20 most frequntly used words from the list.

Then displays the version of python and nltk from the function print_version_info().




