# Using git
This is a brief introduction to using `git` on the command line.  Since you can get more thorough tutorials [elsewhere](https://git-scm.com/docs/gittutorial), I'll just give you the essentials for submitting a `submission.md` file on your homework, e.g., [Assignment 0](https://github.com/dragonstw/socialnets18/blob/master/assignments/assignment0.md).  This should elucidate the process of peer review and everything else, too, which we will go over in class.

More about git:

* Git is pretty neat because it gives great control over your file histories, and also because it allows for asynchronous collaboration.
* Use it for primarily non-binary files, i.e., things like source code rather than things like a machine learning model that you've trained.
* Also, **do not use git for large files**!!  It will keep copies of them around forever, even if you remove them from the repository at a later time.


## Get git
First, make sure you have git.  At the terminal, type

    git --version

If that doesn't work, then [install git](https://www.atlassian.com/git/tutorials/install-git/linux).

## Add an SSH key
After you've installed git, I highly recommend that you [add an SSH key](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html)to your gitlab account. (The [github version](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) of the documentation might be a bit easier to understand for the part where you actually create your SSH key.)

It's not absolutely essential, though.  Adding an SSH key means that you can work with git without having to enter your password as much (the alternative is HTTP).

## Clone the repo
At this point, you should clone the git repository for the class.  In other words, all the source code and files and everything will get downloaded to your computer.  Also, you'll be able to look at the history of how you and others modified your files.

Go to a directory where you want your `socialnets18` folder to live.  Type this:

    git clone git@repo.cslu.ohsu.edu:stephenwu/socialnets18.git

(Note: if you didn't set up your SSH key, you can do `git clone https://repo.cslu.ohsu.edu/stephenwu/socialnets18.git`, but again, I highly recommend the SSH key route.)

You should be able to see that there are files like `README.md` and folders like `admin`, `grades`, `hw`, `resources`.

## Create a branch
When you clone a repository, by default you start out on the `master` branch.  You can see this if you use the `git branch` command:

    ~/teaching$ cd socialnets18
        /Users/wst/teaching/socialnets18
    ~/teaching/socialnets18$ git branch
        develop-stephenwu
      * master
        syllabus
	~/teaching/socialnets18$

Create your own branch, which you will use for the rest of this class.

    git checkout -b develop-<username>

Of course, you replace `<username>` with your own github username.

This means that you now have a **local** branch (i.e., on your computer).  Any changes you make now will not affect anyone else.

(Next time, when you want to switch to an existing branch, you use `git checkout` but leave out the `-b`.)

## Stage a file
Let's try creating an empty `submission.md` file and adding it to the git repository:
```
touch assignments/assignment0/submission.md
git add assignments/assignment0/submission.md
```

When you `git add` something, it's now "staged" but isn't yet part of the repository.  Check to make sure it's there (you'll use this command a lot):

    git status

## Commit the file
Now you want to tell git to take note of **this version** of `submission.md`, in other words, to commit it.
```
git commit -m 'try committing an empty file'
```
The `-m` argument means that you're going to put in a message for the logs.  A good practice is to use a present-tense verb as your first word, and keep the message less than 40 characters.

(Later on, if you have made modifications to files, you can use `git commit -am '...'` and the `-a` part will check in your modifications without you having to type `git add` for each of them.)

## Push the file
So now you have your file in your **local** branch called `develop-<username>`, but no one else can see it.  You can keep it this way until you want to actually submit your assignment.

When you ACTUALLY want to submit so that the instructors (and everyone else) can see it, you do:

    git push origin develop-<username>

This creates (or for future updates, modifies) a **remote** branch on `repo.cslu.ohsu.edu`, and now anybody who is working with the same repository can see it -- including you, from another machine!

## Rebasing
Over the course of the class, I will be updating the `master` branch, while you will be working on your `develop-<username>` branch.  To keep these as much in sync as possible, you can use two strategies: remove your branch and re-create it with a new name (but be aware, you may lose all your work), or _rebase_.

First, commit any changes in your own branch.  Then, rebasing normally looks something like this:
```
git checkout master
git pull
git checkout develop-<username>
git rebase origin/master
```

Now you should have the up-to-date `master` branch, with any changes you've made in your branch re-played on top of it!