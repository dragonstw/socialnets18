# CS 562/662: Natural Language Processing
*******************
Oregon Health & Science University

3 credits, Winter Term 2017

## Course Details

### Instructors
[**Stephen Wu**](https://sites.google.com/site/stephentzeinnwu/)
* Email: wst at ohsu dot edu
* Office: BICC 411, cube by Gaines Hall 30C

<!-- TA: Shiran Dudy -->
<!-- * Email: dudy at ohsu dot edu -->
<!-- * Office: cube by Gaines Hall 30C -->

### When & Where
Lecture:

* M 12:30 - 2:00pm | Gaines Hall 47
* W 12:30 - 2:00pm | Gaines Hall 47
* [Online recordings](http://cslu.ohsu.edu/multimedia) sometimes available -- see password

Office Hours:

* By appointment (contact via Slack message or e-mail)


### Course Description & Goals
CS 562/662 is an introduction to the field of Natural Language Processing (NLP).  By the end of this class, you will have the basic tools to design and/or implement a reasonable computational solution (though not necessarily optimal) to language tasks such as text normalization, part-of-speech tagging, parsing, and representing semantic meaning.
 
In the wide view, NLP can encompass the above tasks as well as a broader set of tasks, like automatic speech recognition, machine translation, information extraction, question answering, domain adaptation, and active learning.  In this introductory class, we will cover a set of core tasks with their key theoretical concepts and landmark algorithms, and sample a smaller number of applied domains and tasks.

The course will be taught in the [techied](bit.ly/techied) framework.

### Textbook
* Required: D. Jurafsky & J.H. Martin. 2008. Speech and language processing: An introduction to natural language processing, computational linguistics and speech recognition. 2nd edition. Upper Saddle River, NJ: Pearson Prentice Hall.

	- ISBN: 978-0131873216
	- Rent or purchase on Amazon or on bigwords.com
	- NB: The 1st edition differs considerably and chapter numbers will not match those used here.
    - Supplementary: Draft versions of the [3rd edition](https://web.stanford.edu/~jurafsky/slp3/)

* Optional: S. Bird, E. Klein, & E. Loper. 2009. Natural Language Processing with Python. 1st edition. Sebastopol, CA: O'Reilly Media.
	- ISBN: 978-0596516499



## Schedule and Assignments
 
| # | Date   | Topic | Reading | Materials | Lecture | Assign | Due |
|---|--------|-------------------------------------------|-----------------------------------------------|------------------------------------------------------------|----------------|---------|---------|
| 1 | 1/9/17 | Birds' eye view of NLP | J&M, chap. 1 | [notes] | Stephen Wu | HW0 |  |
| 2 | 1/11/17 | ML & Evaluation for NLP | Belz 2009<br/>Resnik & Lin 2010 |  | Stephen Wu | HW1 | HW0 |
|  | 1/16/17 | _MLK Day – no class_ |  |  | - |  |  |
| 3 | 1/18/17 | Pronunciation Modeling | Sproat et al. 2001 |  | Brian Roark |  |  |
| 4 | 1/23/17 | Text Normalization | J&M, chap. 11 |  | Steven Bedrick |  | HW1 |
| 5 | 1/25/17 | Tokens and Words | J&M, 19.1-19.3, 20.1-20.8 | [notes] Lexical Semantics & WSD<br/>[notes] Word Similarity | Meysam Asgari |  |  |
| 6 | 1/30/17 | Linear classifiers<br/>Word embeddings | Linear classifiers [ipynb]<br/>Mikolov et al. 2013 | [notes] Linear models/word embeddings | Stephen Wu | HW2 |  |
| 7 | 2/1/17 | Language models & NNs |  |  | Stephen Wu |  |  |
| 8 | 2/6/17 | Tagging and chunking, HMMs | J&M 5-6<br/>Marcus et al. 1993 | [notes] | Stephen Wu |  | HW2 |
| 9 | 2/8/17 | Context-free grammars & transforms | J&M 12J&M 16 | [notes] Syntax | Stephen Wu | HW3 |  |
| 10 | 2/13/17 | Constituency parsing I | J&M 13-14 | [notes] Parsing | Stephen Wu | Project |  |
| 11 | 2/15/17 | Constituency parsing II<br/>Dependency parsing | Petrov et al. 2006<br/>Nivre et al. 2007 | [notes] More Parsing | Stephen Wu |  | HW3 |
|  | 2/20/17 | _President's Day -- no class_ |  |  | - |  |  |
| 12 | 2/22/17 | Computational semantics I | J&M 17-18.3 | [notes] Meaning in Symbols | Stephen Wu |  | Proposal |
| 13 | 2/27/17 | Latent semantic analysis<br/>Topic modeling | Bellegarda 2005<br/>Blei 2012 | [notes] Distributional Semantics | Stephen Wu | HW4 |  |
| 14 | 3/6/17 | Computational semantics II<br/>Discourse | J&M 21, Bos 2008<br/>Banarescu et al 2012 | [notes] Semantics & Discourse | Stephen Wu |  |  |
| 15 | 3/8/17 | Information Extraction | J&M 22 | [notes] Information Extraction | Stephen Wu |  | HW4 |
| 16 | 3/13/17 | Text classification<br/>Sentiment analysis |  |  | Stephen Wu |  |  |
| 17 | 3/15/17 | **Project presentations** |  |  | - |  | Project |
| 18 | 3/20/17 | Machine translation | J&M 25 | [notes] Machine Translation | Stephen Wu |  |  |
| 19 | 3/22/17 | **Final Exam** |  |  | - |  |  |

## Communications
We're all about modern tools for technical education.  You should sign up for the _unofficial_ [**CSLU Slack group**](https://ohsu-cslu.slack.com/) (I'll send an invite).  Furthermore, this syllabus and all other class documentation and assignments will be available on the [**nlp17**](https://repo.cslu.ohsu.edu/stephenwu/nlp17) git repository.


## Course Policies
### Course Grade
* 40% Homework assignments
	* 10% each, 5 homework assignments (HW0-HW4); drop the lowest
* 20% Class project (9 days for proposal + 3 more weeks for final)
* 10% Final exam
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
 
 
### Programming environment
The homework assignments will be designed to work with the new, standardized [CSEE VirtualBox Environment](http://cslu.ohsu.edu/~kain/files/ubuntu.vdi.zip). Assignments should be done in Python 2.7 (note that the VirtualBox environment uses Python 3 for `python` by default). 

 
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
