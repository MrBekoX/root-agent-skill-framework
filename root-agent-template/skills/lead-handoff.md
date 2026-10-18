# lead-handoff

## When to use

Use when a domain's work is managed by a Lead rather than by Root Agent directly: after roster-management verifies a Lead and its members, when delegated scope, priority or membership changes, when the Lead returns a result or a blocker, and when management of a domain transfers to or away from a Lead. This is the single sender for every message Root Agent addresses to a Lead about delegated work. route-and-dispatch remains the sender for work Root Agent manages itself. Sending a package only opens `handoff-pending`. Day-to-day management transfers only after the visibility readback in this skill, and that transfer is not a transfer of accountability for the user's whole request.

## Required inputs and access

Read the accepted brief and current task revision in work-queue.md, the domain record in domains.md, roster capability cards for the Lead and every member, the effort and cut plan from scope-guard, the review requirement from quality-review, and the actual Lead conversation or supported messaging interface. Use team-prompting to compose the package text and standing-workspace for the dispatch-log.md and domains.md record contracts. A Lead's name in a draft does not prove a verified Lead; require an actual Bot reference and a saved-profile readback.

## Sequence of work

1. Resolve the recipient before composing anything. This block is identical in route-and-dispatch; apply it the same way in both.

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

2. Confirm the structure actually calls for a Lead. Tiers 2 and 3, as route-and-dispatch defines them, are managed by a Lead; tiers 0 and 1 are not. Before any management transfer, work that needs one owner and no independent review may return to route-and-dispatch. An already Lead-managed domain keeps its Lead until an explicit ownership transfer reconciles active work. If the work grew past one owner while Root Agent was managing it directly, reconcile the active assignments first, then delegate the remaining scope; do not leave a Specialist holding a Root kickoff for work you are now delegating.
3. Verify the team before delegating it. Each member must have an actual Bot reference, a saved-profile readback, one owned deliverable, an explicit file writer boundary and a recorded access-readiness value from access-probe. A member whose required access is `needs-user-access`, `unavailable` or `unverified` is delegated with that limitation stated, and its source-dependent production stays gated. Do not hand a Lead a roster containing proposed roles described as if they existed.
4. Compose the handoff package through team-prompting. Fill every field with real values; mark a genuinely inapplicable field explicitly rather than leaving a placeholder. Keep the final line exactly as written.

   ```text
    Task and revision: actual task and stage reference, current scope revision, package revision and delivery key.
    Domain and team: actual peer-team reference and Lead, nonoverlapping scope/writers, and the integration owner when capacity split this domain across teams.
   Delegated outcomes: the concrete results this domain owns, each with its acceptance criteria and required evidence.
   Out of scope: work that belongs to another domain, to Root Agent, or to a later cut.
   Priority order: the sequence to work in and the reason, including which outcomes are the accepted cut and which were deferred.
   Team roster: for each member, actual Bot reference, owned deliverable, file writer boundary, access readiness and known limitations.
   Workspace: the domain folder, the Lead's own record location, and the one-writer-per-file rule.
   Decision authority: what the Lead may decide, sequence, re-assign or repair inside this scope without asking.
   Escalation: what must come back to Root Agent instead - scope change, new owner, external effect, access failure, effort limit reached, conflicting ownership.
    Effort and checkpoints: the inherited effort, retry and checkpoint budget, explicit checkpoint-due with time zone, and what changed evidence permits another attempt.
   Review gate: whether an independent review is required, who owns selecting the reviewer, and the artifact revision rule. Root Agent keeps reviewer selection and dispatch.
   Timing: actual deadline and time zone if given, or no committed deadline. Never invent an ETA.
   Reporting contract: what to report, on which events, to which destination, in what evidence format, normally 5-10 lines.
   Return: the integrated deliverable, its revision, unresolved criteria, blockers and the next needed action.

   Root does not send specialist kickoffs for this domain. You compose and send them.
   ```

5. Send the package once to the verified Lead through the actual conversation or supported interface. Record the message reference, recipient, task and package revision, source and check time, and send outcome in dispatch-log.md using standing-workspace's record contract. Set the domain's management state to `handoff-pending`. If the send result is ambiguous, inspect the same conversation before any retry; if ambiguity remains, report it unresolved rather than sending a second package.
6. Require a visibility readback before treating management as transferred. The domain stays `handoff-pending` until the Lead's readback shows it can see the current handoff package and roster: the readback names the member references and the deliverables from that package, confirms the delegated scope and its revision, names any member it cannot reach or use, and gives the first checkpoint it will report. A readback that invents members, or that omits the package's member references, does not count. Count the readback only when it comes from the verified Lead in the conversation the package was sent to. An echo from any other sender does not count. Record the plan in domains.md against the actual member references. Only then set the domain's management state to `lead-managed`. A sent package, a Lead's short reply, or a quiet conversation is not a readback. While the state is `handoff-pending`, do not call the domain delegated, do not tell the user it is delegated, and do not send specialist kickoffs for it.
7. If the readback does not arrive, is incomplete, or contradicts the delegated scope, use blocker-escalation to classify the stall and choose the bounded next step. A Lead that cannot dispatch is an ownership problem, not a reason for Root Agent to take over silently. Taking management back is an explicit ownership transfer: record the reason, reconcile the Lead's active assignments and any completed effects, then set the state to `root-managed` and continue through route-and-dispatch. Do not run both management paths over the same members.
8. Manage the delegation through the Lead afterwards. Scope changes, reprioritization, cut decisions and cancellations go to the Lead as a new package revision against the same task reference, stating what is superseded and what remains valid. Do not reset effort or retry counters by issuing a new package. Do not message a member of a `lead-managed` domain about delegated work; the two fixed exceptions in step 1 remain available and are recorded as Root-managed stages, not as delegated work.
9. Handle a Lead's proposed expansion through scope-guard. A Lead may propose additional work with its reason and cost; it may not enlarge the accepted scope on its own. Return an explicit accepted, deferred or declined decision with its rationale, and record it in decisions.md. An unanswered proposal is not consent.
10. Receive the Lead's results as one integrated domain deliverable with accessible evidence and an output revision. Reconcile it against the delegated acceptance criteria. Route a required independent review through quality-review and route-and-dispatch; the Lead does not select or brief its own reviewer, and a Lead's check of work it integrated is not an independent review. Send required corrections back to the Lead, not to the producing member.
11. Carry the verified result to the user through result-relay, and reconcile the domain's state into work-queue.md and domains.md through work-control. For several domains or Leads at once, use portfolio-status rather than composing a separate view here.
12. Record the transfer itself in decisions.md: which domain, which Lead, the delegated scope and revision, the authority boundary, the readback evidence and the condition under which management returns to Root Agent.
13. Delivery confirmation (User overlay — preserved verbatim through canonical framework updates.) A send is never recorded without the actual SendToAgent result: log its outcome in dispatch-log.md in the same turn, and a task with no send line is `not-dispatched`, never `handoff-pending` or `lead-managed`. After the send, the state stays `handoff-pending` until the Lead's actual readback arrives. Record the readback in dispatch-log.md and domains.md only with a verbatim quote from the Lead's message, its timestamp and sender id; a readback status without that quote, or copied from another task's record, is invalid. If no readback arrives by `checkpoint-due`, resend the same package once (logged) or escalate via blocker-escalation.

### Delivery and revision safeguards

These explicit exceptions govern step 13 while preserving its overlay text. SendToAgent means the supported Bot messaging operation actually available in the recipient's app, not a guaranteed tool name. If Bot messaging is disabled or unsupported, report the blocked capability without inventing a send. Use one delivery key per task, stage, recipient, purpose and package revision. A transport resend retains that key and cannot authorize a second execution. Inspect the destination and prior effects first; allow at most one transport resend for that key, otherwise escalate. A successful send with a failed local log is `sent (record repair pending)` with its actual conversation receipt, never evidence for another kickoff. When durable storage is unavailable, keep the same evidence in explicit conversation-only state; do not claim a saved log.

A valid readback must identify the current task, stage, scope and package revision and come from the verified Lead in the destination conversation after that package was sent. Old or out-of-order replies remain history and cannot release the new revision. A revised package requires a new matching readback for its changed scope; prior accepted management history remains recorded separately while affected new work waits. An exact duplicate package asks only for the prior readback or current status, not another member assignment. Apply standing-workspace's privacy exception to quoted evidence; redact secrets and mark the quote as redacted.

## Validate the result

Verify that a verified Lead exists with an actual reference and profile readback, that the package carries real values in every applicable field and the exact final line, and that the delegated scope matches the accepted task revision. Confirm the readback names the member references and deliverables from the current package before the state becomes `lead-managed`, and that no member was assigned while that package or roster was not visible. Check that every `lead-managed` record cites a quoted Lead readback with timestamp and sender. Check that no member of a `lead-managed` domain also holds a Root Agent kickoff for the same work, that the two fixed exceptions are recorded as Root-managed stages, and that effort counters survived package revisions. Confirm reviewer selection stayed with Root Agent. A composed package, a sent message and a transferred management state are three distinct facts.

## What to return

Return the domain, the verified Lead, the delegated outcomes and their acceptance criteria, the package revision and send evidence, the current management state (`handoff-pending`, `lead-managed` or `root-managed`), the Lead's recorded dispatch plan when present, the escalation boundary, and the next expected checkpoint. If the handoff is blocked, name the missing Lead verification, member readiness, access or decision, and the next useful action. Do not describe a domain as delegated without readback evidence.

## What requires approval

The user's task authority covers delegating scoped work to a verified Lead, composing and sending the package, and recording the transfer. Group creation and membership changes need their own authorized scope. External sends, publication, purchases, deletion, production changes, service connections and other account changes keep their separate approval boundaries; delegating work to a Lead supplies none of them, and a Lead's acceptance of a package does not answer them. The user answers each approval in the acting Bot's own conversation.
