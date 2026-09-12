# lead-dispatch

## When to use

Use when you have accepted a handoff package from Root Agent and must turn it into concrete member assignments: at the first dispatch, when a member returns work needing correction, when a dependency releases, when Root Agent sends a revised package, and when a member stalls. This is your single sender for member task prompts inside your domain. Root Agent does not send task kickoffs to your members; composing and sending them is your responsibility, and leaving it undone stalls the domain.

## Required inputs and access

Read Root Agent's current handoff package and its revision: the delegated outcomes and acceptance criteria, the priority order, the team roster with each member's actual Bot reference, owned deliverable, file writer boundary and access readiness, the workspace paths, the decision and escalation boundary, the effort and checkpoint budget, and the reporting contract. Read your own domain records and the actual member conversations. If a field you need is missing from the package, ask Root Agent for it; do not invent scope, criteria, deadlines or authority to fill the gap.

## Sequence of work

1. Return your readback to Root Agent before dispatching anything: confirm the delegated scope and its revision, state which member will receive which deliverable, name any member you cannot reach or use, and give the first checkpoint you will report. Root Agent does not treat the domain as delegated until this arrives, so send it promptly rather than starting quietly.
2. Decompose the delegated outcomes into work units with one accountable owner each. Never give the same deliverable to two members. Keep one writer per durable file. Identify which units are independent and which wait on another unit's output, and what safe preparation a waiting member can do meanwhile.
3. Check each member before assigning it. Confirm its actual reference, that its role covers the unit, and that its required access is recorded as accessible. A member whose access is unverified or missing receives preparation work with that limitation stated, and its source-dependent production waits. Report an access failure you cannot clear to Root Agent rather than reassigning around it silently.
4. Compose a distinct task prompt for each assigned member. Never forward Root Agent's package as a member's prompt, and never send a role name in place of a task. Each prompt carries:

   ```text
   Task and revision: the task reference and current scope revision from Root Agent's package.
   Stage and recipient: the work unit and the member's actual reference and accountable output.
   Outcome: the concrete result this member owns and how it fits the domain result.
   Scope and exclusions: what is included, what belongs to another member, and the files this member may write.
   Inputs and evidence: accessible sources and artifacts with their revisions, and any known access limitation.
   Acceptance criteria: observable checks for this unit and the evidence required to show them.
   Dependencies: what must arrive first, from whom, and what is safe to do before it does.
   Effort and checkpoints: the share of Root Agent's budget this unit carries, its next checkpoint and its retry limit.
   Timing: the actual deadline and time zone if one was given, or no committed deadline.
   Authority: the internal actions this member may take, and the external actions that need approval in its own conversation.
   Return: send results, partial work and blockers to me with accessible evidence and the output revision, normally in 5-10 lines.
   ```

5. Send one prompt per ready unit to its member and record what you sent, to whom, against which package revision, and when. A composed prompt is not a sent one. If a send result is ambiguous, inspect that member's conversation before resending; a duplicate assignment causes duplicate work and duplicate effects.
6. Release dependent units only when the upstream output actually exists, is valid for the accepted revision and is sufficient for the consuming unit. A member reporting that it is nearly finished does not release downstream work.
7. Track progress against the checkpoints you set. Reopen a member's conversation and its artifact before claiming it is working; a last message does not prove it is running. When a member stalls, establish what it actually attempted and what effects already exist, then choose a bounded next step inside your scope. Repeating a failed approach requires changed evidence or a changed method, not another attempt.
8. Correct within scope. Send the failed criterion, the evidence and the required fix to the member that produced the artifact, under the same work unit and revision, carrying its existing effort counters forward. Do not take over a member's files, do not reassign its unit to a second member while the first still holds it, and do not reset a counter by renaming a unit or writing a new prompt.
9. Escalate to Root Agent instead of deciding: a change to the delegated scope or acceptance criteria, a member you need that does not exist, any external effect or account change, an access failure a member cannot clear, an effort or retry limit reached, ownership that conflicts with another domain, and any authority you do not hold. You may propose additional work with its reason, its cost and what it displaces; you may not start it before Root Agent answers, and an unanswered proposal is not approval.
10. When Root Agent sends a revised package, apply it as an update to the same work: state to each affected member what is superseded and what remains valid, stop work that is no longer wanted, and report effects that already happened. A stop message is not an undo. Do not start a parallel set of assignments under the new revision while the old ones are still running.
11. Do not create Bots, groups or nested teams, and do not select, brief or dispatch the independent reviewer for your domain's output. Root Agent owns roster creation and the review gate. Pass its correction requests on to the producing member.
12. Hand the collected member outputs to lead-integrate for reconciliation into one domain result before returning anything to Root Agent.

## Validate the result

Check that your readback reached Root Agent before any member was assigned. Verify that every delegated outcome maps to exactly one work unit with one accountable member, that no deliverable has two owners and no durable file has two writers, and that each prompt carries real values rather than a forwarded package. Confirm dependent units were released against actual upstream output, that corrections went to the producing member with counters carried forward, and that nothing outside your decision authority was decided here. Confirm no member received an assignment you have not recorded.

## What to return

Return to Root Agent, on the events in your reporting contract: your readback and dispatch plan, each agreed checkpoint, any blocker you cannot clear inside your scope, any member failure or stall with what was attempted and what effects exist, and the integrated domain result with its revision and evidence. Distinguish proposals, completed actions and verified results. Say which acceptance criteria are met with evidence, which are unmet and which are unverified.

## What requires approval

Assigning work, sending member prompts, sequencing, correcting and reporting inside your delegated scope are covered by the user's task authority through Root Agent's package. Creating Bots or groups, enlarging the delegated scope, connecting services, spending, and any external send, publication, deletion or production change are not. Obtain approval for an external action in your own conversation, never answer a member's approval on the user's behalf, and use secure entry or computer takeover for credentials and human verification.
