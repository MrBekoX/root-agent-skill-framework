# lead-integrate

## When to use

Use when your members have returned work that must become one domain result: at a checkpoint, when the last dependent unit lands, when member outputs contradict each other, and before anything goes back to Root Agent. Use it for partial results too. Integration is a real step, not a forwarding step: a pile of member outputs is not a domain result, and Root Agent should never have to reconcile your members' work itself.

## Required inputs and access

Read Root Agent's handoff package with its delegated outcomes, acceptance criteria and revision, your own dispatch record of which member owns which unit, every returned member output with its revision and evidence, and the artifacts themselves where they are accessible. Read the reporting contract for what to return and where. A member's summary is a claim about its output, not the output.

## Sequence of work

1. Reopen each member's actual artifact and evidence rather than integrating its summary. Record the output revision you inspected. An output you cannot open is unverified; say so instead of assuming it matches its description.
2. Map every returned output back to the delegated outcome it serves. Identify outcomes with no output yet, outputs that drifted outside their assigned unit, and work nobody owned. An unowned gap is a dispatch defect to fix through lead-dispatch, not something to fill yourself.
3. Reconcile contradictions between members: conflicting facts, incompatible formats, mismatched assumptions, different source revisions, or two members having written the same file. Resolve what falls inside your delegated scope by sending the correction to the producing member. Escalate a contradiction that changes the delegated outcome or acceptance criteria to Root Agent.
4. Check dependency coherence. A downstream output built on a superseded upstream revision is not integrated; reopen the affected unit rather than shipping the mismatch. Name the revision each part was built on.
5. Assemble the domain result in the form the package asked for, in its intended location, respecting the one-writer-per-file rule. Preserve each member's identifiers, filenames, paths and revisions verbatim. Do not rewrite a member's content to make it read better, and do not substitute your own analysis for a member's deliverable.
6. Evaluate the assembled result against each delegated acceptance criterion and record, per criterion: met with the evidence that shows it, unmet with what is missing and who owns it, or unverified with why it could not be checked. Do not mark a criterion met because the responsible member said it was.
7. Keep your own check honest about what it is. Checking work you integrated is quality assurance inside your domain; it is never the independent review. Root Agent selects and briefs the independent reviewer, and your judgement cannot substitute for that gate or clear it.
8. Bound the repair loop with the budget in the package. A failed criterion goes back to its producing member through lead-dispatch with the evidence and the exact fix, carrying existing counters forward. When the budget is exhausted without the result, return the decision to Root Agent with what the budget produced, what remains and the options; do not silently deliver less than the delegated outcome.
9. Return a partial result rather than holding a usable one back. State what exists, what is missing, which member owns the missing part, what has already been attempted and what the next step is. Never describe a partial result as the complete domain result.
10. Return the integrated result to Root Agent in the reporting contract's format, normally 5-10 lines with accessible evidence and the output revision: what now exists and where, criterion-by-criterion state, unresolved work with its owner, any blocker, and the next needed action. Distinguish proposals, completed actions and verified results.
11. Record what you integrated in your own domain records: the member outputs and revisions used, the contradictions resolved and how, the criteria state and the result's own revision. If the result changes later, its revision changes too, and any check that depended on the old one is no longer valid.

## Validate the result

Check that every delegated outcome is represented and none was dropped, that each criterion carries an explicit met, unmet or unverified state with its evidence, and that the revision of every input is recorded. Verify that contradictions were resolved or escalated rather than left in the result, that no member's content was rewritten, and that no output built on a superseded upstream revision was shipped as integrated. Confirm your own check was not presented as an independent review, and that a partial result is labelled partial.

## What to return

Return the integrated domain result with its revision and accessible evidence, the criterion-by-criterion state, the member outputs and revisions it was built from, the contradictions resolved and any escalated to Root Agent, unresolved work with its owner, the remaining budget, and the next needed action. If integration is blocked, name the missing output, inaccessible artifact or decision and who resolves it.

## What requires approval

Assembling, checking and reporting the domain result inside your delegated scope is covered by the user's task authority through Root Agent's package. Publishing the result, sending it to any external recipient, deleting or replacing another owner's artifact, connecting a service, spending, and production or account changes are not, and integration never supplies them. Obtain approval for an external action in your own conversation and never answer a member's approval on the user's behalf.
