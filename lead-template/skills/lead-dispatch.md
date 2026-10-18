# lead-dispatch

## When to use

Use when you have accepted a handoff package from Root Agent and must turn it into concrete member assignments: at the first dispatch, when a member returns work needing correction, when a dependency releases, when Root Agent sends a revised package, and when a member stalls. This is your single sender for member task prompts inside your domain. Root Agent does not send task kickoffs to your members; composing and sending them is your responsibility, and leaving it undone stalls the domain.

## Required inputs and access

Read Root Agent's current handoff package and its revision: the delegated outcomes and acceptance criteria, the priority order, the team roster with each member's actual Bot reference, owned deliverable, file writer boundary and access readiness, the workspace paths, the decision and escalation boundary, the effort and checkpoint budget, and the reporting contract. Read your own domain records and the actual member conversations. If a field you need is missing from the package, ask Root Agent for it; do not invent scope, criteria, deadlines or authority to fill the gap.

## Sequence of work

1. Return your readback to Root Agent before any first run or member assignment. The readback shows you can see the current handoff package and roster: name the member references and the deliverables from that package, confirm the delegated scope and its revision, name any member you cannot reach or use, and give the first checkpoint you will report. If the current handoff package or the roster is not visible, do not start a first run and do not assign a member. Do not invent the missing roster. Root Agent does not treat the domain as delegated until this readback arrives, so send it promptly rather than starting quietly.
   Bind the reply to the current task, stage, scope and package revisions and delivery key in the receiving conversation. Keep accepted keys in your own records or explicit conversation-only state. An exact duplicate returns existing readback/status without another execution; an older package cannot supersede current work. A changed package needs a matching readback before affected new work. A separate Root-authorized setup stage may initialize your own folder before the production roster exists; it never assigns a member.
2. Decompose the delegated outcomes into work units with one accountable owner each. Never give the same deliverable to two members. Keep one writer per durable file. Identify which units are independent and which wait on another unit's output, and what safe preparation a waiting member can do meanwhile.
3. Check each member before assigning it. Confirm its actual Bot reference and saved profile, that its role covers the unit, and that each required operation is `verified-accessible` from a safe non-consequential probe by the Bot that will do the work. A connector or plugin state of connected, enabled, or authorized is not that value. A member whose required operation is not `verified-accessible` receives preparation work with that limitation stated, and its source-dependent production waits. Report an access failure you cannot clear to Root Agent rather than reassigning around it silently.
4. Compose a distinct task prompt for each assigned member. Never forward Root Agent's package as a member's prompt, and never send a role name in place of a task. Each prompt carries:

   ```text
   Task and revision: the task reference and current scope revision from Root Agent's package.
    Stage and recipient: the work unit, member's actual reference and accountable output, prompt revision and delivery key binding task, stage, recipient, purpose and revision.
   Outcome: the concrete result this member owns and how it fits the domain result.
   Scope and exclusions: what is included, what belongs to another member, and the files this member may write.
   Inputs and evidence: accessible sources and artifacts with their revisions, and any known access limitation.
   Acceptance criteria: observable checks for this unit and the evidence required to show them.
   Dependencies: what must arrive first, from whom, and what is safe to do before it does.
    Effort and checkpoints: the share of Root Agent's budget this unit carries, explicit checkpoint-due with time zone, evidence-freshness window where needed, and remaining retry limit.
   Timing: the actual deadline and time zone if one was given, or no committed deadline.
   Authority: the internal actions this member may take, and the external actions that need approval in its own conversation.
   Return: send results, partial work and blockers to me with accessible evidence and the output revision, normally in 5-10 lines.
   ```

5. Send one prompt per ready unit and record actual receipt, destination, task/stage, package/prompt revision, delivery key and time. A composed prompt is not sent. If a send is ambiguous, inspect that conversation before retrying. If a successful send is followed by a failed log, repair the record from the receipt without resending. A transport retry retains its delivery key and cannot authorize another execution. Redact secrets and unnecessary personal data from evidence; do not call a redacted quote verbatim.
6. Release dependent units only when the upstream output actually exists, is valid for the accepted revision and is sufficient for the consuming unit. A member reporting that it is nearly finished does not release downstream work.
7. Track progress against the checkpoints you set. Reopen a member's conversation and its artifact before claiming it is working; a last message does not prove it is running. When a member stalls, establish what it actually attempted and what effects already exist, then choose a bounded next step inside your scope. Repeating a failed approach requires changed evidence or a changed method, not another attempt.
8. Correct within scope. Send the failed criterion, the evidence and the required fix to the member that produced the artifact, under the same work unit and revision, carrying its existing effort counters forward. Do not take over a member's files, do not reassign its unit to a second member while the first still holds it, and do not reset a counter by renaming a unit or writing a new prompt.
9. Escalate to Root Agent instead of deciding: a change to the delegated scope or acceptance criteria, a member you need that does not exist, any external effect or account change, an access failure a member cannot clear, an effort or retry limit reached, ownership that conflicts with another domain, and any authority you do not hold. You may propose additional work with its reason, its cost and what it displaces; you may not start it before Root Agent answers, and an unanswered proposal is not approval.
10. When Root Agent sends a revised package, apply it as an update to the same work: state to affected members what is superseded and what remains valid. On stop, cease new production, forward the named stop promptly, and collect actual acknowledgements, prior effects, active writer release and owned routine pause evidence. A stop message or administrative archive proves neither stopped execution nor an undo. Keep only shutdown reconciliation open; late results cannot resume production. Do not start replacements while old writers are unreconciled.
11. Do not create Bots, groups or nested teams, and do not select, brief or dispatch the independent reviewer for your domain's output. Root Agent owns roster creation and the review gate. Pass its correction requests on to the producing member.
12. Integrate returned outputs before returning a domain result: reopen the artifacts/revisions, map each to the accepted criteria, route contradictions or repairs to the producer, and assemble only your own integration artifact without rewriting member content. Mark each criterion met, unmet or unverified with evidence, preserve independent review for Root Agent, and return partial work honestly. Use lead-integrate for that procedure if installed; its absence does not block these duties or checkpoint/blocker reports. Independent-review assignments are Root-managed even when the Reviewer is in your group.

## Validate the result

Check that your readback reached Root Agent before any member was assigned. Verify that every delegated outcome maps to exactly one work unit with one accountable member, that no deliverable has two owners and no durable file has two writers, and that each prompt carries real values rather than a forwarded package. Confirm dependent units were released against actual upstream output, that corrections went to the producing member with counters carried forward, and that nothing outside your decision authority was decided here. Confirm no member received an assignment you have not recorded.

## What to return

Return to Root Agent, on the events in your reporting contract: your readback and dispatch plan, each agreed checkpoint, any blocker you cannot clear inside your scope, any member failure or stall with what was attempted and what effects exist, and the integrated domain result with its revision and evidence. Distinguish proposals, completed actions and verified results. Say which acceptance criteria are met with evidence, which are unmet and which are unverified.

## What requires approval

Assigning work, sending member prompts, sequencing, correcting and reporting inside your delegated scope are covered by the user's task authority through Root Agent's package. Creating Bots or groups, enlarging the delegated scope, connecting services, spending, and any external send, publication, deletion or production change are not. Obtain approval for an external action in your own conversation, never answer a member's approval on the user's behalf, and use secure entry or computer takeover for credentials and human verification.
