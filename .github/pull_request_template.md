## Summary

<!-- What changes and why. Link the related issue. -->

## Behavior changes

<!-- List every behavior change. Write "none" for documentation-only changes.
old line → new line
-->

## Validation

- [ ] Ran `python validation/generate_setup.py` inside `root-agent-template/`
- [ ] `python validation/structural_check.py` inside `root-agent-template/` reports `FAIL 0`
- [ ] If a template in `templates/` changed, its copy in `skills/roster-management.md` changed too
- [ ] If the recipient-resolution block changed, it is identical in `route-and-dispatch.md` and `lead-handoff.md`

## Live testing

- [ ] Not live-tested
- [ ] Tested in Grok Bot. Evidence:

## Hygiene

- [ ] No credentials, personal names, email addresses, absolute local paths or internal URLs in `description.md`, `skills/` or `templates/`
- [ ] The final approval line of every description is unchanged
