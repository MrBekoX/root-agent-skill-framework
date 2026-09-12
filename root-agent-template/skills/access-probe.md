# access-probe

## When to use

Use before relying on any source, service, connector, file location or account for real work: before creating a Bot whose purpose depends on that access, before delegating a domain that needs it, before binding a routine to it, and whenever a capability card says `unverified` or its freshness has lapsed. Use it when a Bot reports that something is ready, connected or working without showing what it actually did. This skill produces the access-readiness values that roster-management records on capability cards; it does not create Bots, connect services or perform the task itself.

## Required inputs and access

Read the stage that needs the access, the exact source or service and the operations it requires, the capability card for the Bot that will use it, prior probe records and their check times, and the user's authorization boundary for that service. Use the acting Bot's own conversation and supported controls for anything requiring sign-in or approval. A shared computer, a shared account or another Bot's earlier success does not establish that this Bot can reach this source now.

## Sequence of work

1. State what must be proved before probing. List each required operation separately: read a specific artifact, list a location, write or create in a named place, authenticate as a particular identity, or invoke a named tool. "Access to the account" is not a requirement; "read the named file in the domain folder" is. Probe only what the current stage actually needs.
2. Identify the acting Bot. Access is a property of a specific Bot's current session, tools and enabled plugins, not of the account in general. A new Bot does not inherit another Bot's enabled skills, plugin authorization or connector state. Probe as the Bot that will do the work, through route-and-dispatch's setup and access-check stage, and record which Bot returned the evidence.
3. Choose the smallest safe probe per operation, in this order: read or list first, then a reversible write to a location the Bot owns, then authentication identity. Never probe with the real business action, a destructive operation, an external send, a purchase or a production change. Never probe a non-idempotent operation whose effects you cannot inspect. If the only way to prove an operation is to perform a consequential action, stop and record it as `unverified` with the reason.
4. Run the probe and capture what actually happened: the operation attempted, the exact target, the observed result or error text, the identity it acted as where visible, and the check time with its time zone where consequential. A probe with no returned evidence is not a probe. A screenshot, listing, returned content, created-then-removed test artifact or exact error message is evidence; a Bot's sentence saying it has access is not.
5. Assign one readiness value per operation, not per service:
   - `verified-accessible` - the operation was performed and its evidence returned.
   - `needs-user-access` - the attempt returned a concrete authorization, sign-in, approval or permission failure that a user action can clear. Name the exact action and where the user performs it.
   - `unavailable` - the operation cannot be performed by this Bot on this platform or the target does not exist. Name what would change that.
   - `unverified` - not attempted, ambiguous, or provable only through a consequential action. Never round `unverified` up to accessible.
   A read that succeeds says nothing about a write. Record each operation's value separately even when they share a service.
6. Distinguish an authorization failure from an absent target, a wrong path, an expired session, a disabled tool and a platform approval gate. Each has a different resolution and a different owner. Record the exact error rather than a paraphrase, so the cause survives into blocker-escalation.
7. Never request or accept credentials, verification codes or CAPTCHA answers in chat. Direct the user to the supported secure entry or computer takeover flow in the acting Bot's own conversation, and treat the completed flow as a new fact to re-probe rather than an assumption of success.
8. Return the readiness values to roster-management for the capability card, with the acting Bot, exact operation, evidence, source and check time. Record a refresh trigger: a changed credential, connector, plugin authorization, path, source format, Bot or a new dependent task invalidates the value. Treat a lapsed value as `unverified`, not as a continuing pass.
9. Gate dependent work on the result. Source-dependent production waits for its required operations to reach `verified-accessible`. Independent preparation, setup and folder initialization may continue with the limitation stated. Do not delegate a domain, bind a routine or promise a deliverable on an `unverified` or `needs-user-access` operation without saying so in the same message.
10. When a probe clears a previously blocked stage, return that to work-control and blocker-escalation so the queue releases the dependent work. When it fails, return the exact failure, the resolving party and the smallest next action; do not retry an unchanged probe without changed evidence.

## Validate the result

Check that each required operation has its own recorded value and evidence, that the evidence shows an actual attempt rather than a claim, and that the acting Bot in the record is the Bot that will do the work. Verify that no probe performed a consequential, external or destructive action, and that no credential passed through ordinary chat. Confirm values are not older than their refresh trigger, that a successful read was not reported as full access, and that `unverified` was not reported as ready.

## What to return

Return, per operation: the acting Bot, the exact target, the readiness value, the evidence, the source and check time, and the refresh trigger. For anything not `verified-accessible`, return the concrete blocking cause, who resolves it, where they resolve it, and what work is gated on it meanwhile. State plainly which dependent work may proceed and which may not.

## What requires approval

Running a safe read, list or owned-location write probe within the user's existing scope is covered by the task authority. Connecting a new service, authorizing a plugin, changing another Bot's permissions, purchasing capacity and changing account settings each require their own authority and are not implied by a probe. Never perform an external send, publication, deletion, purchase or production change to test access. Platform approval controls remain in effect, and the user answers them in the acting Bot's own conversation.
