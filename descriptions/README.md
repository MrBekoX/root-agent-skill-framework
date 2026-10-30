# descriptions

Versioned copies of the Bot descriptions (system prompts). Each file contains only the description text. No heading or notes are added inside it, so the file can be pasted as-is, in one piece, into Grok Bot's **Edit Profile → Description** field. Notes are kept in this file.

| Bot | File | Source | Version | Last line |
| --- | --- | --- | --- | --- |
| Root Agent | [`root-agent.md`](root-agent.md) | [`root-agent-template/description.md`](../root-agent-template/description.md) | v0.3.9 (30 October 2026): pending-decision flow addendum and end-of-turn record rule extended to messages received from other Bots; 19 skills; v0.3.8 (26 October 2026): Secrets rule addendum and secret-hygiene added to the skill list; 19 skills; v0.3.7 (24 October 2026): skill templates only (end-of-day self-improvement routine, private user profile folder, same-turn Bot relay, no Bot co-author); v0.3.6 (23 October 2026): reply language generalized to "the user's language"; v0.3.5: skill templates only; 22 October 2026 — v0.3.4: end-of-turn record rule (dispatch-log + work-queue); v0.3.3 routine scope, team briefing and end-of-day self-improvement rules; 18 skills | Approval line verbatim |

## Rules

- **The template is the source.** `root-agent.md` is kept identical to `root-agent-template/description.md`. When you change one, update the other in the same commit. After changing the template, run `python validation/generate_setup.py` and `python validation/structural_check.py` inside `root-agent-template/`.
- **Old versions stay in git history.** No separate `archive/` copy is kept. Every line that changes behavior is listed as `old line → new line`.
- **Every description ends with the same line:** `Sending messages, publishing, deleting, purchasing, and production or account changes always require approval.`
- **No private data.** Personal names, passwords, tokens, internal URLs or task text are never written into a description; tasks are given by message.
