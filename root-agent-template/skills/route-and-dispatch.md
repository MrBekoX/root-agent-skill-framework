# route-and-dispatch

## When to use

Use for a clarified task, a changed scope or priority, an owner failure, a review stage or a returned result needing more work. Coordinate execution without becoming the default specialist. This skill decides the structure the work needs and is the single sender for everything Root Agent manages itself: task kickoffs, revisions, recovery messages and review assignments. lead-handoff is the single sender for a domain whose management has been delegated to a verified Lead. team-prompting composes the text this skill sends.

## Required inputs and access

Read the accepted brief, current account roster and ownership/capability evidence, the domain record in domains.md, your instance's work queue and dispatch records, and the actual Bot conversations or supported messaging interface. Use work-control for readiness, priorities and dependency plans, scope-guard for the accepted cut and effort bound, access-probe for capability readiness, and team-prompting for each recipient's precise instructions. Do not assume that a draft roster lists all existing Bots. Access to a roster and the presence of a suitable owner are separate facts.

## Sequence of work

1. Reopen the current roster, including hidden Bots where available. Record its source and check time. If incomplete or unavailable, identify the missing information and continue only independent preparation; do not claim no suitable Bot exists. If it is visible and contains only Root Agent, proceed with the empty-roster branch below.
2. Use work-control to identify ready stages, current task revisions, priorities and evidence-backed dependency readiness, and scope-guard for the accepted cut and the effort bound this work inherits. Match each requested outcome to an existing owner using verified capability cards and current access. Prefer one accountable owner per stage; do not broadcast the same task to multiple Bots. Keep implementation, integration and independent review responsibilities explicit. Independent ready work may proceed in parallel when input, account/session and file ownership do not conflict.
3. Establish the structure tier for the work, then resolve the recipient. Size the structure to the work, not to the request's wording; a large-sounding request with one deliverable is still tier 1.

   ```text
   Structure tiers
   Tier 0 - no external effects, one deliverable, roughly ten minutes of work
            -> Root Agent completes it directly. No Bot is created.
   Tier 1 - one domain, one accountable deliverable, no independent review required
            -> one Specialist. Root Agent manages it directly through this skill.
   Tier 2 - two or more parallel work units in one domain, or an independent review is required
            -> one Lead plus two to five Specialists. The Lead manages the domain.
   Tier 3 - two or more distinct domains
            -> one Lead per domain. Each Lead manages its own domain; Root Agent
               manages the dependencies and the integrated acceptance between them.
   Tier changes are one-way during a task: work that grows past one owner moves up to
   tier 2. Taking management back from a Lead is an explicit ownership transfer, not a
   tier downgrade.
   ```

   ```text
   Recipient resolution (identical text in route-and-dispatch and lead-handoff)
   Open domains.md for this work unit's domain.
     Domain has a verified Lead (actual Bot reference plus profile readback)? -> lead-handoff
     No verified Lead?                                                        -> route-and-dispatch
   Always route-and-dispatch, regardless of any Lead:
     (a) a newly created Bot's one-time setup or access-check stage
     (b) an out-of-team independent Reviewer stage
   An unverified Lead is not a Lead: use route-and-dispatch and record the gap.
   Never send the same work unit through both.
   ```

4. If no exact owner fits, consider the closest Bot with a temporary task scope. This does not silently rewrite its description, grant account access or change its standing permissions. Confirm that the proposed work fits its actual capabilities and remaining constraints.
5. If no suitable owner exists and the work is tier 0, Root Agent may complete it directly and validate the result. Do not chain short exceptions into a large specialist project.
6. Otherwise use roster-management to establish the needed durable roles for the tier. The user has authorized necessary specialist creation without another confirmation. An empty roster is not a reason to ask the user to build a team manually. For tier 1 create the single Specialist. For tier 2 or 3 create the Lead alongside its members, using the canonical Lead description. Create the smallest relevant structure for the first real task and verify each profile before anything is dispatched. Do not pre-create a generic department roster.
7. If no durable separate role is warranted, or current capacity/ownership prevents creation, bring the concrete decomposition or scope decision to the user through scope-guard. Do not narrow the requested outcome without their decision. Do not hide or delete Bots to evade a limit.
8. Before sending, create or reopen a task/stage reference tied to the accepted request and revision. Check the existing log and destination conversation for prior delivery. Record a pending intent when storage is available. If there is already a confirmed kickoff, continue that conversation; do not create another task with the same scope. A prompt revision is an update to that task, not a second assignment.
9. Have Root Agent use team-prompting to compose an explicit task prompt for every recipient this skill addresses: the accountable owner of a tier 0 or tier 1 stage, a newly created Bot's setup or access-check stage, and an out-of-team independent Reviewer. Include: task/stage and prompt revision references; outcome and acceptance criteria; sources and accessible artifacts; role and scope; timing and time zone where relevant; authorized actions and approval points; dependency conditions and handoff contracts; file writer boundaries; the effort/retry/checkpoint plan from scope-guard; review requirements; and return destination. Give concrete work instructions, not a role name or a forwarded user request. Send one kickoff per ready stage to its verified owner and record the actual message evidence. In a tier 2 or tier 3 structure, do not compose or send task prompts for a Lead's members: hand the domain to the Lead through lead-handoff and let it compose and send them. For multi-domain work, define distinct work units with one owner each and their dependencies; Root Agent reconciles the combined result.
10. Groups receive text handoffs. When an owner must inspect an image, use a supported direct Bot image handoff or an accessible shared artifact and verify access; do not assume posting an image path into a group delivers the image. Keep domain groups within current platform membership limits. Coordinate with the Lead directly when you are outside the group.
11. Record the actual message reference, recipient, task/stage and prompt revision, source/check time and send outcome in dispatch-log.md, using standing-workspace's record contract that lead-handoff shares. Distinguish pending, sent, acknowledged and completed, and return evidence to work-control for the queue. If logging fails after a successful send, retain the conversation evidence and repair the record; do not resend. If the send result is ambiguous, inspect the same destination and source state before any retry. If ambiguity remains, report it as unresolved.
12. Report who received what and known timing, distinguishing estimates from confirmed deadlines and checkpoints. The owner executes and returns evidence. On a missing response, failed delivery or repeated execution failure, use blocker-escalation to classify the cause and choose a bounded next step; it owns the safe-resume and ownership-transfer checklists. Check the original owner and prior effects before reassignment.
13. If the user changes or cancels active work, have team-prompting compose the precise revised instructions and send them promptly to the existing owner under the task's internal handoff authority. For a Lead-managed domain, send the revision to the Lead through lead-handoff instead; do not redirect its members yourself. Use the same task reference with a new revision, state what is superseded and update affected dependency stages. For reprioritization, coordinate a safe pause/checkpoint before conflicting replacement work. Confirm the owner received the update and report any already-completed effects separately. Preserve pause-requested/cancel-requested until evidence supports the terminal state; do not claim work stopped or was undone just because the redirect was sent. Reconcile a late result with the accepted revision before using it.
14. On implementation results, use quality-review to prepare and evaluate the required independent review before important closure. Reviewer selection and dispatch stay with Root Agent in every tier, including a Lead-managed domain, and a Lead's check of work it integrated is never an independent review. Review is a distinct stage with the exact artifact revision and acceptance criteria, not duplicate implementation. If review is unnecessary, record why; if required but unavailable, retain review-blocked and continue other ready work without claiming full verification. Route concrete fixes to the implementation owner in the same task, or to the Lead in a Lead-managed domain, then recheck affected criteria and artifact revisions within the accepted repair/re-review limit. Use result-relay to carry a verified deliverable to the user and user-report to close the task after required review and integrated acceptance.
15. A status check or message alone does not prove that the receiving Bot is still running. Reopen live state before claiming ongoing work. Work-control maintains a next action; timed or event monitoring uses bind-routine-via-owner only when its authorized schedule/time zone or event and actual owning mechanism are established. Never promise unattended checks from Root Agent itself.

## Validate the result

Verify the owner exists and has the needed capability/access, scope matches the accepted revision, required inputs are accessible, dependencies are satisfied for released stages, authority has not expanded, and only one confirmed kickoff exists per work unit. Check that the established tier matches the actual work and that the recipient resolution was applied: no member of a Lead-managed domain holds a Root Agent kickoff for delegated work, and the two fixed exceptions are recorded as Root-managed stages. Verify actual sending independently of the local log, including changes and review assignments. Completion requires the owner's deliverable, any required independent review for its exact revision and integrated acceptance evidence.

## What to return

Return the established tier, the chosen owner or Lead and the rationale, task and prompt revision references, confirmed dispatch evidence, dependencies and known timing. Include review or recovery state when relevant. If the work was delegated, return the lead-handoff state rather than a member-level dispatch list. If routing is blocked, name the missing roster/capability/capacity or decision and the next useful action. If Root Agent used the tier 0 exception, return the actual deliverable and evidence.

## What requires approval

The user's task authority covers scoped internal handoffs and necessary specialist creation. Do not ask for that authority again. New group or membership changes need a concrete authorized scope. External sends, publication, purchases, deletion, production changes, service connections and other account changes need the relevant approval; a Bot handoff does not supply it. Respect the platform's own approval checks.
