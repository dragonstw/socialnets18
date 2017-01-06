# techied

`techied` sets up a `git` infrastructure for computer science
education that is based on the principles of:

* Transparency: an open-source, reproducible-research approach to
  integrity and evaluation
* Excellence: grading structure that rewards performance along
  multiple dimensions 
* Collaboration: grading practices that include peer review
* Humility: enforcing iterative improvement and taking constructive
  criticism
* Innovation: evaluating on divergence as well as convergence

***************
## Setting up a class

1. First, you clone this repository.  You've probably already done this.

	git clone git@gitlab.cslu.ohsu.edu:stephenwu/techied.git

2. This comes with a sample syllabus `syllabus.md` in the root
directory; edit this to your liking. But, note that many of the class
policies in the default `syllabus.md` embed the "techi" education
principles above.

3. Assigning homework:

	a. Create a file `hw/<hw_tag>.md` that describes the homework.
	This file should have a `## Rubric` section at the end, which will
	be used in generating peer review templates and instructor grading
	templates.  See the default [hw/hw0.md](hw/hw0.md) as an example.
	
	b. Assign the homework to the class, stipulating that there will be
	an extra peer review period.  Each student should complete the
	work on a `develop-<student_initials>` branch, rebasing as
	necessary on subsequent homeworks.  For example, if you've
	released a new homework to the `master` branch, your students
	would stay up to date on their own `develop-*` branches by doing:
	
		git checkout master
		git pull
		git checkout develop-<student_initials>
		git rebase -i origin/master
		git push origin develop-<student_initials> -f
	
	c. Edit the [admin/students.txt](admin/students.txt) file to have
	one student's initials (or some other unique ID) per line.
	
	d. Run `python admin/peer_reviewers.py -a <hw_tag> -d
	<due-date-string>`; this will produce  template for peer reviews
	in `grades/<hw_tag>.for_X_by_Y.md` and will also print to `stdout`
	a random set of reviewer assignments (2 reviewers each).
	
	e. Tell each student their reviewer assignments privately
	(single-blind, recommended) or publicly (not blind). Have them
	replace 'X' and 'Y' in `grades/<hw_tag>.for_X_by_Y.md` with their
	own name and the person whose homework they are grading,
	respectively.

	f. When the peer reviews are submitted, create a score sheet (also
    drawing from `students.txt` and `hw/<hw_tag>`) for final grades on
    this assignment:
		
		python admin/score_sheets.py <hw_tag>

	This will populate your `grades` directory (git will not track
	these files, due to `.gitignore`).





