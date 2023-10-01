---
layout: post
title: "Practical Usage of TypeScript Generics"
summary: A short tutorial/how-to on using TypeScript generic types for easy extensibility, and type-safe development constraints.
excerpt: A short tutorial/how-to on using TypeScript generic types for easy extensibility, and type-safe development constraints.
description: >-
    A short tutorial/how-to on using TypeScript generic types for easy extensibility, and type-safe development constraints.
    Let's say you are tasked to extend a generic UI component. The acceptance criteria for this task are:\n
    \t1. It should be easy to go to previous implementations of the original component within the code-base and implement this new functionality.\n
    \t2. It should require little to no extra development for another developer to utilize when creating new instances of the generic component.\n
    This post will show you a method for achieving this task that utilizes TypeScript's generic types.
canonical_url: https://JLSunday.com/tutorials/typescript/2022/04/22/Practical-Usage-of-TypeScript-Generics.html
categories:
    Tutorials
    TypeScript
tags:
    tutorial
    front-end
    Typescript
    how-to
    generic-types
image: https://JLSunday.com/images/other-images/undraw_design_components_9vy6.png
comments: true
last_modified_at: 2022/04/22
---

<figure style="margin-top: 20px;">
        <img alt="Design Components" src="{{ '/images/other-images/undraw_design_components_9vy6.png' | prepend: site.url }}" loading="lazy" title="Design Components">
    <figcaption>
        Image provided by <a href="https://undraw.co/search" target="_blank" rel="noopener noreferrer">unDraw.co</a>
    </figcaption>
</figure>

* TOC
  {:toc}
