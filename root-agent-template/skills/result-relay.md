# result-relay

## When to use

Use when a Lead, Specialist or Reviewer returns a deliverable that must reach the user: a completed artifact, a partial result, a reviewed output, or a routine run's result. Use it whenever the answer the user needs already exists in someone else's output. It owns the carry: what the user sees, in their language, with working evidence paths. user-report decides whether the task closes; portfolio-status answers cross-task questions; this skill moves one result across without damaging it.

## Required inputs and access

Read the returned deliverable and its output revision, the accepted acceptance criteria for that stage, the producing owner's identity, the evidence the owner supplied, the review verdict from quality-review when a gate applied, and the user's language and stated delivery preference. Reopen the artifact or evidence path itself where it is accessible. An owner's summary is a claim about the artifact, not the artifact.

## Sequence of work

1. Identify what the user actually asked for and which returned artifact answers it. If the deliverable answers only part of the request, relay it as a part and name the rest with its owner. A finished component does not become the finished request because it is the piece in hand.
2. Reopen the evidence before relaying it. Confirm each path, link or artifact reference resolves and that the user can reach it. A path inside a domain folder the user cannot open is not delivery; give an accessible route or say the access is missing. Keep the owner's exact identifiers, filenames, revisions and paths verbatim; do not tidy, shorten, translate or reconstruct them.
3. Do not rewrite the deliverable. Root Agent relays; it does not re-author, re-analyze, re-summarize into a new set of claims, or improve the specialist's content. If the output is wrong, incomplete or fails a criterion, that is a correction routed to its owner through quality-review and the domain's sender, not an edit made here. If the output is merely formatted awkwardly, relay it as it is and note the observation separately.
4. Separate the relay from your own additions. What the owner produced, what the reviewer verified, and what Root Agent observed are three sources. Attribute each. Never present a Root Agent inference as part of the owner's finding, and never present an owner's claim as verified when it was not checked.
5. Compose the relay in the user's language, with this shape:
   - **TLDR** - one to three lines: what now exists, whether it meets the accepted criteria, and anything the user must do.
   - **Paths** - the accessible artifact references and evidence, exactly as the owner gave them, each labelled with what it shows.
   - **State** - which acceptance criteria are met with evidence, which are unmet, and which are unverified and why.
   - **Open** - unresolved work with its owner, any open review gate, and the next action.
   Translate your own framing into the user's language; do not translate filenames, identifiers, code, quoted source text or paths.
6. Report the review state honestly. An independent pass names the reviewer, the reviewed artifact revision and the checks performed. A producer's self-check is not an independent pass. A waived review is relayed as unreviewed, with the user decision that waived it. An open gate keeps the result explicitly unclosed, however good the artifact looks.
7. Relay partial and failed results with the same care as successful ones. Give what exists, what is missing, who owns the missing part, what was already attempted and the next step. Do not hold a usable partial result back waiting for completeness, and do not describe a partial result as a delivery.
8. Keep the relay proportionate. Default to a short message; expand only to preserve a material requirement, a real caveat or a needed instruction. Do not restate progress the user already saw, do not expose internal record schemas or coordination file paths, and do not repeat a group conversation the user can read.
9. Note anything that changes the user's next decision: a source that was stale, an access limitation, an assumption the owner made, a deferred scope item, or a cost that landed differently than planned. Keep these as brief labelled observations, separate from the owner's output.
10. Return the relayed state to work-control and user-report so the queue reflects what the user has actually received. Relaying a result does not close a task; user-report closes it only when every requested outcome and required review has supporting evidence.

## Validate the result

Check that every relayed path resolves and is reachable by the user, that identifiers and paths are verbatim, and that the deliverable's content was not rewritten. Verify that owner claims, reviewer findings and Root Agent observations are separately attributed, that unmet and unverified criteria are visible, and that the review state is stated exactly. Confirm the relay is in the user's language while technical identifiers are untouched, and that a partial result is not described as complete.

## What to return

Return the user-facing relay: TLDR, accessible paths with what each shows, criterion-by-criterion state, open work with owners, and the next action. Separately return to the queue: the artifact revision relayed, the evidence checked, the review gate state and anything that remains unverified. If evidence could not be reopened, say which part and what the user would need to reach it.

## What requires approval

Relaying a result inside the current conversation is covered by the task authority. It does not authorize publishing the result, sending it to any external recipient or channel, sharing a link outside the user's scope, deleting or replacing the owner's artifact, or performing any production or account change. Those keep their own approval boundaries, and the user answers each in the acting Bot's own conversation.
