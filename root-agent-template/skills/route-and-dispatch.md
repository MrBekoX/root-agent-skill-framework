# route-and-dispatch

## When to use

Use for a clarified task, a changed scope or priority, an owner failure, a review stage or a returned result needing more work. Coordinate execution without becoming the default specialist. This skill decides the structure the work needs and is the single sender for everything Root Agent manages itself: task kickoffs, revisions, recovery messages and review assignments. lead-handoff is the single sender for a domain whose management has been delegated to a verified Lead. team-prompting composes the text this skill sends.

## Required inputs and access

Read the accepted brief, current account roster and ownership/capability evidence, the domain record in domains.md, your instance's work queue and dispatch records, and the actual Bot conversations or supported messaging interface. Use work-control for readiness, priorities and dependency plans, scope-guard for the accepted cut and effort bound, access-probe for capability readiness, and team-prompting for each recipient's precise instructions. Do not assume that a draft roster lists all existing Bots. Access to a roster and the presence of a suitable owner are separate facts.

## Sequence of work

1. A genuine tier 0 task uses its accepted brief, actual local capability and direct-check evidence without requiring roster access. For work needing another Bot, reopen the current roster, including hidden Bots where available, and record its source/check time. If incomplete or unavailable, identify the missing information and continue only independent preparation; do not claim no suitable Bot exists. If it contains only Root Agent, proceed with the empty-roster branch below.
2. Use work-control to identify ready stages, current task revisions, priorities and evidence-backed dependency readiness, and scope-guard for the accepted cut and the effort bound this work inherits. Match each requested outcome to an existing owner using verified capability cards and current access. Prefer one accountable owner per stage; do not broadcast the same task to multiple Bots. Keep implementation, integration and independent review responsibilities explicit. Independent ready work may proceed in parallel when input, account/session and file ownership do not conflict. When several Bots could own a stage, cite their performance-card counts (or `none yet`) as evidence alongside capability and access; counts never override verified capability, access or ownership.
3. Establish the structure tier for the whole accepted scope, then resolve the recipient. Apply tier 3 for distinct domains first, then tier 2 for parallel units or required independent review, then tier 0 only for one short external-effect-free deliverable with no independent-review gate; otherwise use tier 1. Do not bundle short exceptions into a larger Root-owned project. An existing Lead is retained until an explicit ownership transfer. A large-sounding request with one deliverable and no independent review can be tier 1.

   ```text
   Structure tiers
   Tier 0 - no external effects, one deliverable, roughly ten minutes of work,
            no independent review required -> Root Agent completes it directly.
            No Bot, self-message or dispatch-log send line is required.
   Tier 1 - one domain, one accountable deliverable, no independent review required
            -> one Specialist. Root Agent manages it directly through this skill.
   Tier 2 - two or more parallel work units in one domain, or an independent review is required
            -> one Lead plus as many Specialists as the work needs (no fixed headcount). The Lead manages the domain.
   Tier 3 - two or more distinct domains
            -> one Lead per domain. Each Lead manages its own domain; Root Agent
               manages the dependencies and the integrated acceptance between them.
   Tier changes are one-way during a task: work that grows past one owner moves up to
   tier 2. Taking management back from a Lead is an explicit ownership transfer, not a
   tier downgrade.
   ```

   ```text
   Recipient resolution (identical text in route-and-dispatch and lead-handoff)
   Open domains.md for this work unit's domain and peer team.
     Explicit transfer made Root the current dispatch owner?                 -> route-and-dispatch
     Otherwise current designated Lead has actual reference/profile readback? -> lead-handoff
     No current verified Lead?                                               -> route-and-dispatch
   Always route-and-dispatch, regardless of any Lead:
     (a) a newly created Bot's one-time setup or access-check stage
     (b) any independent Reviewer stage, including a Reviewer in the domain group
   An unverified or former Lead is not the current Lead: record the gap or transfer evidence.
   Never send the same work unit through both.
   ```

4. If no exact owner fits, consider the closest Bot with a temporary task scope. This does not silently rewrite its description, grant account access or change its standing permissions. Confirm that the proposed work fits its actual capabilities and remaining constraints.
5. If no suitable owner exists and the work is tier 0, Root Agent may complete it directly and validate the result. Do not chain short exceptions into a large specialist project.
6. Otherwise use roster-management to establish the needed durable roles for the tier. The user has authorized necessary specialist creation without another confirmation unless their current instructions restrict it. An empty roster is not a reason to ask the user to build a team manually. For tier 1 create the single Specialist. For tier 2 or 3 create and verify the Lead first, then its members with that actual coordinator reference; the production roster belongs in the handoff package, not the Lead's permanent description. A verified new profile may receive its own setup stage before other profiles or service access are ready. Size the structure to the real task's difficulty and complexity. Do not pre-create a generic department roster.
7. If no durable separate role is warranted, or current capacity/ownership prevents creation, bring the concrete decomposition or scope decision to the user through scope-guard. Do not narrow the requested outcome without their decision. Do not hide or delete Bots to evade a limit.
8. Before sending, create or reopen a task/stage reference tied to the accepted request and revision. Check the existing log and destination conversation for prior delivery. Record a pending intent when storage is available. If there is already a confirmed kickoff, continue that conversation; do not create another task with the same scope. A prompt revision is an update to that task, not a second assignment.
9. For tier 0 keep a local brief and direct-check evidence without a recipient prompt or self-send. Otherwise have Root Agent use team-prompting to compose an explicit task prompt for every recipient this skill addresses: the tier 1 owner, a newly created Bot's setup or access-check stage, and any independent Reviewer. Include: task/stage and prompt revision references; outcome and acceptance criteria; sources and accessible artifacts; role and scope; timing and time zone where relevant; authorized actions and approval points; dependency conditions and handoff contracts; file writer boundaries; the effort/retry/checkpoint plan from scope-guard; review requirements; and return destination. Give concrete work instructions, not a role name or a forwarded user request. Send one kickoff per ready stage to its verified owner and record the actual message evidence. In a tier 2 or tier 3 structure, the Lead composes and sends its members' production prompts; the setup and independent-review exceptions remain Root-managed stages. While that domain is `handoff-pending`, do not send specialist kickoffs for it and do not call it delegated. For multi-domain work, define distinct work units with one owner each and their dependencies; Root Agent reconciles the combined result.
10. Groups receive text handoffs. When an owner must inspect an image, use a supported direct Bot image handoff or an accessible shared artifact and verify access; do not assume posting an image path into a group delivers the image. Keep domain groups within current platform membership limits. Coordinate with the Lead directly when you are outside the group.
11. Record the actual message reference, recipient, task/stage and prompt revision, source/check time and send outcome in dispatch-log.md, using standing-workspace's record contract that lead-handoff shares. Distinguish pending, sent, acknowledged and completed, and return evidence to work-control for the queue. If logging fails after a successful send, retain the conversation evidence and repair the record; do not resend. If the send result is ambiguous, inspect the same destination and source state before any retry. If ambiguity remains, report it as unresolved.
12. Report who received what and known timing, distinguishing estimates from confirmed deadlines and checkpoints. The owner executes and returns evidence. On a missing response, failed delivery or repeated execution failure, use blocker-escalation to classify the cause and choose a bounded next step; it owns the safe-resume and ownership-transfer checklists. Check the original owner and prior effects before reassignment.
13. If the user changes or cancels active work, have team-prompting compose the precise revised instructions and send them promptly to the existing owner under the task's internal handoff authority. For a Lead-managed domain, send the revision to the Lead through lead-handoff instead; do not redirect its members yourself. Use the same task reference with a new revision, state what is superseded and update affected dependency stages. For reprioritization, coordinate a safe pause/checkpoint before conflicting replacement work. Confirm the owner received the update and report any already-completed effects separately. When the user says stop for a named scope, do not continue that scope to completion. Report already-done effects; do not undo them. Preserve pause-requested/cancel-requested until evidence supports the terminal state; do not claim work stopped or was undone just because the redirect was sent. Reconcile a late result with the accepted revision before using it.
14. On implementation results, use quality-review to prepare and evaluate the required independent review before important closure. Reviewer selection and dispatch stay with Root Agent in every tier, including a Lead-managed domain, and a Lead's check of work it produced, repaired, or integrated is never an independent review. An incremental or partial delivery does not waive that gate because the delta is small. Review is a distinct stage with the exact artifact revision and acceptance criteria, not duplicate implementation. If review is unnecessary, record why; if required but unavailable, retain review-blocked and continue other ready work without claiming full verification. Route concrete fixes to the implementation owner in the same task, or to the Lead in a Lead-managed domain, then recheck affected criteria and artifact revisions within the accepted repair/re-review limit. Use result-relay to carry a verified deliverable to the user and user-report to close the task after required review and integrated acceptance.
15. A status check or message alone does not prove that the receiving Bot is still running. Reopen live state before claiming ongoing work. Work-control maintains a next action; timed or event monitoring uses bind-routine-via-owner only when its authorized schedule/time zone or event and actual owning mechanism are established. Never promise unattended checks from Root Agent itself.

## Validate the result

Verify the owner exists and has the needed capability/access, scope matches the accepted revision, required inputs are accessible, dependencies are satisfied for released stages, authority has not expanded, and only one confirmed kickoff exists per work unit. Check that the established tier matches the actual work and that the recipient resolution was applied: no member of a Lead-managed domain holds a Root Agent kickoff for delegated work, and the two fixed exceptions are recorded as Root-managed stages. Verify actual sending independently of the local log, including changes and review assignments. Completion requires the owner's deliverable, any required independent review for its exact revision and integrated acceptance evidence.

## What to return

Return the established tier, the chosen owner or Lead and the rationale, task and prompt revision references, confirmed dispatch evidence, dependencies and known timing. Include review or recovery state when relevant. If the work was delegated, return the lead-handoff state rather than a member-level dispatch list. If routing is blocked, name the missing roster/capability/capacity or decision and the next useful action. If Root Agent used the tier 0 exception, return the actual deliverable and evidence.

## What requires approval

The user's task authority covers scoped internal handoffs and necessary specialist creation. Do not ask for that authority again. New group or membership changes need a concrete authorized scope. External sends, publication, purchases, deletion, production changes, service connections and other account changes need the relevant approval; a Bot handoff does not supply it. Respect the platform's own approval checks.
