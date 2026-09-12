# Root Agent — description and skills

This folder contains the English description and reusable workflow instructions for a public Grok Bot named **Root Agent**. Recipients add only Root Agent. It creates necessary specialist Bots for actual tasks without asking for that authorization again, after checking existing ownership and platform capacity.

These files are the editable source texts for the Bot's description and skills. The user shares the configured Bot through **Share template** in the desktop app. No separate template package or recipient-side file import is needed. Live installation and testing have not been performed from this workspace; this does not prevent delivery of the requested source texts.

The template follows the current platform capacity rather than imposing a 20-Bot budget. The [official design article](https://x.ai/news/designing-grok-bot) describes roughly 50 Bots per account and six per group; verify actual availability in the recipient's account. Keep the smallest roster that covers the work instead of filling the capacity.

## Contents

- [Setup instructions for remote use](SETUP-INSTRUCTIONS.md): current description and all sixteen skill bodies in one readable attachment, generated from the individual sources; sharing still uses Share template. Regenerate this snapshot whenever a source text changes.
- [Description](description.md): paste its complete contents into the Bot's description.
- [Canonical specialist description](templates/specialist-description.md): for a Specialist or Reviewer. The same template is embedded in roster-management, so the saved skill carries it without relying on this repository.
- [Canonical Lead description](templates/lead-description.md): for a Lead. Also embedded in roster-management. A Lead created from it manages its own domain and briefs its own members.
- [Lead package](../lead-template/README.md): the Lead description plus two optional Lead-side skills the user can install by hand.
- [Desktop setup and sharing](INSTALL.md): use the configured Bot's native sharing action.
- [Acceptance checks](validation/acceptance.md): source coverage and suggested live checks; live results remain unverified.

## What Root Agent coordinates

Root Agent keeps a prioritized work queue with dependencies and effort checkpoints, routes using evidence of each Bot's capabilities, and diagnoses stalled work. Important deliverables can have a separate review stage. Decisions retain their reasons and revisit conditions; conversational status views show current work, user decisions and next actions. First use starts with one useful outcome rather than a long setup interview.

Root Agent sizes the structure to the work rather than to the request's wording: tier 0 it does itself, tier 1 is one Specialist it manages directly, tier 2 is a Lead plus two to five Specialists managed by that Lead, and tier 3 is one Lead per domain. The user never has to design a team.

Root Agent writes the role-specific description for every Bot it creates, and the task prompt for every recipient it addresses directly: a tier 0 or tier 1 owner, a Lead receiving a handoff package, a new Bot's setup or access-check stage, and an out-of-team independent Reviewer. In a tier 2 or tier 3 structure the Lead composes and sends its own members' prompts. Root Agent keeps roster creation, the review gate and accountability for the whole request. route-and-dispatch sends what Root Agent manages itself; lead-handoff sends to a Lead, and only treats a domain as delegated once that Lead returns a readback naming its dispatch plan. Private task prompts are not part of the public configuration.

Proactive monitoring is supported through a specialist-owned routine after its scope, schedule/time zone or event rule and reporting destination are actually specified and tested. Adding the monitoring workflow does not turn on an unspecified schedule.

## Skills

Sixteen skills, listed in the order they normally run.

- [intake-clarify](skills/intake-clarify.md): establish the outcome and ask only questions that change the next action.
- [scope-guard](skills/scope-guard.md): band the request into P0, P1 and deferred, set the effort bound, and rule on proposed expansions.
- [work-control](skills/work-control.md): keep the queue, priorities, dependencies, stage states and next actions.
- [roster-management](skills/roster-management.md): create necessary Leads and specialists and reconcile roles/capacity.
- [access-probe](skills/access-probe.md): prove read, write and auth access per operation before anything depends on it.
- [team-prompting](skills/team-prompting.md): compose role descriptions, stage briefs, handoff packages and review prompts.
- [route-and-dispatch](skills/route-and-dispatch.md): establish the structure tier, resolve the recipient, and send what Root Agent manages itself.
- [lead-handoff](skills/lead-handoff.md): delegate a domain's management to a verified Lead and require a readback before calling it delegated.
- [quality-review](skills/quality-review.md): arrange independent checks and bounded repairs for important deliverables.
- [blocker-escalation](skills/blocker-escalation.md): classify a stall and run the safe-resume and ownership-transfer checklists.
- [standing-workspace](skills/standing-workspace.md): establish instance ownership and maintain private working records.
- [bind-routine-via-owner](skills/bind-routine-via-owner.md): have the executing owner prove, save, test and own recurring work.
- [learning-loop](skills/learning-loop.md): preserve decisions and apply evidenced corrections to the responsible process.
- [portfolio-status](skills/portfolio-status.md): answer cross-task questions with a sourced view of every domain, blocker and pending decision.
- [result-relay](skills/result-relay.md): carry a finished deliverable to the user with its evidence paths intact.
- [user-report](skills/user-report.md): report one task's status and close it only when every criterion has evidence.

Each skill uses the six content categories described in [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations). These are readable instruction bodies; no undocumented import schema is claimed.

No live Bot, routine or public share link has been created by this repository work.

## Design authority

The files in this folder are the canonical source. Root Agent uses the current platform capacity rather than a fixed Bot budget and creates necessary specialists under the user's standing authorization; group changes and consequential external actions still need their own authorization. Only Root Agent is distributed. The instruction language is English; conversation replies follow the user's language.

The description belongs in Grok Bot's profile description field and the sixteen skills belong in its skill library. Keep private instance data out of public configuration. The earlier ROOT-AGENT-SETUP.md helper is superseded by the desktop Share template workflow and is not a source for current instructions.
