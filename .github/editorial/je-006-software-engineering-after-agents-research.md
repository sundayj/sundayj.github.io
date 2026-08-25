# JE-006 research — software engineering after coding agents

This file is repository-only editorial evidence for the JE-006 dry run. It is not published by Jekyll.

## Working thesis

Coding agents are reducing the value of manually producing routine implementation while increasing the value of engineers who can frame problems, constrain systems, inspect evidence, make architectural tradeoffs, verify behavior, and own outcomes. The interesting question is no longer whether AI can code; it is which engineering responsibilities remain scarce when implementation itself becomes cheap.

## Evidence and counterevidence

### JetBrains Developer Ecosystem Survey 2026
Source: https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/

- Survey reports more than 15,000 professional developers worldwide.
- 90% reported using AI coding agents at work at least weekly; 68% reported daily use.
- Claude Code usage was reported at 39% globally and Codex at 16% in May–July 2026.
- This is strong adoption evidence, but adoption is not the same thing as measured productivity or code quality.

### Stack Overflow Developer Survey 2025
Sources:
- https://survey.stackoverflow.co/2025/ai
- https://survey.stackoverflow.co/2025/work

- 84% of respondents were using or planning to use AI tools in development; 51% of professional developers reported daily use.
- 46% distrusted AI-tool accuracy versus 33% who trusted it; only 3% reported high trust.
- 66% cited “almost right” AI solutions as a frustration; 45% cited time spent debugging AI-generated code.
- 64% did not view AI as a threat to their current job, although that share had declined from the prior year.
- Useful counterweight: developers are adopting AI while remaining skeptical about correctness.

### METR developer-productivity experiments
Source: https://metr.org/blog/2026-02-24-uplift-update/

- METR’s early-2025 randomized study found experienced open-source developers took about 19–20% longer on the studied tasks when AI was allowed.
- METR’s later study produced more favorable raw numbers, including an estimated ~18% speedup for returning participants, but confidence intervals crossed zero and METR explicitly says selection effects make the new estimate unreliable.
- Developers increasingly refusing to participate in no-AI conditions is itself interesting adoption evidence, but should not be presented as clean productivity proof.
- This is a strong reason to reject simplistic “AI makes every engineer X% faster” claims.

### Anthropic Economic Index
Sources:
- https://www.anthropic.com/research/impact-software-development
- https://www.anthropic.com/research/economic-index-march-2026-report

- Anthropic analyzed large samples of coding-related interactions to study how models are used in software work.
- In its March 2026 Economic Index, Computer and Mathematical tasks represented about 35% of Claude.ai conversations, while coding activity increasingly migrated into Claude Code/API traffic.
- Coding remains one of the clearest domains where agentic AI is already economically significant.
- Vendor-produced evidence should be treated as useful behavioral data, not a neutral forecast of job displacement.

### 2026 AI Engineering Survey — Notion × Amplify × Vercel
Source: https://www.notion.com/lp/ai-engineering-survey

- Survey reports more than 1,000 engineers building with AI.
- Among respondents using agents, reported write permissions rose from 52% to 90%.
- Three quarters said cost affects AI usage, and 40% said cost regularly constrains how ambitiously they use AI.
- This supports the argument that agent orchestration, permission design, observability, and economics are engineering concerns rather than prompt-writing trivia.

### Anthropic 2026 agentic coding trends
Sources:
- https://resources.anthropic.com/2026-agentic-coding-trends-report
- https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026

- Anthropic frames software work as shifting from direct code production toward orchestrating agents and emphasizes continued human judgment.
- Useful as an industry view, but it is vendor material and should not be the sole evidence for the thesis.

## Argument map

1. **The baseline has changed.** Coding agents are no longer niche autocomplete; professional adoption is widespread.
2. **Adoption does not prove universal productivity.** METR and Stack Overflow both complicate simplistic speed claims.
3. **Implementation is becoming cheaper faster than accountability is.** The scarce work moves toward problem definition, architecture, verification, domain judgment, and operational ownership.
4. **Senior engineers may benefit first, but there is a pipeline problem.** If organizations stop giving junior engineers meaningful work because agents can do routine tasks, they risk eliminating the apprenticeship path that produces future senior judgment.
5. **The new engineering stack includes the harness.** Context, tools, permissions, tests, evals, observability, cost controls, and rollback are part of the system.
6. **Engineers should optimize for leverage, not compete with token generation.** Learn to direct agents, validate them, understand systems deeply enough to catch plausible mistakes, and own business outcomes.

## Claims to avoid

- Do not claim software engineering is disappearing.
- Do not claim agent use guarantees productivity gains.
- Do not equate one vendor’s adoption data with independent labor-market evidence.
- Do not argue that “prompt engineering” is the durable replacement skill; orchestration and verification are broader engineering disciplines.
- Do not pretend junior roles are definitely doomed. Treat the apprenticeship/pipeline issue as a plausible structural risk that deserves attention.

## JE-006 evaluation notes

The resulting draft should be judged on:

- whether it sounds like Justin rather than generic AI commentary;
- whether factual claims can be traced to sources above;
- whether it includes real counterarguments and uncertainty;
- whether CI-014 produces useful, explainable internal-link suggestions;
- whether the PR remains reviewable without creating a path that can publish automatically.
