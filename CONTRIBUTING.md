# Contributing

Thanks for helping improve Root Agent. Most contributions change English instruction text rather than code, so review focuses on behavior: what a Bot will do differently after the change.

## Before you start

- Read [`README.md`](README.md) to understand how Root Agent works and [`AGENTS.md`](AGENTS.md) for the writing rules.
- For a behavior change, open an issue first so the design can be discussed before texts are rewritten.
- Report security problems privately as described in [`SECURITY.md`](SECURITY.md), not in a public issue.

## Making a change

1. Edit the sources under `root-agent-template/`: `description.md`, `skills/` or `templates/`. Never edit `SETUP-INSTRUCTIONS.md` by hand; it is generated.
2. If you change a template in `templates/`, update its embedded copy in `skills/roster-management.md` in the same change.
3. If you change the recipient-resolution block, change it identically in `skills/route-and-dispatch.md` and `skills/lead-handoff.md`.
4. Regenerate the snapshot and run the checks:

   ```bash
   cd root-agent-template
   python validation/generate_setup.py
   python validation/structural_check.py
   ```

5. Open a pull request and fill in the template.

## What a pull request needs

- `structural_check.py` output showing `FAIL 0`.
- Every behavior change listed as `old line → new line`.
- A statement about live testing: what you ran in Grok Bot and the evidence, or "not live-tested". Scenarios in `validation/acceptance.md` stay NOT RUN unless you have evidence.
- No private data in texts that go to a Bot. See **Public payload hygiene** in [`AGENTS.md`](AGENTS.md).

## Style

- English, operational and concise. Keep the six skill sections.
- Keep the final approval line of every description exactly as it is.
- Do not expand Root Agent's scope into executing work, owning routines or answering other Bots' approvals.

## Code of conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you agree to uphold it.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).
