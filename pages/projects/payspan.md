---
layout: project-case-study
project: payspan
title: PaySpan
description: A self-hosted cash-flow planning and bill-reconciliation system built around real pay periods, statement evidence, and deterministic financial workflows.
permalink: /projects/payspan/
---

## Why I built it

Most budgeting software starts from categories and monthly envelopes. That is useful for many people, but it did not match the problem I was trying to solve.

The difficult question in my household was more operational: **given the next paycheck, the bills that actually need to be funded, the payments that may already be in flight, and the money currently available, what can safely be spent?**

That question becomes surprisingly hard when due dates drift, statement amounts change, bills are paid from different accounts, payments clear on different days, and the source of truth is scattered across bank transactions, email, PDFs, provider websites, and memory.

I started PaySpan to make that state explicit. It is a self-hosted cash-flow planning application that models income, bills, occurrences, payments, and imported evidence over time. The goal is not to replace every budgeting tool; it is to reduce the repeated reconciliation work required to understand what is due, what is already paid, what still needs funding, and whether the current pay period is actually healthy.

## Modeling the problem around pay periods

The core domain deliberately separates a recurring bill from a specific instance of that bill.

A `BillAccount` represents the continuing obligation. A `BillOccurrence` represents one concrete due date and amount. Income is modeled through `IncomeStream` and instantiated into `PayPeriod` records. That distinction matters because a mortgage, utility bill, subscription, or loan may be recurring while the amount, due date, payment state, and supporting evidence for each occurrence are not.

PaySpan then assigns bill occurrences to the paycheck that needs to fund them. A funding deadline can account for buffer days, and larger expenses can be spread across multiple pay periods through sinking-fund behavior. The result is a paycheck-oriented model rather than a monthly snapshot.

That model powers values such as reserved-for-bills, expected income, discretionary targets, and safe-to-spend calculations. More importantly, it gives the rest of the application a stable vocabulary for answering reconciliation questions.

## The Funding Plan as a decision surface

The Funding Plan became the canonical planning workspace rather than another dashboard of disconnected totals.

It brings together upcoming pay periods, bill obligations, funding pressure, adjustments, imported financial data, and plan-health signals. When a period is overloaded, the application can surface that pressure directly instead of leaving the user to infer it from several screens.

Two features grew from that model:

- **Smart Rebalance** helps redistribute bill funding when the current allocation creates unnecessary pressure in one pay period.
- **Catch-Up Plan** explores how to recover when upcoming obligations exceed the money realistically available, instead of merely showing that a period is negative.

The design principle is important to me: the system should not just report a problem. It should preserve the underlying financial constraints and help reason about the next practical action.

## Reconciliation is an evidence problem

One of the hardest parts of personal finance software is that the application's database is not automatically the truth.

A bill may say one thing, a bank transaction another, and an email statement may contain the newest amount or due date. PaySpan treats those inputs as evidence that must be reconciled rather than blindly imported.

The ingestion pipeline can poll configured email accounts asynchronously, persist messages and attachments, normalize HTML email, parse PDF statements, and extract bill information such as due dates and amounts. PDF parsing uses deterministic extraction first, and ambiguous results can be routed into review workflows instead of silently becoming trusted financial state.

This is also why PaySpan has explicit concepts for trust, confidence, and review. Messages can be evaluated using sender-domain rules and authentication results such as SPF, DKIM, and DMARC. Parsed data that cannot be matched confidently can create a low-confidence placeholder rather than pretending the system knows more than it does.

That approach makes the application more complicated than a simple importer, but it matches the real problem: **financial automation is only useful when I can understand why the application believes something is true.**

## Importing without losing provenance

Transaction and statement import has evolved toward a ledger-style architecture with reconciliation as the final step rather than import as the final step.

The important distinction is between acquiring data and deciding what that data means. PaySpan can ingest statements or transactions, deduplicate them, associate them with accounts and bill occurrences, and retain enough provenance to inspect how an imported record affected the plan.

This becomes especially important when a payment has already been recorded manually, a bank transaction arrives later, or multiple sources describe the same event differently. The system needs to recognize that those records may be evidence of one payment rather than three independent financial events.

That architecture is still evolving, but it has become one of the central design constraints of the project: imports should improve confidence in the plan without making the plan less explainable.

## Backend architecture

PaySpan uses Django as the domain and application core, with Django REST Framework exposing a versioned API under `/api/v1/`.

The backend includes:

- Django models and services for bills, occurrences, pay periods, payments, imports, alerts, and reconciliation;
- PostgreSQL for relational persistence;
- Celery and Redis for asynchronous ingestion and scheduled work;
- a REST API with filtering, pagination, and JWT authentication for SPA clients;
- generated or factory-driven CRUD plumbing where straightforward resources do not justify repetitive serializer and viewset code.

I have intentionally kept financial calculations and state transitions in deterministic application services. AI can assist with interpretation or automation, but it should not become an opaque replacement for the domain rules that determine whether money is actually available.

## Angular as the primary application UI

The current frontend is an Angular SPA backed by the Django API.

Moving the user-facing workflow into Angular created a clearer separation between presentation and domain behavior, while still keeping the Django admin and server-side tooling useful for inspection and maintenance. JWT authentication supports the SPA, while Django session authentication remains useful for administrative interfaces.

The frontend work has increasingly focused on reducing the number of screens a user needs to mentally reconcile. Funding, bill occurrence state, imported transactions, and payment evidence are most valuable when they can be viewed in context rather than as isolated CRUD resources.

## Trust, alerts, and failure handling

PaySpan is deliberately conservative about silent automation.

Examples include:

- suspicious or failed email authentication forcing messages into an untrusted state;
- parsed statements that cannot be matched confidently entering review queues;
- bill amount or due-date anomalies generating warnings;
- overloaded pay periods surfacing alerts instead of allowing a negative funding state to disappear into a table;
- missing statement details remaining visibly unresolved rather than being replaced by invented values.

The pattern is consistent: when confidence drops, the application should expose uncertainty and preserve evidence.

## Where AI and agents fit

PaySpan predates some of the current agent tooling, but agentic automation is now one of the most interesting directions for the project.

The opportunity is not simply to add a chatbot. The high-value workflow is to let an agent help gather and reconcile evidence across systems: inspect a bill provider, compare its latest amount and payment history with bank transactions, identify the relevant bill occurrence, and prepare a proposed reconciliation with supporting evidence.

The constraint is equally important. A financial agent should not be allowed to quietly mutate trusted state because it produced a plausible answer. I want agent-assisted workflows to operate through explicit capabilities, bounded permissions, provenance, and review gates where the consequence warrants them.

That direction is one reason I have been applying **Evidence-Gated Capability Adoption** to PaySpan. New integrations and agent capabilities can be evaluated as bounded experiments before becoming permanent architecture.

## Engineering lessons

PaySpan has reinforced several lessons that generalize beyond personal finance software.

### The domain model matters more than the dashboard

Once bills, occurrences, payments, pay periods, and evidence are modeled correctly, many UI features become projections of the same state. When those concepts are blurred together, every new screen creates another reconciliation problem.

### Automation without confidence is technical debt

An importer that is wrong 5% of the time can create more work than a manual workflow if the user cannot tell which 5% is wrong. Provenance, review queues, confidence states, and deterministic reconciliation rules are product features, not just implementation details.

### The hardest workflows cross system boundaries

The remaining friction is rarely inside one database table. It is between a billing portal, an email statement, a PDF, a bank transaction, and the application's current state. That makes orchestration, browser automation, secure credential access, and agent tooling increasingly relevant to the project's future.

### AI is most useful when the deterministic core is strong

The more clearly the application defines its entities, invariants, APIs, and evidence model, the more safely an agent can operate around it. A strong deterministic core does not compete with AI; it gives AI a safer operating surface.

## Current direction

The project is still active and intentionally evolving.

Current work is centered on reducing reconciliation friction further: improving transaction import architecture, making bill-payment matching more reliable, refining Funding Plan behavior, and testing how agentic workflows can gather external bill evidence with as little manual intervention as practical.

The long-term goal is a system that can continuously assemble the evidence needed for a trustworthy cash-flow plan while still making every important conclusion inspectable.

<!-- CI-016 follow-up: add curated screenshots for Funding Plan, reconciliation/bill occurrence workflow, transaction/import workflow, and one representative overview. Use demo/scrubbed data only. -->
