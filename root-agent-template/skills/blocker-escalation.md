# blocker-escalation

## When to use

Use when a stage stops producing evidence: a missing response, a repeated failure, an ambiguous delivery, an unreachable source, an owner that cannot proceed, a Lead that does not return its readback, or an effort limit reached. Use it before retrying, reassigning, taking work back from a Lead or telling the user something is stuck. This skill classifies the cause and produces a bounded next step; work-control keeps the queue and route-and-dispatch or lead-handoff sends whatever this classification calls for.

## Required inputs and access

Read the stalled task and stage with its current revision from work-queue.md, the dispatch or handoff evidence in dispatch-log.md, the domain's management state in domains.md, the owner's capability card and access-readiness values, the effort and retry budget from scope-guard, prior attempts and their observed causes, and the actual owner or Lead conversation. Silence, a stale log entry or a message asking for an update is not evidence of what the owner is doing.

## Sequence of work

1. Establish current state before classifying. Reopen the owner's conversation and the artifact or source itself. Distinguish: never sent, sent but unacknowledged, acknowledged and working, working but past its checkpoint, stopped with a returned cause, stopped without a cause, and unknown. If the send itself is ambiguous, inspect the destination before any retry; an unverified send is a delivery problem, not an execution failure.
2. Classify the stall into exactly one primary cause. Record a secondary cause only when both must be resolved.
   - **Access** - a required source, service, file or identity is not reachable by the acting Bot. Confirm with access-probe rather than assuming; an old success is not a current check.
   - **Decision** - an unresolved scope, priority, acceptance or authority question blocks the next step. Identify whether it belongs to the user, to Root Agent within existing authority, or to the Lead inside its delegated scope.
   - **Dependency** - a prerequisite output is missing, invalid for the accepted revision or insufficient for the consuming stage. Name the upstream stage and its owner.
   - **Owner** - the assigned Bot cannot do the work: a capability mismatch, an unverified profile, a conflicting assignment, a shared session or file conflict, or no response after its checkpoint.
   - **Effort limit** - the accepted attempt, time or cost budget is exhausted without the result. This is a checkpoint requiring a decision, not a licence to abandon the outcome.
   - **Approval** - a platform or user approval gate is open in the acting Bot's own conversation. It is resolved there, never by Root Agent or another Bot.
   - **Unknown** - current state cannot be established. Say so; do not substitute the most likely cause.
3. Name the smallest resolving action and its responsible party. A cause with no named party is not classified. Keep the escalation ladder intact: inside a `lead-managed` domain a member's stall goes to its Lead; the Lead escalates to Root Agent; Root Agent escalates to the user only for a decision, an approval or an authority the team does not hold. Do not reach past a Lead to its member, and do not ask the user for something the team can resolve.
4. Release everything the stall does not block. Independent ready stages continue. A blocked domain does not pause an unrelated one. Record what continued so the stall's cost is visible and bounded.
5. Before resuming, complete the safe-resume checklist. Every item must be answered from evidence, not assumption:
   - What was actually attempted, and what effects already exist?
   - Is the next action idempotent? If not, what would a second execution duplicate, send, publish, charge or overwrite?
   - Has the blocking cause actually changed, or only the attempt number?
   - Is the accepted revision still current, and does the owner hold it?
   - Are the required access values still `verified-accessible` at their current check time?
   - Does the remaining effort budget cover the next step, and what is its checkpoint?
   Repeating a failed approach requires changed evidence or a changed method. Never retry uncertain non-idempotent work blindly; inspect the authoritative source state first.
6. Before transferring ownership, complete the ownership-transfer checklist:
   - Reconcile the current owner's active work and any completed effects; capture partial artifacts and their location.
   - Send the current owner an explicit stop or pause for the named scope, and record `pause-requested` or `cancel-requested` until its actual state supports `paused` or `cancelled`. A stop message is not an undo and does not prove work stopped.
   - Resolve the file writer boundary so two owners never hold the same durable file.
   - Carry forward the task reference, the accepted revision and the existing effort and retry counters. A new owner, renamed stage or fresh prompt revision does not reset them.
   - Record the transfer, its reason and its authority in decisions.md.
   Only then dispatch the replacement, through lead-handoff for a `lead-managed` domain or route-and-dispatch otherwise.
7. For a Lead that does not return its handoff readback, treat it as an `owner` stall against the Lead, not as permission for Root Agent to start briefing that domain's members. Resolve it with the Lead, or perform an explicit ownership transfer back to `root-managed` under step 6 and say so to the user.
8. For an effort-limit stall, bring the decision rather than the failure. Present what the budget produced, what remains, the options with their cost, and a recommendation, through scope-guard. Continuing, cutting scope, changing method and changing owner are all valid outcomes; silently reducing the requested outcome is not.
9. Record the classification, evidence, chosen action, responsible party, new checkpoint and any revised budget in work-queue.md, and the material decisions in decisions.md, through work-control and standing-workspace. Return the result to work-control for queue reconciliation and to portfolio-status when the user asks what is stuck.
10. Do not send task messages from this skill, do not answer another Bot's approval, and do not declare work resumed, stopped or transferred without the evidence that supports that state.

## Validate the result

Check that the current state was reopened from the owner's conversation and the artifact, not inferred from the log. Verify exactly one primary cause with a named resolving party, that the escalation ladder was respected, and that unaffected work continued. Confirm the safe-resume checklist was answered before any retry and the ownership-transfer checklist before any reassignment, with counters carried forward and no duplicate writer. Confirm a `lead-managed` domain's member was not briefed directly. A classification without a next action and a checkpoint is incomplete.

## What to return

Return the stalled stage and its current evidenced state, the primary cause, the resolving party, the smallest next action and its checkpoint, what continued unaffected, and the remaining effort budget. For an ownership transfer, return what was reconciled, what effects already exist and where the partial artifacts are. For an unknown state, say so plainly and give the concrete step that would establish it. Never report a stall as resolved because a message about it was sent.

## What requires approval

Diagnosing, recording and choosing a bounded next step within the accepted scope is covered by the task authority, as are scoped internal handoffs and ownership transfers between existing owners. A stall does not create authority to retry an external send, publication, deletion, purchase or production change, to connect a service, to change another Bot's standing permissions, or to exceed an accepted budget. Approval gates are answered by the user in the acting Bot's own conversation.
