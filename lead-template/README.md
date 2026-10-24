# Lead — description and optional skills

This folder holds the source texts for the **Lead** Bots that Root Agent sets up. In tier 2 and tier 3 structures Root Agent hands the day-to-day management of a domain to the Lead: the Lead writes and sends the Specialists' task prompts, integrates their outputs, and returns a single integrated result to Root Agent.

## What is required, what is optional

| Part | Where | Required? |
| --- | --- | --- |
| Canonical Lead description | [`../root-agent-template/templates/lead-description.md`](../root-agent-template/templates/lead-description.md) | **Yes.** Root Agent applies it when creating the Lead Bot. It works on its own. |
| `lead-dispatch` skill | [`skills/lead-dispatch.md`](skills/lead-dispatch.md) | No. Installed manually; adds depth. |
| `lead-integrate` skill | [`skills/lead-integrate.md`](skills/lead-integrate.md) | No. Installed manually; adds depth. |

No ability to register or enable skills across Bots is assumed; the library and Bot availability checks the current app supports are verified. The mandatory dispatch, revision/duplicate, stop and routine limits are in the canonical Lead description. The two skills here take effect only if they are installed and their availability is verified; a missing one does not stop the mandatory behavior.

## Setup

1. Root Agent first creates the Lead and verifies its profile, then creates the members with the real Lead reference. The variable member roster goes in the handoff, not the permanent description. A separate setup/access-check can initialize the Lead's own folder before the production roster exists. The final approval line is kept verbatim.
2. Optionally, save the two bodies under `skills/` to Grok Bot's skill library and enable them **only for that Lead Bot**. Do not enable them for Root Agent or the Specialists.
3. In the production handoff, the Lead returns a **readback** confirming the members, deliverables and checkpoint with the current task/stage/scope/package revision and delivery key. The reply must come from the same recipient conversation; an old revision or a duplicate package does not start a new execution. Root Agent records the time and sender; if sensitive data is present, the quote is marked redacted. Newly delegated scope waits until there is a valid readback.

## Limits

- The Lead does not create Bots, groups or sub-teams.
- The Lead does not choose or brief the independent reviewer for its own domain — the review gate stays with Root Agent. The Lead checking its own integrated work does not count as independent review.
- The Lead does not expand the delegated scope on its own; it **proposes** with reasons and cost, and Root Agent decides. An unanswered proposal is not approval.
- A routine is bound to the Specialist who actually runs the work; it is not bound only to the coordinating Lead or to Root Agent.

Root Agent counterpart: [`lead-handoff`](../root-agent-template/skills/lead-handoff.md).
