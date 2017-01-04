# CS 562/662: Natural Language Processing
*******************
Oregon Health & Science University
3 credits, Winter Term 2016

## Course Details

### Instructor
Stephen Wu (DMICE & CSLU)
Email: wst@ohsu.edu
Office: Gaines Hall 110 (M/W), BICC 411 (other)

### When & Where
Lecture:

* M 12:30 - 2:00pm | Gaines Hall 30C
* W 12:30 - 2:00pm | Gaines Hall 5

Office Hours:

* W 2:15-3:30pm | Gaines Hall 110 (or by appointment)

### Class Forum/Q&A/Announcements
You should sign up for Piazza for the class forum, announcements, recordings of the lectures, etc.

### Course Description & Goals
CS 562/662 is an introduction to the field of Natural Language Processing (NLP).  By the end of this class, you will have the basic tools to design and/or implement a reasonable computational solution (though not necessarily optimal) to language tasks such as text normalization, part-of-speech tagging, parsing, and representing semantic meaning.
 
In the wide view, NLP can encompass the above tasks as well as a broader set of tasks, like automatic speech recognition, machine translation, information extraction, question answering, domain adaptation, and active learning.  In this introductory class, we will cover a set of core tasks with their key theoretical concepts and landmark algorithms, and sample a smaller number of applied domains and tasks.

### Textbook
* Required: D. Jurafsky & J.H. Martin. 2008. Speech and language processing: An introduction to natural language processing, computational linguistics and speech recognition. 2nd edition. Upper Saddle River, NJ: Pearson Prentice Hall.

	- ISBN: 978-0131873216
	- Rent or purchase on Amazon or on bigwords.com
	- NB: The 1st edition differs considerably and chapter numbers will not match those used here.
 
* Optional: S. Bird, E. Klein, & E. Loper. 2009. Natural Language Processing with Python. 1st edition. Sebastopol, CA: O'Reilly Media.
	- ISBN: 978-0596516499

## Schedule and Assignments
 
| #  | Topics Covered                     | Date   | Assigned reading           | HW       | Notes from class                       |
|----|------------------------------------|--------|----------------------------|----------|----------------------------------------|
|    | Inclement weather – no class       | 4-Jan  |                            |          |                                        |
| 1  | Brief overview of NLP              | 6-Jan  | J&M, chap. 1               |          | [notes] Overview/Probability theory    |
|    | Probability theory review          |        |                            |          | [ipynb] Data struct. for probabilities |
| 2  | Text encoding                      | 11-Jan | Spolsky 2003               |          | [slides] Encodings [pdf]               |
|    | Tokenization                       |        | Gorman 2014                |          | [ipynb] Tokenization, sentence         |
|    | Sentence detection                 |        | (BKL, Ch 3)                |          |                                        |
| 3  | Text normalization                 | 13-Jan | Sproat et al. 2001         | HW0 due  | [slides] Text normalization [pdf]      |
|    | Stemming and lemmatization         |        |                            |          |                                        |
|    | MLK Day – no class                 | 18-Jan |                            |          |                                        |
| 4  | Lexical semantics                  | 20-Jan | J&M, 19.1-19.3, 20.1-20.5  |          | [notes] Lexical Semantics & WSD        |
|    | Word sense disambiguation          |        |                            |          |                                        |
|    | Computational phonology/           | SKIP   | J&M, chap. 11              |          |                                        |
|    | morphology                         |        | Kaplan & Kay 1994          |          |                                        |
| 5  | Word Similarity                    | 25-Jan | J&M 20.6-20.8              | HW 1 due | [notes] Word Similarity                |
| 6  | Linear classifiers for NLP         | 27-Jan | Linear classifiers [ipynb] |          | [notes] Linear models/word embeddings  |
|    | Word embeddings                    |        | Mikolov et al. 2013        |          |                                        |
| 7  | Tagging and chunking               | 1-Feb  | J&M 5-6                    |          | [notes] POS tagging, HMMs, Chunking    |
|    | HMMs                               |        | Marcus et al. 1993         |          |                                        |
| 8  | Context-free grammars              | 3-Feb  | J&M 12                     | HW 2 due | [notes] Syntax                         |
|    | Tree & grammar transforms          |        | J&M 16                     |          |                                        |
| 9  | Constituency parsing I             | 8-Feb  | J&M 13-14                  |          | [notes] Parsing                        |
| 10 | Constituency parsing II            | 10-Feb | Petrov et al.  2006        |          | [notes] More Parsing                   |
|    | Dependency parsing                 |        | de Marneffe et al. 2006    |          |                                        |
|    |                                    |        | Nivre et al. 2007          |          |                                        |
|    | President's Day -- no class        | 15-Feb |                            |          |                                        |
| 11 | Computational semantics I          | 17-Feb | J&M 17-18.3                | HW 3 due | [notes] Meaning in Symbols             |
| 12 | Latent semantic analysis           | 22-Feb | Bellegarda 2005            |          | [notes] Distributional Semantics       |
|    | Topic modeling                     |        | Blei 2012                  |          |                                        |
| 13 | Computational semantics II         | 24-Feb | J&M 21, Bos 2008           |          | [notes] Semantics & Discourse          |
|    | Discourse                          |        | Banarescu et al 2012       |          |                                        |
| 14 | Information Extraction             | 29-Feb | J&M 22                     |          | [notes] Information Extraction         |
| 15 | Text classification                | 2-Mar  |                            | HW 4 due |                                        |
|    | Sentiment analysis - no class      |        |                            |          |                                        |
| 16 | Machine translation                | 7-Mar  | J&M 25                     |          | [notes] Machine Translation            |
| 17 | Evaluation                         | 9-Mar  | Belz 2009                  |          | [notes] NLP Evaluation                 |
|    |                                    |        | Resnik & Lin 2010          |          |                                        |
| 18 | Applications: NLP in Clinical Text | 14-Mar |                            | HW 5 due | [notes] Clinical Text                  |
|    |                                    |        |                            |          | [notes] Stephen's research             |
 
* J&M = Jurafsky & Martin
* BKL = Bird, Klein, & Loper
* (...) = optional
* [...] = linked media resource
* [ipynb] resources can be viewed with nbviewer.ipython.org/url/<paste-ipynb-here>


## Course Policies
### Course Grade
* 60% Homework assignments
	* 12% each, 6 homework assignments, drop lowest score
* 15% Collegiality (peer reviews & providing resources for classmates)
* 15% Participation (attendance, class interaction, etc)
* 10% Final exam/project
 
Letter grades are given at 5-point intervals:
* A+       95-100
* A        90-95
* A-       85-90
* B+       80-85
* B        75-80
* B-       70-75
* C+       65-70
* C        60-65
* C-       55-60
* ...

### Homework Grades and Peer Review
A grading rubric will be posted along with each assignment, explicitly calling out several areas your assignment should address.  An effort is made for this grading to be balanced, gauging your effort, learning, and of course, competency.
 
For most homework assignments, 2 peers will review and grade your
homework, with your final grade for the assignment calculated
according to the following weighting:
* 60% instructor grade
* 20% peer reviewer 1 grade
* 20% peer reviewer 2 grade
 
You will contribute to the reviewing and scoring 2 peers' assignments, chosen randomly.


### Late Work
Homework is due electronically at 12:00pm on the listed assignment due date.  You are encouraged to contact the instructor if the work may be late for any reason.  Late penalties are assessed as follows:

-       No penalty if you submit on-time and make no changes (or very small bug fixes)
-       -10% if you submit on-time but make significant changes
-       -20% if you do not submit on time
-       No credit if you do not submit
 
The second option implies that there is, in fact, a second deadline for work: the peer review due date.   The peer reviews should be submitted by this date.  Revisions to your own submission (for a 10% late penalty, as described above) may be made before this date; these revisions may or may not be seen by your peer reviewers, but will be seen by the instructor.


### Group Work, Attribution, and Plagiarism
Group work and learning from peers on the homework assignments is encouraged.  Frequently, you will find that you accelerate your learning when you learn from peers, and you internalize concepts when you teach them to peers. If you are making "substantial revisions" to an assignment (for a 10% penalty) between the assignment due date and the peer review due date, this includes being able to consider other students' solutions.  You are encouraged to learn from each other, and from the web, and even try out others' code.  
 
However, every sentence and line of code that you turn in, you must understand and type yourself — no cut and paste.  Thus, when doing group work, you should not use anything directly from the meeting, e.g., notes, scrollback in an interactive Python session, cut-and-pasting a chat session.  Everything (code and explanations) should be internalized and re-typed/produced for the actual assignment.
 
If, in the end, you are essentially using someone else's code/idea (even having retyped it), you must give attribution to the source.  Specifically, you need to describe, in code comments and in your description of approach:

1.     Where it came from.  Be as specific as including a link to the original code, if one is available, or some other unique identification.
2.     What else you tried, and why you used the instead. (Please call attention to this in the description of your appraoch.)
3.      A detailed description of how the code works.
 
Example:

    """
    Adapted from L46-52 of http://bit.ly/xxxxxxxx by Person A
    do_something() solves problem X by ...
    ... the inner loop does Y...
    ...
    """
 
If others have given attribution to your work in their own assignment, this is typically a demonstration that you have spent good time and effort making your work clear and correct.  Your grade for that particular assignment will not increase and theirs will not decrease (beyond that stipulated by the late policy); however, your sharing of knowledge in this form will contribute positively to your collegiality score in the class (i.e., the 10% of your final grade that is concerned with quality of peer reviews, etc).
 
If you utilize others' work without understanding it or without attribution, this will constitute plagiarism and will be dealt with according to OHSU's academic dishonesty policies.  Plagiarism is a serious offense, with potential ramifications as serious as dismissal from a degree-seeking program.
 
With your code and/or the reference implementation, please DO NOT POST PUBLICLY and DO NOT SHARE WITH FUTURE CLASSES. Instead, if the opportunity presents itself, give collegial feedback and guidance.

## Attendance & Participation
Physical attendance at lectures is expected.  However, you can miss 2 days for any reason with no consequence to your participation grade.  Please discuss any extenuating circumstances with the instructor.
 
    Missed classes:   _______________________     __________________________
 
During lectures, we will learn through groups and a variety of active learning techniques.  Participation in these activities is part of your grade.

## OHSU Grade Submission Policy
Graduate Studies in the OHSU School of Medicine is committed to providing grades to students in a timely manner. Course instructors will provide students with information in writing at the beginning of each course that describes the grading policies and procedures including but not limited to evaluation criteria, expected time needed to grade individual student examinations and type of feedback they will provide. Class grades are due to the Registrar by the Friday following the week of finals. 

## Students with Disabilities
Our program is committed to all students achieving their potential. If you have a disability or think you may have a disability (physical, learning, hearing, vision, psychological) which may need a reasonable accommodation please contact Student Access at (503) 494-0082 or e-mail at orchards@ohsu.edu to discuss your needs. You can also find more information at [www.ohsu.edu/student-access](www.ohsu.edu/student-access). Because accommodations can take time to implement, it is important to have this discussion as soon as possible. All information regarding a student’s disability is kept in accordance with relevant state and federal laws.

## Acknowledgments
Many thanks to Kyle Gorman (now at Google) and Steven Bedrick (CSLU faculty) for their efforts on previous versions of this class.
