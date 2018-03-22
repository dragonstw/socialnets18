# Assignment 1: Your Facebook Network
We're trying to learn how to analyze social networks. Rather than just learn about theory, we'll try to do some actual analysis on our own, real (online) social network! So in this assignment, you will download data corresponding to your Facebook account, then visualize it and calculate some of the metrics we've learned about.

You should [rebase your branch](../resources/using_git.md) before continuing, so that you have the up-to-date resources.
<!-- (e.g., [assignments/fb.py](assignments/fb.py)). -->

## Step 1: Download your Facebook data
Because Facebook has upped its security, public network data from Facebook is not as easy to access as it used to be (circa 2014). Thus, official means of accessing the network data are not working. Some methods will allow you to get your own friend lists, but not be able to get your friends' friends (path=2). Others won't work at all.

<!-- Here are 2 options for getting your Facebook data downloaded. -->

<!-- ### Option A: Lost Circles (More Simple) -->
[Lost Circles](https://lostcircles.com) is a Chrome extension that uses a normal Chrome browser to retrieve all of your friends and your friends' friends. You have to be willing to trust all of your Facebook data to this app. It actually does too much of the work for you, so we will not use its UI, and instead export data to be viewed in Gephi.

1. Download the Chrome extension
2. In the Chrome plugins toolbar, click on the lost circles icon. Chrome will open a tab with Facebook; log in if it asks you to.
3. Click on `Start loading`. Wait as your browser (and a second, tiny browser) crawls your network and uploads your data to their servers -- this may take an hour or more, depending on your connection speed and your number of friends.
4. When Lost Circles is finished, click on `Download (...)` -> `Graphml (no pics)`. WARNING: Be careful NOT TO HIT `Clear Data`, though it is fine to do this AFTER downloading the data.

<!--
### Option B: Access Facebook Graph API from a Facebook Developer account (More Robust)
This is the more time-intensive option. However, it will also give you the tools to start writing your own Facebook App, etc (though my code is in Python instead of the typical JavaScript). You also do not have to trust your FB data to a third party - you will control the data yourself. Also, it will be very unlikely for Facebook to discontinue support of its Graph API, or for the Facebook Python SDK to stop being supported -- so you will likely be able to use this method for years to come.

1. Go to the [Facebook Developers site](https://developers.facebook.com) and start an account.
2. Start an app -- name it whatever you want, e.g., `SocialNets18`.
3. On the left-hand pane, click on `Settings` -> `Basic`.
# 4. You should see `App ID`. Save this to a plain text file, e.g., in `socialnets18/assignments/.fb_app_id`. DO NOT COMMIT THIS TO THE GIT REPOSITORY. If it bothers you, use [.gitignore](https://help.github.com/articles/ignoring-files/).
5. Click to show the `App Secret`. Save this to `socialnets18/assignments/.fb_app_secret`. Again, DO NOT COMMIT THIS TO THE GIT REPOSITORY.
6. Install the [Facebook Python SDK](https://github.com/pythonforfacebook/facebook-sdk), which accesses the Facebook Graph API. Consider installing the package in a `pip` or `conda` environment.
# 7. Create a `User Token` on with Facebook for Developers' [Access Token Tool](https://developers.facebook.com/tools/accesstoken). Copy this down and use it in the next step. These tokens expire, so YOU MAY NEED TO DO THIS MANY TIMES WHEN YOU RUN THE CODE AGAIN.
8. Run the `assignments/fb.py` code. Follow the instructions to obtain a User Token from the App Token (it will direct you to the [Graph API Explorer](https://developers.facebook.com/tools/explorer/)), giving you programmatic access to your Facebook Network!
-->


## Step 2: Load your data in Gephi
Now that you have your data in GraphML format, you can import it into Gephi.

1. [Download Gephi](https://gephi.org/users/download/) and install it on your machine. OPTIONAL: Consider going through the [tutorial on how to use gephi](https://gephi.org/users/quick-start/).
2. Start Gephi, and select `Open Graph File` (or use `File` -> `Open`). Select the `*.graphml` file you created in Step 1.
3. Display your node labels. If necessary, clean up your data so that it shows individuals' names rather than any other data.


## Step 3: Calculate and report some graph metrics
Answer the following questions, and enter your results in [this Google Form](https://goo.gl/forms/MnG87AaJZ4EFu4mz1) so we can do some class-level analysis. Many of the questions will require for you to think back to metrics defined in our lectures, explore the Gephi interface, and figure out how you can answer the questions.

On each of the follow up questions, the options are: {`node degree`, `average node degree`, `edge weight/tie strength`, `characteristic (average) path length`, `giant component`, `local bridge/span`, `clustering coefficient`, `connectance`}.

1. What percent of your friends are connected (through any number of links) to most of your other friends?

    a. What metric or concept is expressed by this number?

2. Find the person with most friends in common with you. How many friends do they share with you?
    
    a. What metric or concept is expressed by this number?

3. On average, how many Facebook friends do your friends have?

    a. What metric or concept is expressed by this number?

4. Overall, how well-connected are your friends to each other? Give an answer between 0 and 1.

    a. What metric or concept is expressed by this number?

5. Considering possible random pairs of friends in your network, on average how close/far are your friends?

    a. What metric or concept is expressed by this number?

    b. Recall that you are connected to each node in the graph, though this is not shown explicitly in your data. However, not everyone else in the graph is directly connected to each other. Are you more often the shortest link between two of your friends? Or do most of your friends already know each other? 



## Step 4: Lab writeup
Write a short but structured lab report, similar to how an extended abstract might be written (~500-2000 total words). Create an `assignments/assignment1.md` file and commit it locally as soon as you finish. Then, `git push origin develop-<name><fathersname>` by the deadline. Include an **Introduction** of the lab, **Methods** used to get analysis **Results**, and **Discussion**.

* In **Introduction**, describe the main point -- why did we do this lab?
* In **Methods**, _summarize_ the process of producing the results. Were there any particularly tricky steps?
* In **Results**, give statistics from Step 3 and/or other statistics you find interesting. Also include a picture of your network, organized and/or labeled in a way that makes sense to you. This can be done in markdown with the following syntax (making sure that an `SVG` file is checked in in the same `assignments` directory. Please use SVG and not PNG or PDF):

```
![Network example](example.svg)
```
* In **Discussion**, interpret each statistic from the Results. Describe why you chose to present your network the way you did.



## Due
Thursday, 29th March, 2018 @ 8:30am.

Both the Google Forms and Checked-in lab report need to be present by the due date/time.


## Rubric: /100

* /50 Network statistics
    * /20 Submit via Google Forms
    * /30 Legitimate metrics/concepts (6 x 5 pts)
* /50 Lab Report
    * /10 Introduction
    * /5 Methods
    * /15 Results: SVG image,
    * /15 Discussion of results
    * /5 Writing style

**Comments**:


