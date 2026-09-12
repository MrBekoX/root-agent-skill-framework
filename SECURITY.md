# Security Policy

## Scope

This repository contains instruction text for Grok Bot Bots and two local validation scripts. Security reports that belong here include:

- Instructions that could lead a Bot to bypass an approval boundary, take an external action without approval, answer another Bot's approval request, or expand its own authority.
- Prompt-injection weaknesses: text in a source, file or another Bot's message that the instructions would treat as authority.
- Credentials, secrets or private data committed to the repository.
- Problems in `validation/structural_check.py` or `validation/generate_setup.py`.

Vulnerabilities in Grok Bot itself should be reported to its vendor, not here.

## Reporting a vulnerability

Please do not open a public issue. Use GitHub's private vulnerability reporting: open this repository's **Security** tab and choose **Report a vulnerability**.

Include:

- The affected file and section.
- A concrete scenario showing the unsafe behavior: the request, the relevant Bot state and what the Bot would do.
- A suggested fix, if you have one.

The maintainer will coordinate the fix and its disclosure through the private advisory.

## Supported versions

Only the latest commit on `main` is maintained.

## Rules for contributions

Never put passwords, API keys, tokens, verification codes, personal data or internal URLs into descriptions or skills. Bots handle credentials through Grok Bot's secure entry or computer takeover, never through chat or instruction text.
