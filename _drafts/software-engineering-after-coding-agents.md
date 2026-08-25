---
layout: post
title: "Software Engineering After Coding Agents"
date: 2026-08-24
description: >-
  Coding agents can already handle far more implementation work than most software careers were designed around. The useful question now is what engineers should get better at when producing code is no longer the scarce part.
categories: ["AI & Software Engineering", "Software Architecture"]
tags: [AI, Codex, Agentic Engineering, Architecture, Career, software-architecture]
comments: true
include_TOC: true
featured: false
image: /assets/images/posts/software-engineering-after-coding-agents.jpg
---

I keep seeing versions of the same argument about AI and software engineering: the models can write code now, but engineers will still be needed because somebody has to understand requirements, navigate ambiguity, make tradeoffs, debug systems, and verify the result.

That argument used to reassure me more than it does now.

The problem is that capable coding agents are getting surprisingly good at those things too. I can give an agent an ambiguous task, let it inspect a repository, and have it come back with clarifying questions, a reasonable plan, code changes, tests, and a summary of what it validated. With enough context and reasoning budget, it can navigate codebases that would have taken me hours just to map manually.

So I do not think the useful career advice is, “Don’t worry, AI can only type code.” That is already outdated.

I also do not think the opposite extreme is justified: “Software engineers are about to disappear.” The evidence is much messier than that.

The more interesting shift is this:

> **Implementation is becoming cheaper much faster than accountability is.**

That changes what engineering work is worth getting exceptionally good at.

My previous post, [Make Your Coding Agent Earn the Architecture]({% post_url 2026-08-24-make-your-coding-agent-earn-the-architecture %}), looked at one consequence of that shift from inside the repository: when implementation becomes cheap, speculative architecture becomes cheap too, so ideas need to earn their way into a system through evidence rather than plausibility. This post zooms out from the same premise. If agents can increasingly handle implementation, planning, debugging, and review, what part of the software engineer's job is actually becoming more valuable?

<div class="article-tldr">
<p class="article-tldr-title">TLDR</p>
<p class="article-tldr-deck">The Short Version</p>
<p>Coding agents are moving beyond autocomplete into sustained implementation work, and adoption is already widespread. But adoption is not the same as proven productivity, and developers remain appropriately skeptical of correctness. I think the durable engineering advantage is moving away from producing code by hand and toward defining the right problem, shaping the system around the agent, evaluating evidence, controlling risk, and owning the outcome. Engineers should learn to operate at that level instead of trying to beat a model at generating tokens.</p>
</div>

## The adoption argument is basically over

We can still debate how much AI improves engineering productivity, but “developers are not really using this stuff” is getting difficult to defend.

JetBrains' 2026 Developer Ecosystem Survey reports more than 15,000 professional developers and says 90% were using AI coding agents at work at least weekly, with 68% using them daily. Their May–July 2026 data put Claude Code at 39% usage globally and Codex at 16%. Those numbers will move quickly, but the direction is clear: coding agents have become ordinary professional tooling, not a niche experiment. [JetBrains published the adoption breakdown here](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/).

The 2025 Stack Overflow Developer Survey showed the same broader trend before agent adoption accelerated this far. Eighty-four percent of respondents were already using or planning to use AI tools in development, and 51% of professional developers reported daily use. [Stack Overflow's AI section has the full breakdown](https://survey.stackoverflow.co/2025/ai).

What I find more important is what happened to trust at the same time.

Stack Overflow found that 46% of developers distrusted the accuracy of AI-tool output while only 33% trusted it. Sixty-six percent cited solutions that were “almost right” as a major frustration, and 45% complained that debugging AI-generated code could take more time.

That combination—high adoption and low trust—looks much closer to my actual experience than either the booster or doomer version of the story.

I use coding agents heavily because the leverage is real. I also assume they can produce an internally coherent answer that is still wrong.

Those two beliefs are not contradictory. They are becoming the job.

## We should be careful with productivity numbers

There is another tempting shortcut in this conversation: take adoption, multiply it by a vendor's claimed productivity gain, and extrapolate directly to headcount.

The evidence does not support that kind of precision yet.

METR's randomized study of experienced open-source developers in early 2025 famously found that developers took roughly 19–20% longer on the studied tasks when AI tools were allowed. That result aged badly in headlines because people treated it as a permanent measurement of AI coding rather than a measurement of particular developers, models, repositories, and tasks at a particular point in time.

METR tried again as the tools improved. In February 2026, they published an update explaining that their newer experiment had become difficult to interpret because experienced developers increasingly did not want to participate if they might be assigned to work without AI. The raw results were more favorable to AI, including an estimated speedup for returning participants, but the confidence intervals were wide and selection effects were severe enough that METR explicitly called the new productivity signal unreliable. [Their explanation is worth reading because it is unusually candid about the experimental problems](https://metr.org/blog/2026-02-24-uplift-update/).

That is not evidence that AI does nothing. If anything, developers refusing to work without it is interesting evidence by itself.

It is evidence that the question “How much faster does AI make a software engineer?” is underspecified.

Faster at what?

On whose codebase?

With what model and tools?

Under what review standard?

Does the engineer know the system already?

Are we measuring the first patch, or the time until the change is actually safe to ship?

Those details matter because software engineering has never been the same thing as producing a diff.

## The scarce part of engineering is moving

For most of my career, implementation had a built-in cost. Even when the design was obvious, somebody had to type the code, wire up the tests, chase the compiler errors, run the migration, update the API, and clean up the edge cases.

That cost acted as friction.

Agents weaken it dramatically.

If I can ask for a service layer, API endpoint, migration, tests, documentation, and front-end integration and get a plausible implementation in one sustained session, then “can this be coded?” stops being a very interesting question.

The higher-value questions become:

- **Should this exist at all?**
- **Is the model solving the actual problem or a more convenient one?**
- **What invariants must remain true?**
- **What evidence would make us trust the result?**
- **What permissions should the agent have?**
- **What happens when it is confidently wrong?**
- **How expensive is the workflow when it runs at scale?**
- **Who owns the consequences after the agent is done?**

That is still engineering. In some ways it is more recognizably engineering than manually producing another CRUD endpoint.

Anthropic's Economic Index research is useful here, even with the obvious caveat that it comes from an AI vendor. Their 2026 report says Computer and Mathematical tasks represented about 35% of Claude.ai conversations, while more coding activity was moving into Claude Code and API traffic. [The report describes that migration in detail](https://www.anthropic.com/research/economic-index-march-2026-report).

The coding itself is becoming deeply integrated into AI systems. The layer around the coding agent becomes more important as a result.

## The harness is part of the software now

A coding model by itself is not an engineering workflow.

The useful system includes the repository context it can see, instructions it has to follow, tools it can call, permissions it has been granted, tests it must run, evidence it must return, cost limits, observability, retry behavior, and the boundary where a human has to approve something consequential.

That surrounding machinery is sometimes called an agent harness. I think engineers should treat it like any other production system.

A 2026 survey from Notion, Amplify, and Vercel of more than 1,000 engineers building with AI found that among respondents using agents, the share giving them write permissions had increased from 52% to 90%. Three quarters said cost affects how they use AI, and 40% said cost regularly changes how ambitious they are with it. [Their survey is here](https://www.notion.com/lp/ai-engineering-survey).

That is not prompt engineering in the narrow sense.

It is permission design, systems architecture, observability, economics, and risk management.

If an agent can modify a repository, open pull requests, run commands, touch infrastructure, or act against production systems, the engineering problem is no longer “write a really good prompt.” The problem is designing a system in which a fallible but capable worker can operate productively without being given an unlimited blast radius.

That sounds a lot like the work senior engineers already do with humans, services, queues, background jobs, deployment pipelines, and third-party integrations.

The worker is different. The engineering principles are not as different as the marketing makes them sound.

## What I would focus on if I were planning an engineering career now

I would not stop learning to code. You need enough technical depth to know when the agent is lying to you.

But I would spend less energy optimizing for raw implementation speed. Competing with a model on lines of code is a bad long-term strategy.

I would optimize for the following instead.

### 1. Learn to define problems precisely

Agents are extremely good at solving the problem they infer from the context you give them.

That is dangerous when the inferred problem is slightly wrong.

Being able to turn an ambiguous business complaint into explicit constraints, invariants, acceptance criteria, and failure cases is leverage. Better models make that skill more valuable because a clear definition can now trigger much more implementation work than it used to.

### 2. Get good at system-level reasoning

You should be able to trace how a change affects data, APIs, background work, permissions, user experience, deployment, observability, and future maintenance.

An agent can help with all of that. You still need the mental model required to challenge its assumptions.

The easiest AI mistake to miss is not broken syntax. It is a clean implementation of the wrong architecture.

### 3. Treat verification as a first-class engineering discipline

Tests matter more when generating code is cheap.

So do reproducible commands, static analysis, contract checks, database constraints, evals, preview environments, telemetry, and explicit evidence gates.

If your workflow ends with “the agent says it works,” you do not have an engineering workflow.

### 4. Learn how to give agents bounded autonomy

The productive question is not whether an agent should be autonomous.

It is autonomous **where, with what permissions, under what constraints, and with what rollback path?**

Reading a repository is different from merging to `main`. Drafting a database migration is different from applying it in production. Suggesting a blog post is different from publishing under someone's name.

Good agentic systems make those distinctions explicit.

### 5. Understand the economics

Reasoning models, parallel agents, long context windows, browser automation, hosted sandboxes, and repeated verification all cost money and time.

A workflow that is impressive at $40 per task may be useless when run 5,000 times a month.

Engineers who can decide where expensive reasoning is justified—and where a deterministic script is better—will have an advantage over teams that throw the largest model at every problem.

### 6. Own outcomes instead of artifacts

The engineer who says “I finished my ticket” is easier to replace than the engineer who understands why the feature exists, knows whether it helped, notices when the surrounding system is deteriorating, and can decide what should happen next.

AI makes artifact production cheaper. It does not make ownership cheap.

## The junior-engineer problem worries me more than the senior-engineer problem

There is an uncomfortable edge case here.

A lot of the work agents are best at is the work we historically gave junior engineers so they could become senior engineers.

Small bug fixes. Straightforward endpoints. Test coverage. Mechanical refactors. Documentation. Following an established pattern through the stack.

If companies decide that work no longer justifies a junior hire, they may save money in the short term and quietly damage the pipeline that creates experienced engineers.

Senior judgment is not downloaded at promotion time. It is accumulated by making mistakes, reviewing code, operating systems, debugging ugly failures, and seeing how apparently reasonable decisions age.

I do not know what the new apprenticeship model should look like, but “the agent handles all the easy work and humans begin at senior” is not a serious answer.

One possibility is that junior engineers should use agents aggressively while being evaluated less on implementation volume and more on whether they can explain, test, critique, and improve what the agent produced. That could compress some kinds of learning rather than eliminate them.

But organizations will have to design for that deliberately.

## I do not think the engineer disappears; I think the center of gravity moves

The models will keep getting better at tasks people currently use as proof that software engineers are indispensable.

They will understand larger repositories. They will ask better questions. They will debug more effectively. They will operate tools for longer. They will coordinate with other agents. They will get better at reviewing their own work.

I would not build a career plan around the assumption that there is some comfortably human engineering task AI will never touch.

I would build it around a different assumption:

**As capability rises, the person who can decide what deserves to be built, shape the environment in which agents work, detect when the result is wrong, and take responsibility for the system becomes more leveraged—not less.**

That is a different job from the software engineer many of us trained to be.

I think it is still software engineering.

And I think pretending nothing fundamental is changing is much riskier than learning how to do the changed version of the job well.
