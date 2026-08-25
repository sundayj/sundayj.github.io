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

- Open by establishing the actual problem, decision, disagreement, observation, or question. Do not use generic throat-clearing.
- Use descriptive section headings when the article is long enough to benefit from them.
- Organize technical comparisons around concrete criteria and tradeoffs.
- Use lists and tables when they improve scanning, but do not turn prose arguments into listicles.
- Do not force a tidy repeated template such as "why this matters" after every section.
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

- Favor direct sentences and concrete nouns and verbs.
- Mix concise statements with longer explanatory sentences when nuance requires it.
- Vary sentence rhythm deliberately. Avoid a page of uniformly polished, medium-length sentences.
- Contractions are acceptable when they sound natural.
- Parenthetical asides are acceptable sparingly when they add useful personal context.
- Rhetorical questions are acceptable when they genuinely frame the next argument, not as decoration.
- Humor and self-awareness may appear, but should not compete with the technical substance.
- **Do not use em dashes (`—`) in authored blog prose.** Justin does not use them in his natural writing. Rewrite with a period, comma, colon, semicolon, parentheses, or a restructured sentence instead.

## Technical writing

- Prefer examples from real tools, code, workflows, repositories, experiments, failures, or observed behavior.
- Prefer the author's concrete engineering experience over generic claims about what "developers" do when that experience is relevant.
- Define specialized concepts before relying on them heavily.
- State what a feature or technique is useful for, not merely what it is called.
- Distinguish personal preference from objective capability.
- When comparing alternatives, explicitly identify what would make a different choice reasonable for a different reader.
- Favor falsifiable specificity: named tools, actual constraints, measured results, concrete counterexamples, and traceable sources.

## Opinion and argument

- The author is comfortable taking a position.
- Build to the position through evidence and experience rather than announcing certainty before doing the work.
- Preserve genuine disagreement instead of smoothing every argument into artificial consensus.
- Steelman meaningful counterarguments.
- Call out assumptions behind forecasts, especially on fast-moving technology topics.
- Separate "this is happening" from "I think this will happen."
- Preserve uncertainty when the evidence is genuinely incomplete.

## Image style for substantial posts

When an article uses a hero image, prefer a sparse editorial illustration rather than a generic stock image or product-style AI graphic.

- Use a simple, cartoony editorial illustration with generous negative space.
- Prefer the JLSunday teal palette or a restrained palette that clearly belongs with the site.
- Use one clear visual metaphor rather than a crowded scene.
- Do not embed the article title, UI chrome, fake screenshots, labels, or decorative text in the image.
- Keep the style distinct from unDraw's flat SaaS-vector look.
- Use PNG for authored editorial hero illustrations.
- Treat the illustration used by **Make Your Coding Agent Earn the Architecture** as the current reference for visual density and tone, while keeping each article's concept distinct.

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
- any em dash in authored prose
- a summary paragraph after every section
- vague claims such as "AI is transforming everything" without evidence
- generic motivational endings
- stock AI vocabulary used as filler, including repeated uses of words such as `delve`, `landscape`, `crucial`, `pivotal`, `robust`, `leverage`, and `underscores`
- inflated language or fake profundity where a concrete sentence would say more
- prose that could be pasted unchanged into hundreds of unrelated AI-generated blog posts

## Personal experience rule

Never manufacture a personal anecdote, memory, project experience, workplace event, or first-person observation to make a draft sound more human. AI may organize, tighten, or contextualize experiences Justin has actually provided, but invented first-person material is unacceptable.

## Existing-blog characteristics to preserve

The older posts commonly:

- speak directly to the reader
- explain the author's decision process
- acknowledge incomplete information rather than pretending certainty
- provide practical feature-level detail
- use concrete examples and visual aids
- allow personality to appear inside otherwise technical writing

Keep those strengths while making newer posts somewhat tighter, more evidence-driven, and less repetitive than older long-form posts when appropriate.

## Final anti-slop editorial pass

After factual and argument review are complete, but before the draft is presented for final human approval, perform one dedicated anti-slop pass. This is a style and authenticity check, not a factual rewrite.

Check the entire draft for:

1. Generic throat-clearing that delays the actual argument.
2. Claims that could be replaced by concrete first-hand engineering experience or stronger evidence.
3. Artificial neutrality that erases the author's actual opinion or uncertainty.
4. Unnecessary headings, repeated summaries, listicle structure, or overly symmetrical organization.
5. Repetitive sentence length and rhetorical cadence.
6. Stock AI vocabulary, canned transitions, repeated binary-correction patterns, inflated language, and fake profundity.
7. Any em dash. Replace every one without exception in authored prose.
8. Generic claims that lack falsifiable specificity.
9. Counterarguments or disagreements that have been smoothed away rather than addressed directly.
10. Any first-person anecdote that cannot be traced to information the author actually supplied.
11. Paragraphs that could appear essentially unchanged on an unrelated AI-generated blog.

The goal is not to hide AI assistance. The goal is to ensure the final article reflects Justin's actual judgment, experience, evidence standard, and writing habits rather than default model prose.

## Editing rule

A voice-edit or anti-slop pass may change phrasing, organization, rhythm, and emphasis. It must not add new factual assertions, citations, statistics, technical claims, or personal anecdotes. Any such addition must return to factual review and, for personal experience, must be grounded in information actually supplied by the author.
