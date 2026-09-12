# Contributor and agent guide

Rules for people and AI agents changing this repository. `AGENTS.md` and `CLAUDE.md` carry the same text.

## What this repository is

Source texts for **Root Agent**, a coordinator Bot for Grok Bot: its profile description, sixteen skills, canonical Lead and Specialist descriptions, and two validation scripts. This is a prompt and skill engineering project, not an application. The texts are pasted into Grok Bot or given to a Bot as a setup attachment. Nothing in this repository runs a live Bot.

## The model the texts must preserve

- Root Agent is the single entry point. It clarifies the request, bands the scope, sizes the structure, creates the Bots the work needs and delegates. It does not execute research, code, content or analysis, except tier 0 work: no external effects, one deliverable, roughly ten minutes.
- Tiers: **0** Root Agent itself; **1** one Specialist managed by Root Agent; **2** one Lead plus two to five Specialists, managed by the Lead; **3** one Lead per domain.
- In a Lead-managed domain the Lead writes and sends its members' task prompts. Root Agent keeps roster creation, reviewer selection and accountability for the whole request.
- A domain team is at most one Lead and five Specialists, with no nested teams. Use the platform's current capacity; do not reintroduce a fixed Bot budget.
- Recurring work binds to the Bot that executes it, never to Root Agent.
- Do not propose changes that make Root Agent execute work, own routines, or answer another Bot's approval request.

## Repository layout

```text
root-agent-template/     Everything that goes to Grok Bot (canonical source)
  description.md         Root Agent profile description
  skills/                Sixteen skill bodies
  templates/             Canonical Lead and Specialist descriptions
  SETUP-INSTRUCTIONS.md  Generated; never edit by hand
  validation/            structural_check.py, generate_setup.py, acceptance.md
lead-template/           Optional skills for Lead Bots, installed by hand
descriptions/            Paste-ready copies of Bot descriptions
```

## Skill files

- One skill per file in `root-agent-template/skills/`, named with a kebab-case English slug.
- Exactly six sections: `When to use`, `Required inputs and access`, `Sequence of work`, `Validate the result`, `What to return`, `What requires approval`.
- Instruction text is English. Bots reply in the user's language.
- A saved skill must be self-contained: it cannot rely on reading this repository. Refer to other skills by name only.
- The recipient-resolution block must stay byte-identical in `route-and-dispatch.md` and `lead-handoff.md`.

## Descriptions

1. A description holds permanent rules only: role, ownership, sources, style, approval boundary and exclusions. Task text belongs in messages, never in a description.
2. Write operationally: own this, pull from there, produce that, do not do X without approval. No motivational filler.
3. Every description ends with exactly this line:
   > Sending messages, publishing, deleting, purchasing, and production or account changes always require approval.
4. No generic helper Bots. Each Bot has one narrow ownership that fits in one sentence.
5. One owner per piece of work. Check existing roles for overlap before writing a new one.
6. Bot memory is not a source of truth. Steps with consequences reopen current data.
7. A Bot with durable work names its state folder under `/workspace/<slug>/`.
8. The templates in `templates/` must match their embedded copies in `skills/roster-management.md`.

## Routines

- The order never changes: run once and verify, save the method as a skill, then bind a routine.
- Every routine defines: behavior on missing or stale data; where partial completion is reported; whether a retry is idempotent; and the re-test condition when the source format changes.
- The owning Bot reports each run to Root Agent in 5–10 lines with evidence.

## Public payload hygiene

Texts that go to a Bot (`description.md`, `skills/`, `templates/`) must not contain credentials, API keys, tokens, verification codes, personal names, email addresses, absolute local paths, internal URLs, customer data or real task history. `structural_check.py` enforces part of this; reviewers check the rest.

## Validation

```bash
cd root-agent-template
python validation/generate_setup.py     # regenerate SETUP-INSTRUCTIONS.md
python validation/structural_check.py   # must report 0 FAIL
```

## Changing behavior

- Never change a skill's behavior silently. List every behavior change as `old line → new line` in the pull request description.
- Do not claim live behavior was tested unless it ran in Grok Bot and the evidence can be shown. Acceptance scenarios otherwise stay NOT RUN.

## Working style

- Be concise and direct. If a design choice is weak, say so and give the alternative.
- When the output, scope, or one-off versus recurring nature of a change is unclear, ask all questions in one message before changing texts.
- Keep the technical terms skill, routine, description, handoff and dispatch as they are.
- Reply in the language the contributor uses.
