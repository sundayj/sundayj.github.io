---
layout: post
title: "Your Parser Shouldn't Get One Shot"
summary: >-
  A resilient parser should classify the failure mode, choose the cheapest recovery strategy that fits it, validate the result, and preserve uncertainty instead of treating one extraction attempt as truth.
excerpt: >-
  Parsing messy documents is rarely a one-shot problem. A more reliable design is a failure-mode-aware cascade that combines deterministic extraction, OCR, layout-aware recovery, semantic fallback, domain validation, and human review.
description: >-
  A practical look at resilient parser architecture, using a Reddit resume-parser discussion and lessons from a private financial application to examine redundancy, OCR, layout-aware extraction, LLM fallback, confidence, and replay.
canonical_url: "https://jlsunday.com/software-development/2026/08/23/your-parser-shouldnt-get-one-shot.html"
category: "Software Development"
tags: [parsing,ocr,software-architecture,pdf,ai]
image: "https://jlsunday.com/assets/images/posts/parser-redundancy-social.svg"
comments: true
date: 2026-08-23
last_modified_at: 2026-08-23
author: {{ site.author.name }}
include_TOC: true
featured: false
sort: 0
---

<figure style="margin-top: 20px;">
  <img alt="A resilient parser pipeline moving from native text extraction through validation, recovery, review, and a trusted result" src="{{ '/assets/images/posts/parser-redundancy-social.svg' | prepend: site.url }}" title="Your Parser Shouldn't Get One Shot">
</figure>

[A Reddit post about resume parsing](https://www.reddit.com/r/resumes/comments/1vv5c63/i_parse_resumes_for_a_living_here_is_what_broke/){:target="_blank"}{:rel="noopener noreferrer"} caught my attention recently because the problem was familiar even though the domain wasn't. The author had built a resume parser intended to show job seekers what an applicant tracking system might actually see. The failures were the usual ugly document-processing problems: tables flattened into nonsense, two-column layouts read in the wrong order, punctuation mangled, fields dropped, and scanned PDFs with no useful text layer at all.

I replied that my instinct would be to add redundancy. If ordinary text extraction fails, try OCR. If the extracted text exists but clearly doesn't make sense, try another strategy. If deterministic parsing still can't resolve the document, use a semantic model as a bounded fallback. Keep the original artifact around, record what failed, and use that evidence to improve the system later.

The original poster pushed back for a good reason: their product is trying to approximate what an employer's ATS sees. If a resume breaks in Workday, silently recovering the missing information could make the diagnostic less accurate.

That exchange clarified something I had been thinking about while working on document ingestion in one of my own private projects. Parser redundancy is useful, but only when **recovery is actually the product goal**. And when it is, the right design is not "keep trying increasingly powerful parsers until one returns something." It is a failure-mode-aware pipeline in which each fallback exists for a specific reason.

## Text extraction is not document understanding

One of the easiest mistakes to make in document ingestion is treating non-empty text as success.

A PDF parser may return hundreds or thousands of characters and still have destroyed the information your application cares about. A bank-statement table can become a stream of dates, descriptions, amounts, and balances in the wrong order. A two-column document can be flattened line-by-line across both columns. Characters can survive while relationships between them disappear.

That gives us at least two very different questions:

1. **Did I extract text?**
2. **Did I preserve enough structure and meaning to use it safely?**

The first is an extraction question. The second is a validation question.

Production systems need both.

This is especially important in domains where plausible-looking wrong data is worse than an explicit failure. Amazon Textract's own best-practices documentation makes this distinction operationally: it returns confidence scores and recommends stricter thresholds, or human scrutiny, for workflows where incorrect detections have higher consequences. Financial processes are one of the examples Amazon gives for using a much higher threshold than low-risk archival use.

Source: [Amazon Textract best practices](https://docs.aws.amazon.com/textract/latest/dg/textract-best-practices.html)

A parser should therefore be able to say more than "I got text." It should have some way to decide whether the result is credible enough to continue.

## Different failures deserve different fallbacks

The useful way to think about parser redundancy is as a taxonomy of failure modes.

### No usable text layer

This is the straightforward OCR case. The PDF is effectively an image, or the embedded text is absent.

OCR exists specifically to recover from that class of failure. Running OCR first on every document is usually wasteful: born-digital PDFs already contain better text than OCR can reconstruct, and rasterizing them can introduce new errors.

OCRmyPDF's behavior illustrates this nicely. Its default handling is deliberately cautious around pages that already contain text. It also provides distinct modes for skipping existing text, redoing an old OCR layer, or forcing rasterization when the current text layer is damaged. Those are different recovery strategies because "no text," "bad OCR," and "broken character mapping" are different problems.

Source: [OCRmyPDF advanced features](https://ocrmypdf.readthedocs.io/en/stable/advanced.html)

### Text exists, but layout was lost

OCR alone may not help here. The text itself can be perfectly recognizable while the table, columns, headers, or reading order are gone.

This is where layout-aware extraction becomes useful.

The open-source Unstructured project exposes several PDF partitioning strategies: `fast`, `hi_res`, `ocr_only`, and `auto`. Its fast path uses traditional text extraction; `ocr_only` exists for image-based documents; and `hi_res` performs layout detection so document elements can be classified with more structural information. The automatic strategy chooses among these based on document characteristics and requested behavior.

That is much closer to how I think robust ingestion should work: **route based on the failure you have, not on a universal ranking of parsers**.

Unstructured's documentation even calls out cases where the more expensive layout strategy is not automatically better. Multi-column ordering can favor OCR-only in some image-based documents. A later, more sophisticated stage is not an oracle.

Sources: [Unstructured partitioning strategies](https://docs.unstructured.io/open-source/concepts/partitioning-strategies) and [partitioning documentation](https://docs.unstructured.io/open-source/core-functionality/partitioning)

### The source is known, but the format is idiosyncratic

Sometimes a generic document model is unnecessary. If you know the source and understand its format, a specialized deterministic parser can be cheaper, faster, easier to reproduce, and easier to regression-test than an AI model.

This is an area where I think "just send it to an LLM" is often the wrong first instinct.

If a statement format has stable markers, row shapes, or section boundaries, encode that knowledge. A source-specific parser gives you very predictable failure behavior. When the format changes, you get a failing test or a parse warning instead of a model quietly inventing a plausible interpretation.

The cost is maintenance. Enough special cases can become a parser zoo. That is another reason to keep fallback strategies explicit and observable instead of scattering them through unrelated code paths.

### The structure is present, but the meaning is ambiguous

This is the point where semantic models become interesting.

An LLM or vision-language model can be useful when the document contains the necessary evidence but deterministic rules cannot confidently map it into the application's domain model. That does **not** mean the model should become authoritative.

A safer design is to let the semantic layer propose a structured candidate, then validate that candidate against things the application already knows:

- required fields;
- valid date ranges;
- arithmetic relationships;
- expected account or document state;
- duplicate detection;
- cross-document consistency;
- source evidence.

If the candidate fails those checks, the system should reject it, retry under a bounded policy, or ask for review.

The LLM is an interpreter, not the source of truth.

## A private financial application as a case study

I have been applying versions of this pattern in a private financial application I maintain. I don't plan to publish the repository or the personal data it processes, but the architecture is general enough to discuss without exposing either.

The application ingests financial documents and transaction data from multiple formats. Its preferred path is deterministic because deterministic parsing is cheap, reproducible, and straightforward to test. When a PDF has no useful text layer, OCR is available as a bounded fallback rather than the default. Known statement shapes can be routed to specialized parsers, and the output is not accepted merely because a parser produced rows.

The important part is what happens after extraction.

Parsed candidates are compared with domain state. Amounts, dates, balances, existing transactions, and other evidence provide constraints that a parser working in isolation does not have. Ambiguous results can be surfaced for review rather than silently promoted into canonical financial data.

This architecture has evolved because of real failures. A parser that works on ten statements can still meet an eleventh that exposes a bad assumption. When that happens, the most valuable artifact is not only the fix. It is the failed case and the regression test that prevents the same assumption from returning later.

That leads to another form of redundancy that is easy to overlook: **temporal redundancy**.

The system should preserve enough evidence to reinterpret yesterday's failure using tomorrow's parser.

## Preserve the artifact and the failure

A brittle ingestion pipeline often throws away exactly the information needed to improve it.

The document arrives. Parsing fails. The system returns an error. The user tries something else. Later, an engineer sees a generic "could not parse" metric with no way to reproduce the failure.

A better pipeline retains, subject to the privacy and retention requirements of the domain:

- the original artifact or a reproducible reference to it;
- which parser strategy was attempted;
- warnings and confidence information;
- structured candidates that were rejected;
- validation failures;
- any human correction that resolved the ambiguity.

That turns parser failures into a corpus of real edge cases.

The next parser version can be replayed against them. A newly introduced fallback can be measured against old failures. A source-specific rule can be justified by evidence instead of intuition.

Of course, keeping documents creates its own responsibilities. Resumes contain personal information. Financial statements contain even more. Retention, encryption, access control, and deletion policies have to be part of the architecture. "Keep everything forever because it might help debugging" is not a responsible default.

## Confidence is a routing signal, not a magic number

Machine-learning document systems often expose confidence scores, but I would be cautious about treating those scores as universal probabilities of correctness.

Their most useful role is often routing.

A result above a carefully tested threshold may qualify for straight-through processing. A result below it may need another parser or human review. A result that violates a hard domain invariant should be rejected regardless of how confident the extraction model claims to be.

This is also why confidence thresholds should be tuned using representative data rather than selected because 90 or 95 "sounds safe." The consequences of an error determine what threshold is acceptable, and different fields may deserve different rules.

In other words:

```text
parser confidence
        +
domain validation
        +
source provenance
        +
consequence of error
        =
routing decision
```

Not:

```text
confidence > 90
        =
truth
```

## Sometimes failure is the correct output

The Reddit discussion that started this is also the best counterexample to my own argument.

If your application exists to reproduce another system's behavior, outperforming that system can make your product less correct.

A resume-analysis tool answering "what information can I recover from this PDF?" should probably use every safe recovery path available.

A tool answering "what will this ATS likely see?" may need to stop exactly where the ATS stops.

That is the distinction between **document recovery** and **diagnostic fidelity**.

The same technical failure can require opposite product behavior depending on which question the software is supposed to answer.

There are other cases where explicit failure is preferable as well. If another parser attempt is expensive, if the consequence of a false positive is high, if privacy rules prohibit sending the artifact to an external model, or if the system has too little evidence to validate an interpretation, asking a human is not a failure of automation. It is a valid branch in the workflow.

## A parser cascade should be conditional, not desperate

Putting all of this together, the pipeline I increasingly prefer looks something like this:

```text
original artifact
      |
      v
classify source/document characteristics
      |
      v
cheapest deterministic extraction that should work
      |
      v
validate structure and domain expectations
      |
      +---- valid ----------------------------> candidate result
      |
      v
classify observed failure
      |
      +---- image/no text -------> OCR
      |
      +---- layout lost ---------> layout-aware extraction
      |
      +---- known source --------> specialized parser
      |
      +---- semantic ambiguity --> bounded semantic/LLM fallback
      |
      v
validate again
      |
      +---- credible -----------> accept/reconcile
      |
      +---- uncertain ----------> human review or explicit failure
      |
      v
retain evidence for replay and regression testing
```

That is more work than calling one parser and returning an error. It also creates more dependencies, more paths to test, and more operational complexity. Not every application needs it.

But messy external documents are adversarial in a mundane way: nobody designed all of them to satisfy your parser's assumptions. If users regularly pay the cost when those assumptions fail, giving the parser only one shot is often an architectural choice rather than an unavoidable limitation.

The design goal shouldn't be to make parsing infallible. It should be to make failure **observable, recoverable when appropriate, and honest when it isn't**.
