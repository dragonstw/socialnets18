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
 
<table border=1>
 <tr>
  <td>
  <p><b
  style='mso-bidi-font-weight:normal'><span><o:p>&nbsp;</o:p></span></b></p>
  </td>
  <td>
  <p><b><span>Topics
  Covered<o:p></o:p></span></b></p>
  </td>
  <td>
  <p><b><span>Date<o:p></o:p></span></b></p>
  </td>
  <td>
  <p><b><span>Assigned
  reading<o:p></o:p></span></b></p>
  </td>
  <td>
  <p><b><span>HW<o:p></o:p></span></b></p>
  </td>
  <td>
  <p><b><span>Notes
  from class<o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><i style='mso-bidi-font-style:normal'><span>Inclement weather &#8211; no class<o:p></o:p></span></i></p>
  </td>
  <td>
  <p><span>1/4<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>1<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Brief overview of NLP<br>
  Probability theory review<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>1/6<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M, chap. 1<br><o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture1Notes.pdf">[<span>notes</span>] Overview/Probability theory</a><o:p></o:p></span></p>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/LectureNB1a.ipynb"
  title="ipython notebooks can be viewed with nbviewer.ipython.org/url/&lt;paste-url-here&gt;">[<span><span>ipynb</span></span>] Data <span>struct</span>.
  <span>for</span> probabilities</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>2<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Text encoding<br>
  Tokenization<o:p></o:p></span></p>
  <p><span>Sentence detection<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>1/11<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://www.joelonsoftware.com/articles/Unicode.html"><span><span>Spolsky</span></span><span> 2003</span></a><br>
  <a
  href="http://sonny.cslu.ohsu.edu/~gormanky/blog/understanding-text-encoding-in-python-2-and-python-3/"><span>Gorman 2014</span></a><o:p></o:p></span></p>
  <p><span>(BKL, <span>Ch</span> 3)<o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture2Slides.pptx">[<span>slides</span>] Encodings</a> [<a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture2Slides.pdf"><span>pdf</span></a>]<o:p></o:p></span></p>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/LectureNB2a.ipynb">[<span><span>ipynb</span></span>] Tokenization, sentence</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>3<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Text normalization<o:p></o:p></span></p>
  <p><span>Stemming and
  lemmatization<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>1/13<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://www.sciencedirect.com/science/article/pii/S088523080190169X"><span><span>Sproat</span></span><span> et al. 2001</span></a><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/hw/hw0.htm">HW0 due</a><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lecture/Lecture3Slides.pptx">[<span>slides</span>] Text normalization</a> [<a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture3Slides.pdf"><span>pdf</span></a>]<o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><i style='mso-bidi-font-style:normal'><span>MLK Day &#8211; no class<o:p></o:p></span></i></p>
  </td>
  <td>
  <p><span>1/18<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>4<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Lexical semantics<br>
  Word sense disambiguation<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>1/20<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M, 19.1-19.3,
  20.1-20.5<o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture4Notes.pdf">[<span>notes</span>] Lexical Semantics &amp; WSD</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td></td>
  <td>
  <p><i style='mso-bidi-font-style:normal'><span>Computational phonology/<br>
  morphology<o:p></o:p></span></i></p>
  </td>
  <td>
  <p><i
  style='mso-bidi-font-style:normal'><span>SKIP<o:p></o:p></span></i></p>
  </td>
  <td>
  <p><i style='mso-bidi-font-style:normal'><span>J&amp;M, chap. 11<br>
  <a href="http://www.anthology.aclweb.org/J/J94/J94-3001.pdf"><span>Kaplan &amp;
  Kay 1994</span></a><o:p></o:p></span></i></p>
  </td>
  <td>
  <p><i
  style='mso-bidi-font-style:normal'><span><o:p>&nbsp;</o:p></span></i></p>
  </td>
  <td></td>
 </tr>
 <tr>
  <td>
  <p><span>5<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Word Similarity<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>1/25<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 20.6-20.8<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a href="http://cslu.ohsu.edu/~wst/nlp-class/hw/hw1.htm">HW 1
  due</a><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture5Notes.pdf">[<span>notes</span>] Word Similarity</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>6<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Linear classifiers for NLP<o:p></o:p></span></p>
  <p><span>Word embeddings <o:p></o:p></span></p>
  </td>
  <td>
  <p><span>1/27<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://nbviewer.ipython.org/url/cslu.ohsu.edu/~gormanky/courses/CS662/Notebooks/CS-562-662-linear-classifiers-for-NLP.ipynb">Linear
  classifiers [<span>ipynb</span>]</a><o:p></o:p></span></p>
  <p><span><a
  href="http://www.aclweb.org/anthology/N13-1090"><span><span>Mikolov</span></span><span> et
  al. 2013</span></a><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture6Notes.pdf">[<span>notes</span>] Linear models/word embeddings</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>7<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Tagging and chunking<o:p></o:p></span></p>
  <p><span>HMMs<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/1<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 5-6<br>
  <a href="http://dl.acm.org/citation.cfm?id=972475"><span>Marcus
  et al. 1993</span></a><o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture7Notes.pdf">[<span>notes</span>] POS tagging, HMMs, Chunking</a></span><span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>8<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Context-free grammars<br>
  Tree &amp; grammar transforms<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/3<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 12<o:p></o:p></span></p>
  <p><span>J&amp;M 16<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/hw/hw2.htm">HW 2 due</a><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture8Notes.pdf">[<span>notes</span>] Syntax</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>9<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Constituency parsing I<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/8<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 13-14<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture9Notes.pdf">[<span>notes</span>] Parsing</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>10<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Constituency parsing II<o:p></o:p></span></p>
  <p><span>Dependency parsing<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/10<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://www.aclweb.org/old_anthology/P/P06/P06-1.pdf#page=473"><span>Petrov</span> et al.<span>&nbsp;
  </span>2006</a><o:p></o:p></span></p>
  <p><span><a
  href="http://nlp.stanford.edu/manning/papers/LREC_2.pdf"><span>de</span>
  <span>Marneffe</span> et al. 2006</a><o:p></o:p></span></p>
  <p><span><a
  href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.65.3351&amp;rep=rep1&amp;type=pdf"><span>Nivre</span> et al. 2007</a><o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture10Notes.pdf">[<span>notes</span>] More Parsing</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td></td>
  <td>
  <p><span>President's Day -- no class <o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/15<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>11<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Computational semantics I<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/17<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 17-18.3<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://gitlab.cslu.ohsu.edu/stephenwu/cslu-nlp-class/blob/master/hw3/hw3.md">HW
  3 due</a></span><span><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture11Notes.pdf">[<span>notes</span>] Meaning in Symbols</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>12<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Latent semantic
  analysis<o:p></o:p></span></p>
  <p><span>Topic modeling <o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/22<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&amp;arnumber=1511825"><span><span>Bellegarda</span></span><span> 2005</span></a><br>
  <a href="http://dl.acm.org/citation.cfm?id=2133826"><span><span>Blei</span></span><span> 2012</span></a><o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture12Notes.pdf">[<span>notes</span>] Distributional Semantics</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>13<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Computational semantics II<o:p></o:p></span></p>
  <p><span>Discourse<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/24<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 21, <a
  href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.178.4281&amp;rep=rep1&amp;type=pdf"><span><span>Bos</span></span><span> 2008</span></a><o:p></o:p></span></p>
  <p><span><a
  href="http://www.isi.edu/~ulf/amr/help/amr-guidelines.pdf"><span>Banarescu</span> et al 2012</a><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture13Notes.pdf">[<span>notes</span>] Semantics &amp; Discourse</a></span><span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>14<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Information Extraction<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>2/29<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 22<o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture14Notes.pdf">[<span>notes</span>] Information Extraction</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>15<o:p></o:p></span></p>
  </td>
  <td>
  <p><i style='mso-bidi-font-style:normal'><span>Text classification<o:p></o:p></span></i></p>
  <p><i style='mso-bidi-font-style:normal'><span>Sentiment analysis - no class<o:p></o:p></span></i></p>
  </td>
  <td>
  <p><i
  style='mso-bidi-font-style:normal'><span>3/2<o:p></o:p></span></i></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://gitlab.cslu.ohsu.edu/stephenwu/cslu-nlp-class/blob/master/hw4/hw4.md">HW
  4 due</a></span><span><o:p></o:p></span></p>
  </td>
  <td></td>
 </tr>
 <tr>
  <td>
  <p><span>16<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Machine translation<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>3/7<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>J&amp;M 25<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture15Notes.pdf">[<span>notes</span>] Machine Translation</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>17<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Evaluation<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>3/9<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://dl.acm.org/citation.cfm?id=1516107"><span><span>Belz</span></span><span> 2009</span></a><br>
  <a
  href="http://www.cslu.ogi.edu/~gormanky/courses/CS662/PDFs/resnik_lin_2010.pdf"><span><span>Resnik</span></span><span> &amp; Lin 2010</span></a><o:p></o:p></span></p>
  </td>
  <td></td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture16Notes.pdf">[<span>notes</span>] NLP Evaluation</a><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>18<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Applications: NLP in
  Clinical Text<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>3/14<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://gitlab.cslu.ohsu.edu/stephenwu/cslu-nlp-class/blob/master/hw5/hw5.md">HW
  5 due</a></span><span><o:p></o:p></span></p>
  </td>
  <td>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture17Notes.pdf">[<span>notes</span>] Clinical Text</a><o:p></o:p></span></p>
  <p><span><a
  href="http://cslu.ohsu.edu/~wst/nlp-class/lectures/Lecture17Slides.pptx">[<span>notes</span>] Stephen's research</a></span><span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr>
  <td>
  <p><span>19</span><span><o:p></o:p></span></p>
  </td>
  <td>
  <p><span>Final exam<o:p></o:p></span></p>
  </td>
  <td>
  <p><span>3/16<o:p></o:p></span></p>
  </td>
  <td>
  <p><span><o:p>&nbsp;</o:p></span></p>
  </td>
  <td></td>
  <td></td>
 </tr>
</table>

 
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

## Acknowledgments
Many thanks to Kyle Gorman (now at Google) and Steven Bedrick (CSLU faculty) for their efforts on previous versions of this class.
