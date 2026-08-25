# JLSunday Voice Guide

This is a living guide derived from the existing public blog. It should be refined as new author-approved posts provide better examples.

## Core voice

- Write as a technically experienced practitioner explaining what was learned, tested, or concluded.
- Use first person naturally when the author's experience or judgment is relevant.
- Be conversational without becoming casual filler.
- Prefer clear opinions with reasons over artificial neutrality.
- Show uncertainty when it is real; do not weaken well-supported conclusions merely to sound balanced.
- Explain enough context that a competent developer outside the immediate specialty can follow the argument.

## Structure

- Open by establishing the actual problem, decision, or question rather than with a generic definition.
- Use descriptive section headings when the article is long enough to benefit from them.
- Organize technical comparisons around concrete criteria and tradeoffs.
- Use lists and tables when they improve scanning, but do not turn prose arguments into listicles.
- Conclusions should synthesize what the evidence means, not simply repeat earlier sections.

## Long-form scanability

For long technical articles, preserve depth while giving scanning readers enough structure to decide whether to keep reading.

- Consider a concise **TLDR** block near the beginning. Use the deck label **The Short Version** when appropriate.
- Major conversational headings may be followed by a one-sentence explanatory **section deck** that states the technical point of the section more formally.
- Use a small number of **pull quotes** for conclusions worth remembering. They should surface claims already supported by nearby prose rather than introduce new claims.
- Use a substantive end-of-article **call to action** when the post has a natural next step such as trying a tool, inspecting a repository, or reporting failure cases. Avoid generic engagement prompts.
- A reader should be able to scan the title, TLDR, headings, section decks, pull quotes, and conclusion and understand the article's argument before committing to the full read.
- Do not add these devices mechanically to every post. They are aids for long-form material, not a required template.

The DevSculptor theme provides reusable classes for these elements: `article-tldr`, `article-deck`, `pull-quote`, and `article-cta`.

## Sentence-level style

- Favor direct sentences and concrete nouns/verbs.
- Mix concise statements with longer explanatory sentences when nuance requires it.
- Contractions are acceptable when they sound natural.
- Parenthetical asides are acceptable sparingly when they add useful personal context.
- Rhetorical questions are acceptable when they genuinely frame the next argument, not as decoration.
- Humor and self-awareness may appear, but should not compete with the technical substance.

## Technical writing

- Prefer examples from real tools, code, workflows, or observed behavior.
- Define specialized concepts before relying on them heavily.
- State what a feature or technique is useful for, not merely what it is called.
- Distinguish personal preference from objective capability.
- When comparing alternatives, explicitly identify what would make a different choice reasonable for a different reader.

## Opinion and argument

- The author is comfortable taking a position.
- Build to the position through evidence and experience rather than announcing certainty before doing the work.
- Steelman meaningful counterarguments.
- Call out assumptions behind forecasts, especially on fast-moving technology topics.
- Separate "this is happening" from "I think this will happen."

## Avoid generic AI prose

Do not use these habits unless the surrounding prose genuinely calls for them:

- "In today's rapidly evolving landscape..."
- "It is important to note..."
- "This begs the question..."
- "Let's dive in."
- "At the end of the day..."
- repeated "However," / "Moreover," / "Furthermore," transitions
- repeated binary correction structures such as "it's not X, it's Y," "not X but Y," or "the goal isn't X; it's Y"; legitimate contrasts are fine, but do not use this construction as a recurring rhetorical rhythm
- symmetrical three-item lists used only for rhetorical polish
- excessive em dashes
- a summary paragraph after every section
- vague claims such as "AI is transforming everything" without evidence
- generic motivational endings

## Existing-blog characteristics to preserve

The older posts commonly:

- speak directly to the reader
- explain the author's decision process
- acknowledge incomplete information rather than pretending certainty
- provide practical feature-level detail
- use concrete examples and visual aids
- allow personality to appear inside otherwise technical writing

Keep those strengths while making newer posts somewhat tighter, more evidence-driven, and less repetitive than older long-form posts when appropriate.

## Editing rule

A voice-edit pass may change phrasing, organization, rhythm, and emphasis. It must not add new factual assertions, citations, statistics, or technical claims without sending those additions back through factual review.
