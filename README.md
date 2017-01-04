# CS 555/655: Analyzing Sequences
*******************
Oregon Health & Science University

3 credits, Fall Term 2016

## Course Details

### Instructors
[**Stephen Wu**](https://sites.google.com/site/stephentzeinnwu/)
* Email: wst at ohsu dot edu
* Office: BICC 411, cube by Gaines Hall 30C

[**Meysam Asgari**](http://cslu.ohsu.edu/~asgari/)
* Email: asgari at ohsu dot edu
* Office: Gaines Hall room 17

TA: Shiran Dudy
* Email: dudy at ohsu dot edu
* Office: cube by Gaines Hall 30C

### When & Where
Lecture:

* M 4:00 - 5:30pm | Gaines Hall 47
* W 4:00 - 5:30pm | Gaines Hall 47
* [Online recordings](http://cslu.ohsu.edu/multimedia) sometimes available -- see password

Office Hours:

* By appointment (contact via Slack message or e-mail)


### Course Description & Goals
Many types of data occur sequentially. A conversation between two people can be thought of as a sequence of speech turns; a written sentence can be thought of as a sequence of words and punctuation symbols; electronic text can be thought of as a sequence of characters; a spoken sentence can be thought of as a sequence of speech sounds. Time-series data (weather observations, stock tickers, etc.) is inherently sequential, and, of course, molecular biology is replete with examples of sequential data (sequences of nucleotide bases in DNA and RNA, amino acids in protein strands, etc.).

This course will concern itself with methods for analyzing these kinds of data, with a particular emphasis on sequences derived from linguistic data.  Topics will include:

* Applications of finite state automata, in particular with regards to language modeling;
* Discrete and continuous Hidden Markov Models;
* Gaussian Mixture Models & the Expectation-Maxmization algorithm;
* Suffix Arrays & Trees/Tries;
* Sequence alignment & matching.

The course will be taught in the [techied](bit.ly/techied) framework.

### Textbook
* Required: D. Jurafsky & J.H. Martin. 2008. Speech and language processing: An introduction to natural language processing, computational linguistics and speech recognition. 2nd edition. Upper Saddle River, NJ: Pearson Prentice Hall.

	- ISBN: 978-0131873216
	- Rent or purchase on Amazon or on bigwords.com
	- NB: The 1st edition differs considerably and chapter numbers will not match those used here.
 
* Optional: D. Gusfield. 1997. Algorithms on Strings, Trees, and Sequences. Cambridge University Press.
	- ISBN: 978-0521585194

## Schedule and Assignments
 
|      |     Date | Topic    | Reading                                                               | HW                                | Lecture                                    |
|------|----------|-----------------------------------------------------------------------|-----------------------------------|--------------------------------------------|---------|
| 1    | 9/28/16  | [Introduction](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/00_intro.pdf)          |                                   | [HW0 - Course setup](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/hw/hw0.md)                         | Stephen |
| 2    | 10/3/16  | [Regular Expressions & FSAs](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/01_regex.pdf)  | J&M Chap. 2                       | HW0 Due                                    | Stephen |
| 3    | 10/5/16  | [FSTs, part 1](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/02_fst.pdf)                                                          | [Sproat & Roark 2007, Chap. 1](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/roark_sproat_2007-ch1.pdf)                             |                                        | Stephen |
| 4    | 10/10/16 | [FSTs, part 2](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/03_wfst.pdf)           |          | [HW1 - FSTs](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/hw/hw1.md) | Stephen |
| 5    | 10/12/16 | [LMs](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/04_lm.pdf)                      | J&M 4                             |                                            | Stephen |
| 6    | 10/17/16 | [LMs & Smoothing](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/05_smoothing.pdf)   |                                   |                                     | Stephen |
| 7    | 10/19/16 | [String Similarity](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/06_simdist.pdf)   |                                   | HW1 Due                               | Stephen |
| 8    | 10/24/16 | [Markov Models](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/07_markov.pdf)                                                           |                                   |                                            | Meysam  |
| 9    | 10/26/16 | [HMMs and VQ] (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/08_hmm.pdf)                                                 |               |             | Meysam  |
| 10   | 10/31/16 | [GMMs and Viterbi Algorithm](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/09_viterbi.pdf)                                                           |                                   |          [HW2 - Implement a Viterbi Algorithm] (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/hw/hw2.md)                                    | Meysam  |
| 11   | 11/2/16  | [ML estimation] (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/10_EM1.pdf)                                                        |                                   |                         | Meysam  |
| 12   | 11/7/16  |  [EM algorithm]    (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/11_EM2.pdf)                           |                                   |                                           | Meysam |
| 13   | 11/9/16  | [HMM training (I)] (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/12_HMM1.pdf)                                                               |                                   | HW2 Due                                    | Meysam  | HW2 Due 
| 14   | 11/14/16 | [HMM training (II)]  (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/13_HMM2.pdf)                                                          |                                   | HW3  - [implement a Baum-Welch algorithm] (https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/hw/hw3.md)                                       | Meysam  |
| 15   | 11/16/16 | **Midterm Exam**                                                      |                                   |                                            | Meysam  |
| 16   | 11/21/16 | [String Matching - Preprocessing](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/14_preprocess.pdf)                                         | [Gusfield Ch. 1](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/gusfield_chap_1_2.pdf) |                                            | Stephen |
| 17   | 11/23/16 | [Exact String Matching](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/15_exact.pdf)                                         | [Gusfield Ch. 2](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/gusfield_chap_1_2.pdf) & [3.4](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/gusfield_chap_3.pdf)                   |                                           | Stephen |
| 18   | 11/28/16 | [Approximate String Matching](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/16_approximate.pdf) | [Gusfield Ch. 12](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/gusfield_chap_12.pdf)       | HW3 Reassign                      | Stephen |
| 19   | 11/30/16 | [HMM String Alignment](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/17_hmmalign.pdf)                                                      |                                   |                                            | Stephen |
| 20   | 12/5/16  | [Tries & Levenshtein Automata](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/18_tries.pdf)                                                 |                                   | HW3 Due                                    | Stephen |
| 21   | 12/7/16  | [Suffix Trees](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/resources/share/19_suffixtrees.pdf)                                                    | Add'l Reading                     | [HW4 - String Matching](https://repo.cslu.ohsu.edu/stephenwu/seqf16/blob/master/hw/hw4.md)                                   | Stephen |
| 22   | 12/12/16 | Intro to Information Theory                                        | Add'l Reading                     |                                            | Stephen, Shiran |
| 23   | 12/14/16 | Conditional Random Fields                |                                   | HW4 Due                                    | Stephen |

## Communications
We're all about modern tools for technical education.  You should sign up for the _unofficial_ [**CSLU Slack group**](https://ohsu-cslu.slack.com/) (I'll send an invite).  Furthermore, this syllabus and all other class documentation and assignments will be available on the [**seqf16**](https://repo.cslu.ohsu.edu/stephenwu/seqf16) git repository.


## Course Policies
### Course Grade
* 60% Homework assignments
	* 12% each, 5 homework assignments (HW0-HW4)
* 20% Midterm
* 10% Collegiality (peer reviews, providing resources for classmates)
* 10% Participation (attendance, class interaction, etc)
 
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


### Attendance & Participation
Physical attendance at lectures is expected.  However, you can miss 2 days for any reason with no consequence to your participation grade.  Please discuss any extenuating circumstances with the instructor.
 
    Missed classes:   _______________________     __________________________
 
During lectures, we will learn through groups and a variety of active learning techniques.  Participation in these activities is part of your grade.


### Homework Grades and Peer Review
Homework is due electronically at the beginning of class (4:00pm) on the listed assignment due date.  

A grading rubric will be posted along with each assignment, explicitly calling out several areas your assignment should address.  An effort is made for this grading to be balanced, gauging your effort, learning, and of course, competency.

For most homework assignments, 2 peers will review and grade your
homework, with your final grade for the assignment calculated
according to the following weighting:
* 25% peer reviewer 1 grade (on due date)
* 25% peer reviewer 2 grade (on due date)
* 50% instructor/TA grade (on due date + 48 hours)

You will contribute to the reviewing and scoring of 2 peers' assignments, chosen randomly and anonymized.
These peer reviews are **due 48 hours after** the original due date/time. They will reflect what was submitted by the due date.

Revisions to your submission may be made during the 48-hour review period; these
will be seen by the instructor and reflected in the 50% instructor/TA grade.
Thus, it is possible to improve your score after the due date, but impossible to
get a perfect score without doing the work ahead of time.


### Late Work
You will receive only 25% credit for late work (judged on the due date, not the
peer review date); this will throw off peer review schedules.  Given the grading
structure, it makes more sense to turn in what you have at the due date, then
continue editing until the 48-hour peer review deadline.

You are encouraged to contact the instructor if there is an
extenuating circumstance and you know the work may be late.  
 
 
### Programming languages
You may use either Python, Matlab, or Octave for your programming assignments.  However, some of the assignments are primarily designed for just one language.

 
### Group Work, Attribution, and Plagiarism
Group work and learning from peers on the homework assignments is encouraged.  Frequently, you will find that you accelerate your learning when you learn from peers, and you internalize concepts when you teach them to peers.  Helping your peers is part of your "Collaboration" grade -- the proper place to do this is in the private "seqf16" Slack group, so that we can give you credit for helping each other out.

How does this work with the academic honesty policy?  On any graded assignment: every sentence or equation you write, every line of code that you turn in, you must understand and produce yourself — no cut and paste.  Thus, when doing group work, you should not use anything directly from the meeting, e.g., notes, scrollback in an interactive Python session, cut-and-pasting a chat session.  Everything (code and explanations) should be internalized and re-typed/produced for the actual assignment.

If you are essentially using someone else's idea (even having internalized and retyped/rewritten it), you must give attribution to the source (where it came from) and fully/explicitly describe it in words.

If you utilize others' work without understanding it or without attribution, this will constitute plagiarism and will be dealt with according to OHSU's academic dishonesty policies.  Plagiarism is a serious offense, with potential ramifications as serious as dismissal from a degree-seeking program.

### Academic Honesty
Course participants are expected to maintain academic honesty in their course work. Participants should refrain from seeking past published solutions to any assignments. Literature and resources (including Internet resources) employed in fulfilling assignments must be cited. See [here](http://www.ohsu.edu/xd/education/library/research-assistance/plagiarism.cfm?WT_rank=1#) for information on code of conduct for OHSU and
[here](http://www.ohsu.edu/xd/education/teaching-and-learning-center/for-students/index.cfm) for more information on citing sources and recognizing plagiarism.


## OHSU Policies
### OHSU Grade Submission Policy
Graduate Studies in the OHSU School of Medicine is committed to providing grades to students in a timely manner. Course instructors will provide students with information in writing at the beginning of each course that describes the grading policies and procedures including but not limited to evaluation criteria, expected time needed to grade individual student examinations and type of feedback they will provide. Class grades are due to the Registrar by the Friday following the week of finals. 

### SYLLABUS CHANGES AND RETENTION
This syllabus is not to be considered a contract between the student and the School of Medicine.  It is recognized that changes may be made as the need arises. Students are responsible for keeping a copy of the course syllabus for their records.

### SYLLABUS STATEMENT REGARDING DISABILITY SERVICES
OHSU is committed to providing equal access to qualified students who experience a disability in compliance with Section 504 of the Rehabilitation Act of 1973, the Americans with Disabilities Act (ADA) of 1990, and the ADA Amendments Act (ADA-AA) of 2008.  If you have a disability or think you may have a disability (physical, sensory, chronic health, psychological or learning) please contact the Office for Student Access at (503) 494-0082 or studentaccess@ohsu.edu to discuss eligibility for academic accommodations.  Information is also available at [www.ohsu.edu/student-access](www.ohsu.edu/student-access).  Because accommodations may take time to implement and cannot be applied retroactively, it is important to have this discussion as soon as possible.  All information regarding a student’s disability is kept in accordance with relevant state and federal laws.

### COMMITMENT TO EQUITY AND INCLUSION
Oregon Health & Science University is committed to creating and fostering a learning and working environment based on open communication and mutual respect. If you encounter sexual harassment, sexual misconduct, sexual assault, or discrimination based on race, color, religion, age, national origin or ancestry, veteran or military status, sex, marital status, pregnancy or parenting status, sexual orientation, gender identity, disability  or any other protected status please contact the Affirmative Action and Equal Opportunity Department at 503-494-5148 or aaeo@ohsu.edu. Inquiries about Title IX compliance or sex/gender discrimination and harassment may be directed to the OHSU Title IX Coordinator at 503-494-0258 or titleix@ohsu.edu

### INCLEMENT WEATHER POLICY
When the weather forecaster is calling for ice or snow, call the OHSU Alert Line, 503 494-9021, for information regarding weather conditions that may affect operations at OHSU. This hot line will offer specific recorded messages for road conditions on OHSU's Marquam Hill and West campuses (option 1), and for patients (option 2), students (option 3) and employees (option 4).

If extreme weather conditions present potentially unsafe situations, the provost of the university may choose to delay or cancel classes, or alter office and research activities. If classes are canceled or delayed, residents and students who have patient care responsibilities must meet those obligations.

For more information, please view [this website](http://www.ohsu.edu/xd/about/visiting/weather/index.cfm) or call the above hotline.
