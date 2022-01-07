---
layout: post
title: 40 Awesome Programming Resources
canonical_url: 'https://jlsunday.com/resources/2021/12/14/Forty-Awesome-Programming-Resources.html'
categories: Resources
tags: [tools, software, list, IDEs, database-manager, database, VSCode, DBeaver, markdown, time-trackers, VSCode-Extensions, resources, SQL, Python, Git, full-stack, newsletter, games]
comments: true
image: '/images/other-images/40-awesome-programming-resources-markdown-screenshot.png'
excerpt: 40 awesome programming resources regarding tools, IDEs, VS Code Extensions, tutorial sites, and newsletters.
summary: 40 awesome programming resources regarding tools, IDEs, VS Code Extensions, tutorial sites, and newsletters.
description: 40 awesome programming resources regarding tools, IDEs, VS Code Extensions, tutorial sites, and newsletters.
last_modified_at: 2021-12-29 12:50:00 +0000
---

* TOC
{:toc}

## Intro

<figure class="kg-card kg-image-card kg-card-hascaption" style="margin-top: 20px;">
        <img alt="40 Awesome Programming Resources Markdown Screenshot" src="{{ '/images/other-images/40-awesome-programming-resources-markdown-screenshot.png' | prepend: site.baseurl }}" class="kg-image" loading="lazy" title="40 Awesome Programming Resources Markdown Screenshot">
    <figcaption>
        A screenshot of this post as a Markdown WIP. Image created by the author.
    </figcaption>
</figure>

> _**UPDATED 2021/12/29**_<br>
> Added "Best practices for writing code comments" to "General".<br>
> Added Stack Overflow's newsletter, _The Overflow_, to "Newsletters".<br>
> Appended info to the end of "My Newsletter" in "Newsletters".

First off, I just want to mention that this post, actually, the majority of this site was written in markdown.
Markdown is extremely useful in reading and writing documentation for source code, taking notes, and even writing websites. I'll have more on Markdown below.

Secondly, this list is specific to the tools and resources I used regularly when I started my first job at *UST*, now 
*98Ventures*. I originally wrote everything here as a getting-started programming primer for a new-hire who would be
taking over my old position since I had been promoted. I spent a lot of time on this back in the day, and I know my colleague made
good use of the resources listed here, so I thought I would share it with all of you. I will also be adding new resources
that didn't appear in the original document.

Finally, believe it or not, I'm not making money (yet :wink:) from any of the sites, tools, or resources I've linked to here. I honestly just think they all rock and are worth sharing.

> _**Pro-Tip:**_ Be on the lookout for list items marked with :star:! These are the tools I use often and highly recommend.

## Tools

---

### IDEs and Apps

- **[Visual Studio Code (VS Code)](https://code.visualstudio.com/){:target="_blank"}{:rel="noopener noreferrer"}**
  <br/>Extremely popular. I use this editor for pretty much everything, especially SQL scripts when utilizing the
  [SQL Server (mssql)](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql){:target="_blank"}{:rel="noopener noreferrer"} extension I have listed in the VS Code extension section below.
  - Free and open source.
  - Great for frontend web development.
  - Extremely extensible with extensions for anything you can think of.
  - Great Python editor if PyCharm professional is too expensive.
  - Their [docs](https://code.visualstudio.com/docs) have great tutorials on multiple languages and topics.

- **[DBeaver Community](https://dbeaver.io/){:target="_blank"}{:rel="noopener noreferrer"}** :star: :star: :star:
  <br/>A Database manager that is infinitely more flexible and easier to use than any other DB manager I've ever used, including SQL Server Management Studio (SSMS), PHP MyAdmin, and MySQL Workbench.
  <br/>As a matter of fact, I may need to do a post specifically on DBeaver. I can't stress enough how awesome this app is.
  - Free and Open Source
  - Great for quickly looking at data and metadata in a table
  - Supports all the popular databases:
    - MySQL
    - PostgresSQL
    - SQLite
    - Oracle
    - DB2
    - SQL Server

- **[Boostnote](https://boostnote.io/){:target="_blank"}{:rel="noopener noreferrer"}**
  <br/>A text editor specifically for Markdown. While VS Code has decent Markdown extensions, sometimes an editor made specifically for Markdown is preferred
  - Free and Open Source
  - Side-by-side comparison of what you're writing and what it will look like when rendered.
  - Can export to multiple formats, such as HTML and PDF.

- **[Obsidian](https://obsidian.md/){:target="_blank"}{:rel="noopener noreferrer"}** :star:
  <br/>I actually went back-and-forth about whether to add this when I already have Boostnote listed. However, while Boostnote was on my original list, I have since fallen in love with Obsidian.
  - Features a more sophisticated file and folder structure.
  - Has a lot of great extensions.
  - Utilizes tags to build a visual web of your thoughts and notes.
  - There is a free app on mobile that allows you to sync your notes between devices.

- **[Git Extensions](https://gitextensions.github.io/){:target="_blank"}{:rel="noopener noreferrer"}** :star: :star: :star:
  <br/>First off, if you haven't heard someone say "You have to know Git on the command line to even be considered for a job in programming," then I promise you soon will.
  Sure, it's nice to know, especially if you just need to do a quick pull, but in my five years of programming, I have yet to be told that I HAVE to use a terminal for Git, and I have never felt like I needed the command line while using Git Extensions.
  - It's free!
  - It has visual Git history
  - Interface customization
  - A visual diff/commit window that allows you to stage and reset files and individual lines.
  - A stash management window that makes it easier to remember what you have stashed, where, and whether there are old stashes that need to be deleted.
  - There are even commands that make branch resetting, rebasing,and commit cherry-picking a breeze!
  - Seriously, if you don't try anything else out from this post, you should at least check this one out. Like DBeaver, I'm probably going to do a post specifically on Git Extensions because it is so awesome.

### Time Trackers
- **[Activity Watch](https://activitywatch.net/){:target="_blank"}{:rel="noopener noreferrer"}** - Time tracker to help track the time you spend on a project, or anything on your computer.
  - Free and open source.
  - They have extensions for multiple IDEs as well as a Chrome extension.
- **[WakaTime](https://wakatime.com/){:target="_blank"}{:rel="noopener noreferrer"}** :star: :star:
  <br/>Time tracker specific to software development/programming. Great way to measure your work and experience.
  - Free version and paid version.
  - Extensions for pretty much every IDE under the sun.
  - I use this tracker to report my weekly time to my manager every week. Highly recommend!
  - Also, the graphs are just really cool to see when you have a bunch of different projects, languages, and repos to visualize.

### VS Code Extensions
Here is a list of extensions I've found useful in both my work and personal software development:
- **[aw-watcher-vscode](https://marketplace.visualstudio.com/items?itemName=lindraupe.aw-watcher-vscode){:target="_blank"}{:rel="noopener noreferrer"}** - The Activity Watch extension for VS Code
- **[Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify){:target="_blank"}{:rel="noopener noreferrer"}** - Formats code that you may have pasted into a file.
- **[Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer){:target="_blank"}{:rel="noopener noreferrer"}** - Helps differentiate different levels of nested parenthesis in your code. Super useful for SQL or nested arrow functions in JavaScript.
- **[Night Owl](https://marketplace.visualstudio.com/items?itemName=sdras.night-owl){:target="_blank"}{:rel="noopener noreferrer"}** :star: - A theme that is nice on the eyes and allows font ligatures.
- **[nomnoml](https://marketplace.visualstudio.com/items?itemName=doctorrustynelson.vscode-nomnoml){:target="_blank"}{:rel="noopener noreferrer"}** - A tool for rendering UML diagrams based on the nomnoml library.
- **[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python){:target="_blank"}{:rel="noopener noreferrer"}** - Official Microsoft extension developed specifically for VS Code. Highly recommended if you want to use Python.
- **[Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv){:target="_blank"}{:rel="noopener noreferrer"}** :star: - Helps to visually identify the columns in a CSV file. Especially useful if you find yourself working with CSVs for test or example data.
- **[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync){:target="_blank"}{:rel="noopener noreferrer"}** - Useful if you use VS Code on multiple computers. Syncs your settings between the two computers.
- **[SQL Server (mssql)](https://marketplace.visualstudio.com/items?itemName=ms-mssql.mssql){:target="_blank"}{:rel="noopener noreferrer"}** :star: :star: :star:
  - Official Microsoft extension for SQL Server.
  - Extremely useful if you want to use VS Code for SQL scripts and reporting.
  - While I very much love DBeaver, sometimes I need to write a query with a lot of `JOIN`s, `PIVOT`s, or maybe even a variable `TABLE`. When the need arises, utilizing a great editor like VS Code has its advantages over the built-in editor present within DBeaver.
- **[TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight){:target="_blank"}{:rel="noopener noreferrer"}** :star: - Highlights any `TODO`s, `FIXME`s, or other keywords in comments.
- **[Wakatime](https://marketplace.visualstudio.com/items?itemName=WakaTime.vscode-wakatime){:target="_blank"}{:rel="noopener noreferrer"}** :star: - Wakatime's official extension for VS Code.



## Learning Resources and Tutorials by Language

---

### SQL
- [SQL Murder Mystery](https://mystery.knightlab.com/){:target="_blank"}{:rel="noopener noreferrer"} :star: - Fun little game for practicing SQL. I actually recommend checking out their [GitHub repo](https://github.com/NUKnightLab/sql-mysteries){:target="_blank"}{:rel="noopener noreferrer"}. It contains a lot of great SQL resources. You can also download the SQLite database the game depends on and run the scripts directly from VSCode or DBeaver (Which I recommend over doing everything directly on their website).
- [X-Team's Roadmap for Learning SQL](https://x-team.com/blog/learning-sql-roadmap/){:target="_blank"}{:rel="noopener noreferrer"} - A great roadmap for beginners.
- [Official Microsoft SQL Server Docs](https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15){:target="_blank"}{:rel="noopener noreferrer"} - References and articles on pretty much everything SQL Server. This [link](https://docs.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver15){:target="_blank"}{:rel="noopener noreferrer"} is especially useful.
  > _**Pro-Tip:**_ "T-SQL" is the specific SQL language used by SQL Server. You'll hear people use "T-SQL" and "SQL Server" interchangeably when referring to Microsoft's flavor of SQL.

### Python
- [Full Stack Python](https://www.fullstackpython.com/){:target="_blank"}{:rel="noopener noreferrer"} - A great all-purpose general reference for all things Python.
- [Real Python](https://realpython.com/){:target="_blank"}{:rel="noopener noreferrer"} - A site with amazing written and video tutorials on a multitude of Python topics. This is my go-to resource for Python programming and I wish *every* language had a tutorial website this amazing. They recently launched a paid version of the site, so a lot of the videos may not be available, but the written articles and tutorials are still free and I personally find them to be more than enough.
- [Automate the Boring Stuff](https://automatetheboringstuff.com/#toc){:target="_blank"}{:rel="noopener noreferrer"} :star: - Another great resource that I use regularly. This is the online version of a written book. It gets updated whenever the book updates. It's also free! Contains tutorials on automating a ton of different time-consuming processes.
- [W3 Schools - Python](https://www.w3schools.com/python/default.asp){:target="_blank"}{:rel="noopener noreferrer"} - I know you already mentioned W3, but in case you didn't already know, it is an amazing reference for quick functions and other intricacies of the Python language.
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/){:target="_blank"}{:rel="noopener noreferrer"} - Like *Full Stack Python*, this is another great resource for general Python info.
- [Awesome Python](https://awesome-python.com/){:target="_blank"}{:rel="noopener noreferrer"} :star: :star: - A curated list of awesome Python frameworks, libraries, software, and resources.

### Markdown
In case you haven't noticed yet, most of the tutorials and articles you read online are written in Markdown. A lot of the READMEs you find in GitHub repos are also written in Markdown. Also, Confluence, the site we use for documentation at *98Ventures* also utilizes Markdown.
- [StackEdit](https://stackedit.io/){:target="_blank"}{:rel="noopener noreferrer"} - An in-browser Markdown editor. In case you don't want to use VS Code Markdown extensions or Boostnote, this is a great alternative for writing Markdown.
- [Markdown Guide](https://www.markdownguide.org/){:target="_blank"}{:rel="noopener noreferrer"} :star: - I use this regularly as a reference when I need to write documentation, or other things, in Markdown.
- [Markdown in API Documentation](https://documenter.getpostman.com/view/4630964/S1LsXVJy?_ga=2.65655143.877826915.1571251520-1293263363.1571251520&version=latest){:target="_blank"}{:rel="noopener noreferrer"} - This website is specific to Markdown for the purposes of API documentation, but is a great way to see Markdown examples and how it is rendered, along with explanations.

### Git
- [Git Handbook](https://guides.github.com/introduction/git-handbook/){:target="_blank"}{:rel="noopener noreferrer"} - A quick reference and refresher on Git.
- [Resources to Learn Git](https://try.github.io/){:target="_blank"}{:rel="noopener noreferrer"} - More Git Learning Resources

### General
- [Best practices for writing code comments](https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/){:target="_blank"}{:rel="noopener noreferrer"} :star: :star: :star:
  - I personally do my best to follow these guidelines, and I can't recommend enough that you strive to do the same. Good comments save so much development time and prevent a lot of frustration.
  - Comments help with type hinting in IDEs, tracking down usages, and they help devs understand what was going through your mind and why you made the choices you did.
- [FreeCodeCamp](https://www.freecodecamp.org/news/){:target="_blank"}{:rel="noopener noreferrer"} :star:
  - A great general resource for free tutorials, articles, and news for all things related to coding and programming. I recommend signing up for their newsletter.
  - 5,000+ free tutorials.
  - Free certification courses [here](https://www.freecodecamp.org/learn/){:target="_blank"}{:rel="noopener noreferrer"}.
- [Udacity](https://www.udacity.com/){:target="_blank"}{:rel="noopener noreferrer"} - Paid and free tech tutorials on a variety of topics. I highly recommend this site if you want more formal tutorials.
- [Pluralsight](https://www.pluralsight.com/){:target="_blank"}{:rel="noopener noreferrer"} - Can be expensive, but there is a free trial. Excellent and professional video tutorials on a range of tech topics. One of my go-tos.
- [Advent of Code](https://adventofcode.com/){:target="_blank"}{:rel="noopener noreferrer"}
  - A yearly challenge of programming word problems.
  - A new challenge is posted every night at midnight for the month of December.
  - You can utilize any language of your choosing to solve the problems.
  - Sponsored by some really great companies.
    - Some of these companies host their own challenges.
    - Many of them scout for prospects among the high scorers in the Advent of Code leaderboard.

## Newsletters

---

Believe it or not, I only stumbled into a few of the resources I listed above organically via Google searches. I learned about many of them
via newsletters and other blogs. So, here I am going to list a few newsletters that I recommend for anyone interested in programming.
Yes, yes, I know... Sometimes our mailboxes can get cluttered with junk or stuff we signed up for that
seemed like a good idea at the time. However, even if you delete 90% of the emails you receive from these sources, then you actually
occasionally open one of them on a whim one day, I can pretty much guarantee you won't regret it, and you will find something new and cool.
- X-Team's Newsletter :star: - A weekly email that contains links to cool repos, top stories regarding tech, some of their own tutorials and articles, as well as a link to their awesome radio. Sign up [here](https://x-team.com/blog/#subscribe){:target="_blank"}{:rel="noopener noreferrer"}.
- Free Code Camp's Newsletter :star: - A weekly email with at least 5 links to great tutorials, interviews, and tech news. Sign up [here](https://www.freecodecamp.org/email-sign-up/){:target="_blank"}{:rel="noopener noreferrer"}
- Stack Overflow's Newsletter, [The Overflow](https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/){:target="_blank"}{:rel="noopener noreferrer"} - From their site description, "A newsletter by developers, for developers, curated by Cassidy Williams and the Stack Overflow team. Every week, we’ll share a collection of great questions from our community, news and articles from our blog, and awesome links from around the web."
- PyCoder's Weekly Newsletter - A weekly Python specific newsletter. Each email contains articles, Python community announcements, popular discussions on social media, Python job listings, tutorials, repos, and more! Sign up [here](https://pycoders.com/){:target="_blank"}{:rel="noopener noreferrer"}
- My Newsletter :star: :star: :star: :wink: - ...Coming Soon! Until then, you can subscribe to my RSS feed with your favorite RSS feed aggregator, Outlook, or Chrome extension. My favorite RSS Feed reader is [FeedBro](https://nodetics.com/feedbro/){:target="_blank"}{:rel="noopener noreferrer"}. Check it out! Many email clients also allow you to add RSS feeds to your inbox list (Such as Outlook).

## Final Thoughts

---

So there you have it; 40 awesome development resources! Is there anything else that you'd like to see on this list?
Any comments, concerns, suggestions, or requests? Please leave a comment below, or feel free to contact me via one of the links under my "About Me."
Thanks for reading, and stay tuned; There is more where this came from!

A teaser of topics in the works:
- Code Snippets
  - What are Snippets?
  - Why you should use snippets
  - Snippets in VSCode
  - Snippets in Webstorm
  - Pros and Cons to Snippet Extensions
- 12 Code Games for Fun and Practice
- A list of my favorite cheatsheets
- A Deep Dive into Git Extensions and What Makes it Great
- A Deep Dive into DBeaver and What Makes it Great
- How to Create a Python GUI Executable, Complete with an Installer

See you soon!
