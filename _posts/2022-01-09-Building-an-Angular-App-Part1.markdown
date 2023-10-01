---
layout: post
title: "Building an App with Angular, Part 1: Introduction"
summary: Part one introduces the project and sets the stage for the following parts in the series.
excerpt: Part one introduces the project and sets the stage for the following parts in the series.
description: >-
    This post introduces the project and sets the stage for the following posts in the series.
    The series will cover HTTP Interceptors, logging, snackbar messages, angular material data tables, NGRx and more.
canonical_url: https://JLSunday.com/tutorials/angular/2022/01/09/Building-an-Angular-App-Part1.html
categories:
    Tutorials
    Angular
tags:
    tutorial
    Angular
    front-end
    Typescript
    JavaScript
    Angular-Material
    services
    in-memory-database
    flex-layout
    interceptors
    logging
    snackbar
image: https://JLSunday.com/images/other-images/undraw_Maker_launch_re_rq81.png
comments: true
last_modified_at: 2022/01/11
---

<figure style="margin-top: 20px;">
        <img alt="Angular Windows"  src="{{ '/images/other-images/undraw/undraw_Maker_launch_re_rq81.png' | prepend: site.url }}" loading="lazy" title="How do you like these angles?">
    <figcaption>
        Photo by <a href="https://undraw.co/search">unDraw.co</a>
    </figcaption>
</figure>

* TOC
{:toc}

## Intro

> **IMPORTANT**<br>
> This tutorial utilizes Angular 12. I realize Angular 13 is now published. If enough people request it, then I may make a tutorial
> on how to upgrade between the two versions. Afterwards, the new version will be available in this project's repo.


> **Part One - Intro Repo**<br>
> If you want to follow along with the progression of the app, you can find the repo for this part of the project under the
> [PartOne-Introduction](https://github.com/sundayj/JLSundayAngular/tree/PartOne-Introduction){:target="_blank"}{:rel="noopener noreferrer"}
> branch.

Hello, and welcome to my first posted Angular tutorial! Originally, I was going to go over how to create an Angular app from scratch,
but the [Angular Tour of Heroes App and Tutorial](https://v12.angular.io/tutorial#tour-of-heroes-app-and-tutorial){:target="_blank"}{:rel="noopener noreferrer"}
already does such a great job of that. So, what I am going to be doing in this series of posts is going over some of the more complicated
aspects of building an app with Angular. This first post will serve as an intro to the project, explaining the structure, and the
"why" behind some choices I've made. The next few posts will show how to implement some basic services and components that are useful for
any modern web app that consumes REST APIs. Then, in a few later posts, I will be covering Angular Material tables, forms,
state-management with NGRx, and more.

### The Project

This project is really just the completed *Tour of Heroes* app from the Angular tutorial. However, there are some important differences.
First, I decided to use the Angular *Tour of Heroes* app, because the point of this tutorial isn't "How to Design an App", "How to Plan an App",
"How to Invent an App," or anything like that. Rather, for the purposes of this series, I just need a basic app; Something with basic
functionality that can be expanded upon with more in-depth and complex examples. It is important to understand that I am not claiming
that this is an original app of my own creation.

### The Repository

The main repo for this project is the [JLSundayAngular](https://github.com/sundayj/JLSundayAngular){:target="_blank"}{:rel="noopener noreferrer"}
repo's main branch. It will always contain the current state of the project. To make the project easy to follow along with, I will
have branches for each part of the project containing the final state of the app at that point in the project. So, if
you want to start the project from the state displayed in this post (recommended), then you should clone the 
[PartOne-Introduction](https://github.com/sundayj/JLSundayAngular/tree/PartOne-Introduction){:target="_blank"}{:rel="noopener noreferrer"}
branch. The following post will have its own branch containing the final state of the app as described in that post.

So, effectively, you can clone the PartOne-Introduction branch and get familiar with it during this post. Then, when the next
post is published, you can follow along with that post. Finally, by the end of the next post, what you have should match what sits in the repo
for that specific post. I hope that is easy to understand. If not, please leave a comment at the bottom, via the [Contact Form]({{"/about/#contact-me" | prepend: site.url}})
, or contact me via one of the many means in the sidebar.

### Requirements

I've listed the requirements for this project here, as copied from the repo's package.json:

```json
{
    "dependencies": {
        "@angular/animations": "~12.2.0",
        "@angular/cdk": "^12.2.13",
        "@angular/common": "~12.2.0",
        "@angular/compiler": "~12.2.0",
        "@angular/core": "~12.2.0",
        "@angular/flex-layout": "^12.0.0-beta.35",
        "@angular/forms": "~12.2.0",
        "@angular/material": "^12.2.13",
        "@angular/platform-browser": "~12.2.0",
        "@angular/platform-browser-dynamic": "~12.2.0",
        "@angular/router": "~12.2.0",
        "angular-in-memory-web-api": "^0.12.0",
        "rxjs": "~6.6.0",
        "tslib": "^2.3.0",
        "zone.js": "~0.11.4"
    },
    "devDependencies": {
        "@angular-devkit/build-angular": "~12.2.13",
        "@angular/cli": "~12.2.13",
        "@angular/compiler-cli": "~12.2.0",
        "@types/jasmine": "~3.8.0",
        "@types/node": "^12.11.1",
        "jasmine-core": "~3.8.0",
        "karma": "~6.3.0",
        "karma-chrome-launcher": "~3.1.0",
        "karma-coverage": "~2.0.3",
        "karma-jasmine": "~4.0.0",
        "karma-jasmine-html-reporter": "~1.7.0",
        "typescript": "~4.3.5"
    }
}
```

### External Resources

The following links are the references I used when implementing the new additions to the project. You may find them useful as well.

- [Angular's Official Documentation](https://v12.angular.io/docs){:target="_blank"}{:rel="noopener noreferrer"}
  - [Angular CLI Reference](https://v12.angular.io/cli){:target="_blank"}{:rel="noopener noreferrer"}
- [Angular Material](https://v12.material.angular.io/){:target="_blank"}{:rel="noopener noreferrer"} - Material Design Components for Angular
- [Material Design Icons](https://google.github.io/material-design-icons/#icon-font-for-the-web){:target="_blank"}{:rel="noopener noreferrer"} - Important for the icons used in this project to display correctly.
- [Flex-Layout](https://github.com/angular/flex-layout){:target="_blank"}{:rel="noopener noreferrer"} - Very useful for quickly implementing
flexbox layouts without having to deal with all CSS styling.


### Differences

As I stated before, there are certain differences between this project and the *Tour of Heroes* app's original code.
So, if you want to follow along, I recommend cloning this project directly from my GitHub repo,
[here](https://github.com/sundayj/JLSundayAngular/tree/PartOne-Introduction){:target="_blank"}{:rel="noopener noreferrer"},
instead of cloning the original *Tour of Heroes*. However, cloning the original *Tour of Heroes* code, then
implementing the same changes made in this project could also be a great exercise.

#### Project Structure

```bash
# This tree was printed in Windows Terminal using the 'tree' command.
# See https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/tree for more info.
├───app
│   │   app-routing.module.ts
│   │   app.component.css
│   │   app.component.html
│   │   app.component.spec.ts
│   │   app.component.ts
│   │   app.module.ts
│   │   mock-heroes.ts
│   │
│   ├───components
│   │   ├───dashboard
│   │   │       dashboard.component.css
│   │   │       dashboard.component.html
│   │   │       dashboard.component.spec.ts
│   │   │       dashboard.component.ts
│   │   │
│   │   ├───hero-detail
│   │   │       hero-detail.component.css
│   │   │       hero-detail.component.html
│   │   │       hero-detail.component.ts
│   │   │
│   │   ├───hero-search
│   │   │       hero-search.component.css
│   │   │       hero-search.component.html
│   │   │       hero-search.component.ts
│   │   │
│   │   ├───heroes
│   │   │       heroes.component.css
│   │   │       heroes.component.html
│   │   │       heroes.component.ts
│   │   │
│   │   └───snackbar-content
│   │           snackbar-content.component.css
│   │           snackbar-content.component.html
│   │           snackbar-content.component.spec.ts
│   │           snackbar-content.component.ts
│   │
│   ├───htpp-interceptor
│   │       http-interceptor.interceptor.spec.ts
│   │       http-interceptor.interceptor.ts
│   │
│   ├───models
│   │       hero.ts
│   │
│   └───services
│       ├───hero-service
│       │       hero.service.spec.ts
│       │       hero.service.ts
│       │
│       ├───in-memory-data
│       │       in-memory-data.service.spec.ts
│       │       in-memory-data.service.ts
│       │
│       ├───log-service
│       │       log.service.spec.ts
│       │       log.service.ts
│       │
│       └───snackbar-service
│               snackbar.service.spec.ts
│               snackbar.service.ts
│
├───assets
│       .gitkeep
│
├───environments
│       environment.prod.ts
│       environment.ts
│
│   favicon.ico
│   index.html
│   main.ts
│   polyfills.ts
│   styles.css
│   test.ts
│
```

#### Services

As shown above, in the Project Structure, I've moved the `hero.service.ts` and `in-memory-data.service.ts` files into
their respective folders within the `services` folder. For now, since this is a small app, I will keep all services
within this folder for better organization and to make them easier to find. Now, if the app were larger, like
Enterprise level, then I may opt to put the `heroes`, `hero-detail`, and `hero-search` components into a `hero` folder
along with the `hero-service`, whereas the more generic services would stay within a `shared/services/` folder. For now, though,
this structure will suffice.

#### Models

Like `services`, I've also created a `models` folder that will house all the app's object models. Again, this will help
with organization by keeping all similar file types together. Also like `services`, if the app were larger, I may opt to
put `models` folders within their respective components and keep a `shared/models/` folder for those more generic
models utilized throughout the app.

#### Components

Similar to `services` and `models`, I've moved all components into a `components` folder. Otherwise, the components,
along with the `models` and `services` folders would've been listed together alphabetically, and it makes more sense
to keep like with like. It also makes things easier to see in an explorer view.

## Useful Additions

The following sections give a bit of detail on the extra additions that aren't present in the original *Tour of Heroes*.
All of these additions are actually tightly coupled together and are each fired off in sequence, especially when
requesting data from a server. So, I am going to be detailing them in the order in which Angular will be utilizing them:
1. **The HTTP Interceptor** - Whenever the app makes a request to a server, or receives a response from the server, this
   interceptor does exactly as the name implies - It intercepts the call/response.
2. **The Snackbar** - Every App needs to be let its user know when an action is successful, or not, and that is where this comes in.
3. **The Log Service** - During development, and especially when debugging, logging comes in very handy. You'll see how this service can be very helpful.

### HTTP Interceptor

As stated above, the HTTP Interceptor *intercepts* any outgoing or incoming requests to a server. There can be many uses
for an HTTP Interceptor, but the main reason for the one in this project is to assist with logging, debugging, and notifying
users of completed tasks. How to implement the HTTP Interceptor into an Angular app will be covered in the next post.
For more information on Angular HTTP Interceptors, see their documentation,
[here](https://v12.angular.io/guide/http#intercepting-requests-and-responses){:target="_blank"}{:rel="noopener noreferrer"}

### The Snackbar

Now, the normal *Tour of Heroes* app makes use of a `message` service that logs simple messages to the window for the user.
While we understand that, for the sake of their tutorial, that was all that was needed for the original *Tour of Heroes*,
we also know that it is a very common scenario for a developer to want to build a notification of some kind to pass messages
to a user and that those simple messages wouldn't cut it in a production app. The third post in this series will explore
how to implement the `snackbar` to create a reusable, and modular, component that can notify users of any action taking
place throughout the app.

### Log Service

If you've ever written anything for the front-end, then surely you've used something like `console.log('Insert important note here...'')`
at some point. The log service we will be implementing will show you how to make that logging uniform and how to utilize
it the same way throughout your app, as well as printing easy-on-the-eyes and even easier to read notes.

## Final Words

Thank you for reading! Hopefully, this post has given you some idea of what to expect in the upcoming posts. You don't have
to worry about waiting too long for the next post to be published, because it is already in the works. I was honestly intending
to make this tutorial one long post, but thought better of it once I saw just how long it was becoming. So, to make it easier
on you, the reader, to not only read without falling asleep, but also to pace yourself while following along, I've decided to
break the tutorial into several posts.

Finally, as always, let me know what you think in the comments, shoot me a message through the
[Contact Me](https://jlsunday.com/about/#contact-me){:target="_blank"}{:rel="noopener noreferrer"}
form, or any of my social links in the sidebar. How do you feel about this project? Are these things that you find interesting for learning Angular?
Would you prefer that I use a different set of components? Is there a particular component, service, directive, or anything else that you'd
like me to add to these tutorials? Just let me know!

See you soon!
