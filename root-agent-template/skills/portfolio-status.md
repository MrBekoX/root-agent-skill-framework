# portfolio-status

## When to use

Use for any question that spans more than one task, domain or Lead: "What is happening?", "Where are we?", "What do you need from me?", "What is blocked?", "What is next?". Use it before proposing new work, at a checkpoint covering several domains, and whenever the user must choose between competing requests. user-report answers a single task and reports its closure; this skill owns the cross-task view. It is an on-request view of checked records, not a live dashboard or a monitoring service.

## Required inputs and access

Read work-queue.md across all active tasks, domains.md for domain owners, Leads and management states, decisions.md for open and recent decisions, dispatch-log.md for send and acknowledgement evidence, roster capability cards for owner readiness, and the relevant owner or Lead replies. Use work-control for priority, dependency and next-action planning, blocker-escalation for stall causes, and scope-guard for the accepted cut and deferred work. A stored record is evidence of what was last checked, not of what is running now.

## Sequence of work

1. Establish the scope of the view: all active work, one domain, work waiting on the user, or the next decision. Include every accepted task, not only the ones in progress. Blocked, waiting, paused, deferred and review-pending work belongs in the view. Never reduce a portfolio to the subset that is going well.
2. Reopen each task's current record and its supporting evidence. Record a check time per item. Where evidence is unavailable or stale, mark the item `unknown` or `last known at <time>` rather than repeating an old state as current. Do not infer that a Bot is running from its last message.
3. For each domain, establish the management state and who to ask: `root-managed` means Root Agent holds dispatch, `lead-managed` means the named Lead does, and `handoff-pending` means the package was sent but the Lead has not returned its dispatch plan. Show the actual Lead or owner reference so the user knows whose conversation an approval or question belongs to.
4. Classify each item into exactly one of: progressing, waiting on a dependency, waiting on the user, blocked, review-pending, review-blocked, paused, deferred by an accepted cut, or complete. Keep execution and review status separate; a finished implementation with an open review gate is not complete. Use blocker-escalation's cause classes for anything blocked, so the view names the cause rather than only the symptom.
5. Separate what the team can resolve from what only the user can. For each user-action item, state the concrete decision or action, which Bot's conversation it belongs in, what is waiting on it and what it costs to keep waiting. Do not answer, reproduce or relay another Bot's approval request; point to it.
6. Identify the next checkpoint per domain: what will produce the next evidence, who owns it, and whether a real mechanism exists for it. A checkpoint that depends on the user's next message is stated as such. Do not present a planned time as a scheduled check unless an enabled routine or another verified mechanism owns it.
7. Order the view by the user's explicit priorities first, then actual deadlines, then dependencies that unblock other accepted work, then waiting age. Take the ordering from work-control rather than re-deciding it here; explain the effect of a priority conflict and request only the consequential decision.
8. Write the view in the user's language, compactly. Default to a short table of task, state with check time, owner or Lead, blocker or user action, and next action, followed by at most three lines naming what needs the user now. Expand beyond the default length only to preserve a material requirement. Keep internal record schemas and file paths out of the reply unless they explain a persistence problem.
9. Make freshness visible. State the oldest check time in the view, or per row where they differ materially. If a record could not be reopened, say which one and what remains unverified. Never present a stored snapshot as live status.
10. Return the reconciled view and any newly observed state to work-control so the queue reflects what this pass established. Do not send task messages, change priorities, or close work from this skill.

## Validate the result

Check that every accepted task appears, including blocked, deferred and waiting work, and that no requested outcome disappeared because one part finished. Verify each state against its evidence source and check time, that execution and review states are distinct, and that each domain's management state matches domains.md. Confirm user-action items name the right conversation and that no approval was answered or relayed. Confirm claimed checkpoints have real owners and mechanisms. An item with no reopened evidence is `unknown`, not `progressing`.

## What to return

Return the current cross-task view: what is moving and with what evidence, what is waiting and on whom, what is blocked and why, what the user must decide or do and where, the next checkpoint per domain, and the freshness of the evidence. Include deferred scope and its revisit condition so an accepted cut stays visible. If the view is partial because records or conversations could not be reopened, say exactly which parts are unverified.

## What requires approval

Reading your own coordination records and reporting them in the current conversation is covered by the task authority. Reporting does not authorize publishing the view, sending it to external recipients, changing priorities, dispatching work or closing tasks. Do not answer another Bot's approval request on the user's behalf, and keep external sends, publication, deletion, purchases and production or account changes within their own approval boundaries.
