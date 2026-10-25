# secret-hygiene

## When to use

Use before and after any step that touches a credential or secret: a token, API key, password, cookie or session, verification code, card detail, private key, connection string or secret URL, in any app or service. Also use when writing a config, URL, command, file, log, message, prompt or template, when a tool result or file may contain a secret, and when a secret is found exposed.

## Required inputs and access

Read the step being taken, the app or service it targets, the secret's name (never its value) and where it is stored, and the user's authorization for that service. Use only the platform secret store, vault or a masked environment variable that the user authorized for this task.

## Sequence of work

These rules apply to every app and service, not only source control.

1. Secrets live only in the platform secret store, vault or a masked environment variable. Request them with the secure secret/form tool; never ask for or accept them as plain chat text when a secure entry exists.
2. A secret never goes into: a URL, a command line or its history, a config or git remote, a file in a workspace, a log, a record, a prompt, a message to a user or another Bot, a skill, a template, a routine payload, a screenshot, a commit or a PR. Reference it by name only (for example `$NAME`).
3. Read-only by default: never print, echo, cat, grep -o or otherwise display a value. To check for a secret use presence tests, counts or masked output (replace the value with `***`). Do not open a file only to look at a secret.
4. Before writing any config, URL, command or file that targets an external service: check for embedded credentials (`user:pass@`, `token@`, `?key=`, `Authorization`, long random strings) and stop if present. Prefer credential helpers, env variables or header injection that are not persisted.
5. After any git or network setup: verify with masked output (for example list remotes with credentials masked). Scan new artifacts before share, push, export or template creation, using pattern and presence checks that do not display values.
6. If a secret is found exposed (in a file, URL, log, message, repo or history): (a) do not display or copy it; (b) tell the user immediately in the same turn, naming only the location and secret type; (c) propose containment (remove from the location, rotate or revoke at the service, check history and forks) and wait for the user's approval before changing or deleting anything, except removing it from a file the user already authorized; (d) record only a redacted note (location, type, time, status), never the value; (e) track until rotation or revocation is confirmed by the user or the service.
7. Removing a secret from a file or URL does not make it safe: assume it was exposed until it is rotated or revoked. Say so plainly.
8. Least privilege and expiry: prefer scoped, short-lived credentials; ask the user to rotate after any exposure; never reuse a secret for a different service or purpose.
9. Never use a found or leaked secret, and never use another service's secret for a different purpose. Use only what the user authorized for the stated task.
10. Delegates: every handoff, kickoff and specialist prompt states these rules in one line and forbids passing secrets in message text. Report received secrets or likely exposures from other Bots to the user immediately.

## Validate the result

Before closing a task that used a credential:
- No secret in the final artifacts, logs, records, messages or commits (masked scan done).
- Remote URLs, configs and routine prompts contain no embedded credentials.
- Exposure incidents have a recorded containment status and a user-confirmed rotation.

## What to return

Return the masked check results (location and type only, never a value), the containment status of any exposure, and the next action the user must take, such as rotation or revocation.

## What requires approval

Changing, deleting or rotating anything after an exposure, except removing it from a file the user already authorized, needs the user's explicit approval. Sending messages, publishing, deleting, purchasing, and production or account changes always require approval.
