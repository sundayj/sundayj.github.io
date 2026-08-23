---
layout: post
title: "Your Parser Shouldn't Get One Shot"
summary: >-
  A resilient parser should classify the failure mode, choose the cheapest recovery strategy that fits it, validate the result, and preserve uncertainty without treating one extraction attempt as truth.
excerpt: >-
  Parsing messy documents is rarely a one-shot problem. A more reliable design is a failure-mode-aware cascade that combines deterministic extraction, OCR, layout-aware recovery, semantic fallback, domain validation, and human review.
description: >-
  A practical look at resilient parser architecture, using a Reddit resume-parser discussion and lessons from a private financial application to examine redundancy, OCR, layout-aware extraction, LLM fallback, confidence, and replay.
canonical_url: "https://jlsunday.com/software-development/2026/08/23/your-parser-shouldnt-get-one-shot.html"
category: "Software Development"
tags: [parsing,ocr,software-architecture,pdf,ai]
image: "https://jlsunday.com/assets/images/posts/parser-redundancy-social.png"
comments: true
date: 2026-08-23
last_modified_at: 2026-08-23
author: {{ site.author.name }}
include_TOC: true
featured: false
sort: 0
---

<figure style="margin-top: 20px;">
  <img alt="A resilient parser pipeline moving from native text extraction through validation, recovery, review, and a trusted result" src="{{ '/assets/images/posts/parser-redundancy-social.png' | prepend: site.url }}" loading="lazy" title="Your Parser Shouldn't Get One Shot">
</figure>

[A Reddit post about resume parsing](https://www.reddit.com/r/resumes/comments/1vv5c63/i_parse_resumes_for_a_living_here_is_what_broke/){:target="_blank"}{:rel="noopener noreferrer"} caught my attention recently because the problem was familiar even though the domain wasn't. The author had built a resume parser intended to show job seekers what an applicant tracking system might actually see. The failures were the usual ugly document-processing problems: tables flattened into nonsense, two-column layouts read in the wrong order, punctuation mangled, fields dropped, and scanned PDFs with no useful text layer at all.

I replied that my instinct would be to add redundancy. If ordinary text extraction fails, try OCR. If the extracted text exists but clearly doesn't make sense, try another strategy. If deterministic parsing still can't resolve the document, use a semantic model as a bounded fallback. Keep the original artifact around, record what failed, and use that evidence to improve the system later.

The original poster pushed back for a good reason: their product is trying to approximate what an employer's ATS sees. If a resume breaks in Workday, silently recovering the missing information could make the diagnostic less accurate.

That exchange clarified something I had been thinking about while working on document ingestion in one of my own private projects. Redundancy only helps when recovery is actually part of the product's goal. In a recovery-oriented system, I want each fallback to exist for a known failure mode and to earn the right to continue through validation.

## Text extraction can succeed while understanding fails

One of the easiest mistakes to make in document ingestion is treating non-empty text as success.

A PDF parser may return hundreds or thousands of characters and still have destroyed the information your application cares about. A bank-statement table can become a stream of dates, descriptions, amounts, and balances in the wrong order. A two-column document can be flattened line-by-line across both columns. Characters can survive while relationships between them disappear.

That gives us two separate questions:

1. **Did I extract text?**
2. **Did I preserve enough structure and meaning to use it safely?**

The first is an extraction question. The second is a validation question, and production systems need both.

This matters most in domains where plausible-looking wrong data is worse than an explicit failure. Amazon Textract's best-practices documentation makes that distinction operationally: it returns confidence scores and recommends stricter thresholds, or human scrutiny, when incorrect detections have greater consequences. Financial processes are one of Amazon's examples for using a much higher threshold than low-risk archival use.

Source: [Amazon Textract best practices](https://docs.aws.amazon.com/textract/latest/dg/textract-best-practices.html)

A robust parser therefore needs some way to decide whether the extracted result is credible enough to continue.

## Different failures deserve different fallbacks

The useful way to think about parser redundancy is as a taxonomy of failure modes.

### No usable text layer

This is the straightforward OCR case. The PDF is effectively an image, or the embedded text is absent.

OCR exists specifically to recover from that class of failure. Running OCR first on every document is usually wasteful because born-digital PDFs already contain better text than OCR can reconstruct, and rasterizing them can introduce new errors.

OCRmyPDF illustrates this well. Its default behavior is deliberately cautious around pages that already contain text, while separate modes can skip existing text, redo an old OCR layer, or force rasterization when the current text layer is damaged. "No text," "bad OCR," and "broken character mapping" are different problems, so they deserve different recovery strategies.

Source: [OCRmyPDF advanced features](https://ocrmypdf.readthedocs.io/en/stable/advanced.html)

### Text exists, but layout was lost

OCR alone may not help here. The text itself can be perfectly recognizable while the table, columns, headers, or reading order are gone.

This is where layout-aware extraction becomes useful.

The open-source Unstructured project exposes several PDF partitioning strategies: `fast`, `hi_res`, `ocr_only`, and `auto`. Its fast path uses traditional text extraction; `ocr_only` exists for image-based documents; and `hi_res` performs layout detection so document elements can be classified with more structural information. The automatic strategy chooses among these based on document characteristics and requested behavior.

That is much closer to how I think robust ingestion should work: route according to the observed failure mode.

Unstructured's documentation also calls out cases where the more expensive layout strategy can perform worse. Multi-column ordering may favor OCR-only in some image-based documents. More sophisticated processing still has its own failure modes.

Sources: [Unstructured partitioning strategies](https://docs.unstructured.io/open-source/concepts/partitioning-strategies) and [partitioning documentation](https://docs.unstructured.io/open-source/core-functionality/partitioning)

### The source is known, but the format is idiosyncratic

Sometimes a generic document model is unnecessary. If you know the source and understand its format, a specialized deterministic parser can be cheaper, faster, easier to reproduce, and easier to regression-test than an AI model.

This is an area where "just send it to an LLM" is often the wrong first instinct.

If a statement format has stable markers, row shapes, or section boundaries, encode that knowledge. A source-specific parser gives you predictable failure behavior. When the format changes, you get a failing test or parse warning instead of a model quietly inventing a plausible interpretation.

The cost is maintenance. Enough special cases can become a parser zoo. That is one reason I prefer explicit, observable fallback stages instead of scattering special-case logic through unrelated code paths.

### The structure is present, but the meaning is ambiguous

This is the point where semantic models become interesting.

An LLM or vision-language model can be useful when the document contains the necessary evidence but deterministic rules cannot confidently map it into the application's domain model. I treat that model output as a structured candidate that still has to survive validation against things the application already knows:

- required fields;
- valid date ranges;
- arithmetic relationships;
- expected account or document state;
- duplicate detection;
- cross-document consistency;
- source evidence.

If the candidate fails those checks, the system can reject it, retry under a bounded policy, or ask for review.

The LLM's job is interpretation. Authority still comes from source evidence and validation.

## A private financial application as a case study

I have been applying versions of this pattern in a private financial application I maintain. I don't plan to publish the repository or the personal data it processes, although the architecture is general enough to discuss without exposing either.

The application ingests financial documents and transaction data from multiple formats. Its preferred path is deterministic because deterministic parsing is cheap, reproducible, and straightforward to test. OCR is reserved as a bounded fallback for PDFs without a useful text layer. Known statement shapes can be routed to specialized parsers. Every parsed result still passes domain checks before it becomes canonical financial state.

That validation step matters.

Parsed candidates are compared with domain state. Amounts, dates, balances, existing transactions, and other evidence provide constraints that a parser working in isolation does not have. Ambiguous results can be surfaced for review rather than silently promoted into canonical financial data.

This architecture has evolved because of real failures. A parser that works on ten statements can still meet an eleventh that exposes a bad assumption. The fix matters, and so does the failed case itself. Turning that case into regression coverage keeps the same assumption from quietly returning later.

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

Of course, keeping documents creates its own responsibilities. Resumes contain personal information. Financial statements contain even more. Retention, encryption, access control, and deletion policies have to be part of the architecture. "Keep everything forever because it might help debugging" is a poor default for sensitive data.

## Use confidence to route work

Machine-learning document systems often expose confidence scores. I would be cautious about interpreting those scores as universal probabilities of correctness; their most useful role is often routing.

A result above a carefully tested threshold may qualify for straight-through processing. A result below it may need another parser or human review. A result that violates a hard domain invariant should be rejected regardless of how confident the extraction model claims to be.

Confidence thresholds should also be tuned using representative data instead of choosing 90 or 95 because it sounds safe. The consequence of an error determines what threshold is acceptable, and different fields may deserve different rules.

A routing decision might combine:

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

The confidence score is one piece of evidence in that decision.

## Sometimes failure is the correct output

The Reddit discussion that started this is also the best counterexample to my own argument.

If your application exists to reproduce another system's behavior, outperforming that system can make your product less correct.

A resume-analysis tool asking "what information can I recover from this PDF?" should probably use every safe recovery path available. A tool asking "what will this ATS likely see?" may need to stop exactly where the ATS stops.

That difference comes down to the product's definition of correctness. One system is trying to recover the document's meaning; the other is trying to reproduce a downstream parser's behavior.

There are other cases where explicit failure is preferable. Another parser attempt may be expensive, the consequence of a false positive may be high, privacy rules may prohibit sending the artifact to an external model, or the system may have too little evidence to validate an interpretation. Human review is a valid branch in the workflow whenever automation runs out of trustworthy evidence.

## Make the parser cascade conditional

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

That is more work than calling one parser and returning an error. It creates more dependencies, more paths to test, and more operational complexity, so the extra machinery needs to earn its keep.

Messy external documents are adversarial in a mundane way: nobody designed all of them to satisfy your parser's assumptions. If users regularly pay the cost when those assumptions fail, giving the parser only one shot is often an architectural choice rather than an unavoidable limitation.

The design goal is graceful, observable failure: recover when the evidence supports it, and fail honestly when it doesn't.
