# HW0: Test
***********

## Description
This homework is just setup and stuff for the various tools we'll be
using in this class.

1. **Install Python 2.7.x** if you don't have it already.

2. (Optional) Install these helpful libraries (typically via
   [pip](http://www.pip-installer.org/en/latest/installing.html): 
   `pip install package-name`):

	a. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) -
	lets you install specific python packages for a particular
	project, without adding those packages to the machine you're
	working on.
	b. [ipython](http://ipython.org/) - an interactive command line, a
	tad nicer than the default python interpreter.
	c. [jupyter notebook](http://jupyter.readthedocs.org/en/latest/install.html) - 
	a very neat web-based python interpreter that allows you to
	interleave markdown and LaTeX equations with runnable Python code.

3. **Install [git](https://git-scm.com/)** - the version control
   software we will use to share and review homework assignments.
   
   a. Make sure you have a gitlab account, and have permissions to
   push and pull from your class's repository.
   b. Clone the class repository and set up any necessary git global
   variables.
   c. Create a `develop-<YOUR-INITIALS>` branch off of master via `git
   checkout -b develop-<YOUR-INITIALS>`

4. **Install nltk** (typically `pip install nltk`) and **download the
   brown corpus** (at least).  To download this interactively:
   
   * `python -m nltk.downloader`
   * Select "brown"
   * Click on "Download"

5. For this assignment, you'll need to `pip install nilsimsa` also.

6. Post your output from running `python hw/test_setup.py` from the
   root directory of the git project.
   
   * Copy and paste your output as `submission.md` (in
     [markdown format](https://daringfireball.net/projects/markdown/syntax))
   * Describe what `test_setup.py` does, and note anything interesting
     about it
   * Add and commit this to your `develop-<YOUR-INITIALS>` branch
   

## Due
Before next class period


## Rubric: /100

* /60 Produce the output from the script.
* /20 Describe what the script does in a `submission.md` file
* /20 Push successfully to your `develop-<YOUR-INITIALS>` branch in git

**Comments**:
