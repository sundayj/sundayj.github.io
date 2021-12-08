---
layout: post
title: Programming Resources
categories: Resources
tags: [tools, software, list, tools, IDEs, database-manager, database, VSCode, DBeaver, markdown, time-trackers, VSCode-Extensions, resources, SQL, Python, Git, full-stack]
comments: true
summary: Here is a list of programming resources that I found very handy when I first started my programming journey.
---

## Intro

First off, I just want to mention that this post, actually, this entire site was written in markdown.
Markdown is extremely useful in reading and writing documentation for source code, taking notes, and even writing websites. I'll have more on Markdown below.

Secondly, this list is specific to the tools and resources I used regularly when I started my first job at UST, now 
*98Ventures*. I originally wrote everything here as a getting-started programming primer for a new-hire who would be
taking over my old since I had been promoted. I spent a lot of time on this back in the day, and I know my colleague made
good use of the resources listed here, so I thought I would share it with all of you. I will also be adding new resources
that didn't appear in the original document.

## Tools

---

### IDEs and Apps
- **Visual Studio Code (VS Code)** - Extremely popular. I use this for pretty much everything, especially SQL scripts.
    - Free and open source.
    - Great for frontend web development.
    - Extremely extensible with extensions for anything you can think of.
    - Great Python editor if PyCharm professional is too expensive.
    - [VS Code Site](https://code.visualstudio.com/)
    - Their [docs](https://code.visualstudio.com/docs) actually have great tutorials on multiple languages and topics.

- **DBeaver** - A Database manager that is infinitely more flexible and easier to use than any other DB manager I've ever used, including SQL Server Management Studio (SSMS), PHP MyAdmin, and MySQL Workbench.
    - [DBeaver Site](https://dbeaver.io/)
    - Free and Open Source
    - Great for quickly looking at data and metadata in a table
    - Supports all the popular databases:
        - MySQL
        - PostgreSQL
        - SQLite
        - Oracle
        - DB2
        - SQL Server...

- **Boostnote** - A text editor specifically for Markdown. While VS Code has decent Markdown extensions, I prefer using this app when I strictly need to use Markdown. I actually used it to write this document.
    - [Boostnote Site](https://boostnote.io/)
    - Free and Open Source
    - Side-by-side comparison of what you're writing and what it will look like when rendered.
    - Can export to multiple formats, such as HTML and PDF. I will include those formats for this document as well so you can see how awesome Markdown is.

- **Obsidian**

### Misc
#### Time Trackers
- **Activity Watch** - Time tracker to help track the time you spend on a project, or anything on your computer. Free and open source. They have extensions for mutliple IDEs as well as a Chrome extension. [Activity Watch Site](https://activitywatch.net/)
- **Wakatime** - Time tracker specific to software development/programming. Great way to measure your work and experience. Free version and paid version. Extensions for pretty much every IDE under the sun. I use this tracker to report my weekly time to my manager every week. Highly recommend. [WakaTime Site](https://wakatime.com/)

#### VS Code Extensions
Here is a list of extensions I've found useful in both my work and personal software development:
- **aw-watcher-vscode** - The Activity Watch extension for VS Code
- **Beautify** - Formats code that you may have pasted into a file.
- **Bracket Pair Colorizer** - Helps differentiate different levels of nested parenthesis in your code. Super useful for SQL.
- **Kite Python Autocomplete** - AI suggestions and autocomplete based on how your type.
- **Night Owl** - A theme that is nice on the eyes and allows font ligatures.
- **nomnoml** - A tool for rendering UML diagrams based on the nomnoml library.
- **Python** - Official Microsoft extension developed specifically for VS Code. Highly recommended if you want to use Python.
- **Rainbow CSV** - Helps to visually identify the columns in a CSV file.
- **Settings Sync** - Useful if you use VS Code on multiple computers. Syncs your settings between the two computers.
- **SQL Server (mssql)** - Official Microsoft extension for SQL Server. Extremely useful if you want to use VS Code for SQL scripts and reporting.
- **TODO Highlight** - Highlights any TODOs, FIXMEs, or other keywords in comments.
- **Wakatime** - Wakatime's official extension for VS Code.



## Learning Resources and Tutorials by Language

---

### SQL
- [SQL Murder Mystery](https://mystery.knightlab.com/?utm_source=Iterable&utm_medium=email&utm_campaign=the_overflow_newsletter&utm_content=12-24-19) - Fun little game for practicing SQL. I actually recommend checking out their [GitHub repo](https://github.com/NUKnightLab/sql-mysteries). It contains a lot of great SQL resources. You can also download the SQLite database the game depends on and run the scripts directly from VSCode or DBeaver (Which I recommend over doing everything directly on their website).
- [Official Microsoft SQL Server Docs](https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15) - References and articles on pretty much everything SQL Server. This [link](https://docs.microsoft.com/en-us/sql/t-sql/language-reference?view=sql-server-ver15) is especially useful.
    - **FYI** - "T-SQL" is the specific SQL language used by SQL Server and people use "T-SQL" and "SQL Server" interchangeably when referring to SQL Server.

### Python
- [Full Stack Python](https://www.fullstackpython.com/) - A great all-purpose general reference for all things Python.
- [Real Python](https://realpython.com/) - A site with amazing written and video tutorials on a multitude of Python topics. This is my go-to resource for Python programming and I wish *every* language had a tutorial website this amazing. They recently launched a paid version of the site, so a lot of the videos may not be available, but the written articles and tutorials are still free and I personally find them to be more than enough.
- [Automate the Boring Stuff](https://automatetheboringstuff.com/#toc) - Another great resource that I use regularly. This is the online version of a written book. It gets updated whenever the book updates. It's also free! Contains tutorials on automating a ton of deifferent time consuming processes.
- [W3 Schools - Python](https://www.w3schools.com/python/default.asp) - I know you already mentioned W3, but in case you didn't already know, it is an amazing reference for quick functions and other intricacies of the Python language.
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/) - Like *Full Stack Python*, this is another great resource for general Python info.
- [Awesome Python](https://awesome-python.com/) - A curated list of awesome Python frameworks, libraries, software, and resources.

### Markdown
In case you haven't noticed yet, most of the tutorials and articles you read online are written in Markdown. A lot of the READMEs you find in Github repos are also written in Markdown. Also, Confluence, the site we use for documentation at *98Ventures* also utilizes Markdown.
- [StackEdit](https://stackedit.io/) - An in-browser Markdown editor. In case you don't want to use VS Code Markdown extensions or Boostnote, this is a great alternative for writing Markdown.
- [Markdown Guide](https://www.markdownguide.org/) - I use this regularly as a reference when I need to write documentation, or other things, in Markdown.
- [Markdown in API Documentation](https://documenter.getpostman.com/view/4630964/S1LsXVJy?_ga=2.65655143.877826915.1571251520-1293263363.1571251520&version=latest) - This website is specific to Markdown for the pruposes of API documentation, but is a great way to see Markdown stuff and how it is rendered, along with explanations.

### Git
- [Git Handbook](https://guides.github.com/introduction/git-handbook/) - A quick reference and refresher on Git.
- [Resources to Learn Git](https://try.github.io/)

### General
- [5 Challenging App Ideas You Can Start Building Today](https://medium.com/better-programming/here-are-5-challenging-app-ideas-you-can-start-building-today-jan-2020-78cd4fb45996) - An article showcasing ideas for practicing programming. I haven't had time to try them myself, but I thought they may be worth sharing. Also, [Medium](https://medium.com/) is a great resource for written tutorials, but be careful of when they were written; Some of the tutorials are out-of-date and use outdated technology.
- [FreeCodeCamp](https://www.freecodecamp.org/news/) - A great general resource for free tutorials, articles, and news for all things related to coding and programming. I recommend signing up for their newsletter.
    - 5,000+ free tutorials.
    - Free certification courses and tutorials [here](https://www.freecodecamp.org/learn/).
- [Udacity](https://www.udacity.com/) - Paid and free tech tutorials on a variety of topics. I highly recommend this site if you want more formal tutorials.
- [Pluralsight](https://www.pluralsight.com/) - Can be expensive, but there is a free trial. Excellent and professional video tutorials on a range of tech topics. One of my go-tos.
- Advent of Code
- 
