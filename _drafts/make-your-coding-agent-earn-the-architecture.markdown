---
layout: post
title: "Make Your Coding Agent Earn the Architecture"
description: "Evidence-Gated Capability Adoption is the workflow I use to keep coding agents from turning plausible ideas into permanent architecture before the evidence justifies it."
categories: [Software Engineering, AI]
tags: [AI, Codex, Agentic Engineering, Architecture, EGCA]
---

Coding agents have changed one of the constraints I used to rely on without realizing it.

A few years ago, a speculative architecture had a built-in cost. If I wanted a new model, service layer, migration, API, orchestration engine, test harness, and supporting abstractions, somebody had to spend a meaningful amount of time building all of it. That effort was annoying, but it also created friction. An idea had to seem useful enough to justify the work.

With a capable coding agent, that friction is much weaker.

I can describe a problem, let the agent inspect the repository, and get a surprisingly complete architecture back quickly. That is one of the reasons I use agents so heavily. It also creates a new failure mode: **a plausible architecture can become real code before anyone has proven that the architecture was necessary.**

I started noticing this while working on my own projects and eventually at work. The recurring pattern was not that the agent wrote obviously bad code. The proposals were often internally coherent. They solved the problem as described. The issue was that they sometimes solved a larger problem than the repository actually had.

That distinction matters. Once unnecessary architecture exists, its implementation may have been cheap, but its maintenance is not.

The workflow I ended up developing to deal with this is something I now call **Evidence-Gated Capability Adoption**, or EGCA. The name is new; most of the ideas behind it are not. It combines hypothesis-driven development, technical spikes, evolutionary architecture, decision records, and a few lessons that became much more important once agents started doing sustained repository-scale work.

The central rule is straightforward:

> A new capability or abstraction does not earn a place in the architecture because it sounds reasonable or because an agent can implement it. It earns that place when evidence survives an explicit gate.

## The PaySpan feature that made the problem obvious

One of the clearest examples came from PaySpan, a private personal-finance application I have been building and using as a proving ground for agent-assisted development.

I was adding better support for accounts that had fallen behind. The problem looked substantial. Arrears can affect due amounts, payment history, scheduling, catch-up planning, and how the system distinguishes an ordinary upcoming bill from debt that has accumulated over time.

The first architectural instinct was correspondingly substantial. The agent explored adding dedicated arrears models and a separate engine responsible for managing them.

That proposal was not absurd. If I had asked for an implementation directly, I suspect the resulting code would have been clean enough and probably would have worked.

Instead, I ran the problem through the experimental workflow I had recently started using.

The baseline investigation changed the shape of the problem. PaySpan already had a mature ledger for payments, charges, reversals, statuses, occurrences, and catch-up planning. The first bounded experiment showed that most of the behavior could be represented using those existing primitives with a much narrower distinction than the proposed subsystem required.

A later experiment was even more useful. We assumed the existing catch-up planner would need production changes to become arrears-aware. The experiment found that the behavior we needed was already supported once the inputs were represented correctly.

**Zero production-code changes were required for that part of the feature.**

That is the moment the methodology became much more interesting to me.

The experiment did not merely produce a better implementation. It stopped us from building an implementation that did not need to exist.

## Put the burden of proof on the abstraction

EGCA treats architecture proposals as candidates rather than commitments.

The lifecycle looks like this:

```text
Candidate
   ↓
Investigate
   ↓
Hypothesize
   ↓
Smallest useful experiment
   ↓
Evidence
   ↓
Adopt / Adapt / Reject / Repeat
   ↓
Record
```

Those states sound obvious when written down. In practice, coding agents can move through them so quickly that they blur together.

A useful idea becomes a proposed implementation. A proposed implementation becomes a branch. The tests pass, so the branch starts to look like evidence that the idea was correct. A few iterations later, the architecture is permanent and nobody quite remembers which assumptions were ever tested.

The workflow forces a harder question at each transition.

A **candidate** asks whether an idea might be valuable.

An **investigation** asks how the current system and any source implementation actually work. This is where I want the agent reading the repository rather than designing from the prompt alone.

A **hypothesis** states the expected improvement in falsifiable terms. It also records what evidence would count against the idea before implementation starts.

The **smallest useful experiment** is the cheapest bounded change that can answer the architectural question. It exists to reduce uncertainty before more architecture accumulates.

Then comes the part I care about most: the evidence gate.

The outcome must be allowed to be **Adopt, Adapt, Reject, or Repeat**. If every experiment eventually becomes "Adopt," there is no meaningful gate. There is only a slower implementation process.

## Isn't this just normal software development?

Mostly, yes.

Experienced engineers have always formed ideas, tried things, learned from bugs and constraints, and adjusted designs as they went. Hypothesis-driven development, Lean, technical spikes, evolutionary architecture, and decades of ordinary engineering practice already cover that territory. If EGCA were simply a renamed version of "iterate on your code," the name would deserve the eye roll.

The part I found useful enough to make explicit is narrower: **separating an architectural candidate from an implementation commitment and requiring evidence before promoting it into the architecture.**

That distinction is easy to handle implicitly when one engineer is carrying the reasoning in their head. It becomes much easier to lose when an agent can turn an architectural suggestion into a convincing implementation before the underlying assumption has been challenged.

Consider the arrears example again. A normal iterative path could have looked like this:

```text
"Arrears probably needs its own subsystem"
          ↓
Start building the subsystem
          ↓
Models, services, migrations, APIs, tests
          ↓
Learn from the implementation
          ↓
Refactor, simplify, or remove pieces
```

That is legitimate iterative development. It might eventually converge on the same answer.

EGCA moves the expensive learning question earlier:

```text
"Arrears may need its own subsystem"
          ↓
Record it as a candidate
          ↓
Inspect the existing system deeply
          ↓
Hypothesis: existing primitives may already cover most of it
          ↓
Run the smallest experiment that can answer that question
          ↓
Evidence: most of the proposed subsystem is unnecessary
          ↓
Never build it
```

The gain is not the existence of iteration. The gain is **moving iteration upstream of architectural commitment**.

A few rules make that boundary more concrete:

- A candidate is allowed to remain merely interesting. It does not automatically become backlog work.
- Rejection is a successful experimental outcome when it prevents unjustified complexity.
- Where practical, rejection criteria are written before implementation so the same agent cannot quietly redefine success after seeing the result.
- Implementation momentum is not treated as proof that the original idea was good.
- The reasoning is preserved in durable state so another engineer or agent can understand why an idea was adopted, adapted, deferred, or deliberately never built.

That last point matters more than I expected. A repository shows what exists. It is much worse at showing the architectures that were considered and rejected, or the evidence that made the team stop. Humans often carry that history informally. Agents make that implicit memory much less reliable across sessions.

So I do not think EGCA replaces ordinary iterative development. It formalizes a hesitation experienced engineers already practice before turning a plausible idea into permanent architecture. Coding agents made that hesitation worth making explicit.

## Sometimes the abstraction earns its way in

I also do not want the method to become a philosophy of "always write less code."

A workplace use of EGCA gave me a useful counterexample.

The work began with a real production support regression involving financial semantics across several state-specific document generators. The obvious long-term concern was duplicated mapping logic. It would have been easy to jump from the bug directly into a broad typed configuration or policy registry.

We started by characterizing the actual regression and isolating two narrower problems. Once those were understood, a later experiment tested whether a shared typed financial-bucket abstraction reduced the risk without forcing a general registry across every state.

That smaller abstraction held up across multiple independently verified paths, so it earned adoption.

The broader policy registry did not. Several states still had semantics that had not been verified well enough to encode into a universal abstraction. That part stayed deferred.

This is an important property of the method. EGCA is biased toward **justified architecture**, whether the evidence leads to less structure or a carefully bounded new abstraction.

In PaySpan, evidence removed architecture. In the workplace case, evidence justified a narrow abstraction while continuing to defer a larger one.

That is exactly what I want from the gate.

## Durable state turned out to be just as important as the experiments

The experimentation itself was only half of the breakthrough.

The other half was keeping the state of the work somewhere both I and the agents could inspect and modify over time.

Long-running agent work has several kinds of state that are easy to conflate:

- **Repository truth:** what code and behavior exist right now.
- **Project decision state:** what we are researching, what hypotheses exist, what has been tested, and why decisions were made.
- **Agent memory:** context an agent retains across conversations or sessions.
- **Runtime checkpoints:** where a long-running execution can resume after interruption.

Those are different problems.

I do not want a spreadsheet or a Markdown tracker duplicating the repository. The repository remains authoritative for current code. The tracker records the information Git does not naturally explain: why E-004 exists, which assumption it tests, what would falsify it, what E-002 taught us, and why a capability was adapted instead of adopted.

Stable experiment IDs also matter more than I expected. If `E-007` suddenly becomes more important than `E-003`, I change priority or dependencies. I do not renumber history. That keeps decisions and evidence referentially stable for both humans and agents.

## Google Sheets was useful. It was not the methodology.

My first EGCA trackers lived in Google Sheets.

That choice was extremely practical. I could inspect and edit the tracker manually, ChatGPT could work with it through connected tools, and Codex could use it as persistent project state during a long-running goal. Tables made dependencies, evidence, status, and decisions easy to scan.

For a while, I thought the interesting part of the workflow might be "use a spreadsheet as long-term memory for coding agents."

Then I used EGCA at work with a Git-tracked Markdown tracker instead.

The methodology survived just fine.

That clarified the boundary for me. **EGCA is the process. The storage layer is an adapter.**

Google Sheets is a good adapter when humans and heterogeneous agents all need convenient read/write access and tabular views. Git-tracked Markdown or YAML is attractive when versioning, portability, and repository-local operation matter more. A project tracker or a database behind an API/MCP server may be a better fit for larger teams or concurrent agents.

Agent memory systems and runtime persistence can complement any of those, but they solve different problems.

## The public test: JLSunday and DevSculptor

The most useful case study is also the easiest one to inspect because the repositories are public.

[JLSunday](https://github.com/sundayj/sundayj.github.io) is this site's repository. [DevSculptor](https://github.com/sundayj/devsculptor) is the reusable Jekyll theme/site project it consumes. I used EGCA to modernize both together, with a shared tracker holding the investigation and experiment state.

That run produced several outcomes I would not have predicted from the initial plan.

One early experiment, `JE-001`, started from a plausible assumption about duplicated metadata ownership. The result was **Adapt** rather than a clean confirmation. The experiment proved some metadata was duplicated, but it also showed that the SEO plugin did not own every field we initially assumed it did.

Even the evidence harness failed usefully. A validation step initially reported a problem because the validator itself contained a bad assumption. Fixing the harness became part of the learning rather than being mistaken for evidence against the architecture.

Other items bypassed experimentation entirely. Once the existing code and generated output provided enough evidence, running a formal spike would have been ceremony. EGCA should add friction where uncertainty exists rather than manufacture uncertainty so the process has something to do.

The Algolia/search work became another good example. Peeling away wrapper actions, theme behavior, and repository responsibilities progressively changed our understanding of where indexing belonged. The eventual answer went beyond "fix the failing action." Part of the responsibility did not belong in the reusable theme at all.

Cross-repository validation mattered too. A theme can look correct in isolation and still fail at its consumption boundary. We tested DevSculptor changes against JLSunday using the exact theme commit that would be consumed, rather than assuming a green theme repository meant the integrated system was safe.

Human review still caught things CI did not. That should be unsurprising, but it is worth stating because an evidence gate can become dangerously self-referential if the same agent designs the experiment, implements it, chooses the metric, and declares the result successful.

The public run also changed EGCA itself. Branch hygiene, cumulative integration, and some of the tracker rules became more explicit because the experiments exposed weaknesses in the methodology.

That feedback loop is now part of the design:

```text
Skill
  ↓
Real project
  ↓
Friction or failure
  ↓
Case-study evidence
  ↓
Methodology change
  ↓
Skill revision
```

## Keep experimental success away from production until the program is ready

One of the larger changes that emerged from those runs was the branch model.

A successful local experiment does not prove the whole capability program is ready to ship. If every accepted experiment merges directly into `main`, the evidence gates become piecemeal production releases.

The structure I now prefer is:

```text
main
  └── feature/<egca-program>
        ├── experiment/e-001-...
        ├── experiment/e-002-...
        ├── adaptation/e-002-...
        └── experiment/e-003-...
```

Experiments branch from the cumulative EGCA feature branch. Adopted or adapted work returns to that branch. Rejected experiments remain evidence and stay out of the candidate architecture.

The feature branch is the cumulative architecture we are evaluating. Only after the program-level evidence gate passes does it become a normal production candidate.

This became especially important when later experiments depended on earlier accepted work or when evidence changed the interpretation of an earlier decision.

## EGCA has plenty of ways to fail

Any process that makes architecture more deliberate can become architecture bureaucracy.

That is the strongest objection to EGCA, and I think it is correct for the wrong-sized problem.

A typo does not need a hypothesis. An obvious dependency bump probably does not need a candidate backlog. If the team already has strong production evidence and an approved implementation path, forcing an experiment can add paperwork without reducing uncertainty.

Small experiments can also create false confidence. A benchmark that passes on a curated corpus may say very little about production. A metric can become a target. Easy-to-measure qualities can crowd out maintainability, operator experience, or domain correctness. A coding agent can unconsciously construct an experiment that confirms its own preferred design.

The mitigations are mostly procedural:

- use EGCA when meaningful uncertainty exists;
- define rejection evidence before implementation;
- prefer repository, runtime, and user evidence over agent self-report;
- keep a human review boundary for consequential decisions;
- record environment-blocked validation separately from a failed hypothesis;
- allow direct implementation when the evidence already exists.

The method should reduce speculative architecture without wrapping every change in ceremony.

## This is a synthesis, not a new scientific method

I gave the workflow a name because I needed a way to reproduce it across repositories and agents. The useful part is the explicit promotion boundary and durable state, not a claim that experimentation itself is new.

The closest lineage includes **Hypothesis-Driven Development**, the scientific method as applied to engineering, Lean's Build-Measure-Learn loop, technical and architectural spikes, Continuous Architecture, evolutionary architecture and fitness functions, Real Options/last-responsible-moment thinking, and Architecture Decision Records.

Each contributes something important.

The specific combination I care about is narrower: evaluating whether a capability, external idea, dependency, or abstraction deserves adoption into an existing system while coding agents are capable of implementing the idea very quickly.

EGCA adds an operational shape around that problem: source investigation, falsifiable hypotheses, predeclared evidence gates, stable experiment identities, durable human/agent state, explicit Adopt/Adapt/Reject/Repeat outcomes, and cumulative integration isolation.

I have not found an established methodology that matches that entire workflow closely enough that using its name would be more accurate than describing EGCA as a synthesis.

## A practical starter version

You do not need my tracker to try the idea. A minimal EGCA run can fit in a Markdown file.

For each substantial capability:

1. **Establish the baseline.** Inspect what the system already does before designing anything new.
2. **Capture the candidate.** Record the idea without treating it as approved work.
3. **Investigate.** Study the current repository, source implementation, alternatives, and constraints.
4. **Write a falsifiable hypothesis.** Include what evidence would weaken or reject it.
5. **Design the smallest useful experiment.** Change only enough to answer the architectural question.
6. **Record actual evidence.** Tests, runtime behavior, UX, performance, review findings, or domain validation.
7. **Choose Adopt, Adapt, Reject, or Repeat.** Keep the decision tied to the evidence gathered.
8. **Integrate accepted work on a cumulative candidate branch.** Keep experiments away from production until the program is ready.
9. **Record the decision.** Preserve the reasoning so another human or agent does not have to reconstruct it.
10. **Run a final program-level gate.** Validate the cumulative architecture before it reaches the production branch.

A lightweight tracker might include:

```text
Candidate ID
Problem / opportunity
Current status
Source investigation
Hypothesis
Experiment ID
Experiment scope
Success evidence
Rejection evidence
Observed evidence
Decision: Adopt / Adapt / Reject / Repeat
Dependencies
Branch / PR
Decision rationale
Next action
```

And the corresponding agent instruction can be surprisingly small:

```text
Use the Evidence-Gated Capability Adoption workflow for this initiative.
Treat the repository as the source of truth for current behavior and the tracker
as durable research/decision state. Do not assume the proposed capability should
be adopted. Establish the baseline, investigate existing primitives, and design
the smallest experiment that can falsify or support the current hypothesis.
Update evidence and decisions as the work progresses. New abstractions must be
justified by observed evidence before they enter the cumulative feature branch.
```

I have packaged the fuller workflow as a public, reusable Agent Skill in the [EvidenceGatedCapabilityAdoption repository](https://github.com/sundayj/EvidenceGatedCapabilityAdoption). The skill is intentionally still evolving. Some of its current rules exist because real uses exposed failures in earlier versions, including a broken installation package, ambiguous experiment integration, and validation states that were too coarse.

That is probably appropriate for a methodology built around evidence.

## Implementation is cheap now. Architecture still is not.

I do not want coding agents to become slower. Their speed is the point.

What I want is to spend more of that speed on learning before speculation hardens into a permanent design.

An agent can produce a convincing architecture in minutes. That no longer tells me whether the architecture deserves to exist.

**Implementation cost is no longer a reliable filter for whether an architectural idea deserves to exist. Evidence can be.**
