# SETUP-INSTRUCTION-PROMPT — Root Agent v0.3.9 from the cleaned repository

Install or upgrade **this existing Root Agent** to **v0.3.9 from merge #26**, using the exact source commit below. Fetch the repository from GitHub, perform the installation yourself through supported controls, verify the actual saved configuration, and report in the user's language. Do not stop at a plan or give me installation steps you can execute yourself.

This is a one-time installation request. Keep this prompt out of the installed description, skills and public template. Use the existing Bot and its verified instance; do not create another Root Agent, a Lead or a team for setup.

## 1. Fixed source snapshot and authority

- Repository: https://github.com/MrBekoX/root-agent-skill-framework
- Cleanup merge: https://github.com/MrBekoX/root-agent-skill-framework/pull/11
- Immutable source: https://github.com/MrBekoX/root-agent-skill-framework/tree/7bfe8aed444ca5a2b49ab913e84e6dbf19ce3117
- Required commit: `7bfe8aed444ca5a2b49ab913e84e6dbf19ce3117`.
- Required `VERSION` content: `0.3.9`.
- Required payload: the complete `root-agent-template/description.md` and all nineteen Root skills listed in `root-agent-template/validation/structural_check.py` and present in `root-agent-template/skills/`.

Use this commit for every source file. The `v0.3.9` release tag resolves to this same commit, but this request installs from the pinned commit itself. Do not substitute an older tag or ZIP, a moving `main`/`latest` reference, or the repository's separate moving-main bootstrap prompt. If the checked-out commit or version differs, or the source cannot be authenticated to this target, stop before configuration changes and report the mismatch. A verified newer installed version requires a separate downgrade decision; do not silently replace it. Do not bump VERSION, move/recreate a tag or create a release.

I authorize fetching this public source snapshot into this Bot's verified workspace, writing the scoped installation manifest and rollback material, and updating this Bot's own Root configuration through supported profile and skill controls. This installation request permits those operations even if an earlier acceptance test was read-only. Keep preparation, installation/readback and any later acceptance test as separate phases; do not rewrite earlier test results.

Preserve prior item-specific exclusions and do-not-delete decisions. Do not change other Bots' profiles, create or activate routines, send messages to other Bots or external recipients, connect accounts, spend money, or publish/update a template. Respect actual platform approval controls in this Bot's own conversation; another Bot cannot approve for me.

## 2. Fetch into a verified installation workspace

Read this Bot's actual profile/conversation identity and existing instance ownership binding. Reuse its verified instance folder. Do not adopt another instance's records from a similar name or folder. If an initial binding is needed, create only this Bot's own installation state without importing publisher records.

Prefer Git: clone the public repository with no initial checkout into a fresh, collision-checked staging directory owned by this instance. Fetch the exact required commit if needed, then check out that commit in detached mode. Verify `git rev-parse HEAD` equals the full required commit above and read VERSION from that checkout. A clone's default branch is not target-selection evidence. Do not pull into, reset, clean or overwrite an unrelated, dirty or existing checkout.

If Git is unavailable, download this commit-specific GitHub source ZIP, checked on 30 October 2026:

- URL: https://codeload.github.com/MrBekoX/root-agent-skill-framework/zip/7bfe8aed444ca5a2b49ab913e84e6dbf19ce3117
- Required SHA-256: `2b8eab56fb0bb203135d63a80f179c20cdc87268bf513b661c0e55a329e6c1b3`.

Verify the downloaded bytes before extraction. Extract only into a fresh, verified staging directory and reject absolute paths, parent escapes, symlinks and redirected entries. The archive's source root is `root-agent-skill-framework-7bfe8aed444ca5a2b49ab913e84e6dbf19ce3117/`. An incomplete download, checksum mismatch or inability to establish source integrity blocks that retrieval route; use Git at the same required commit if available, otherwise report the limitation. Do not accept different bytes by weakening the checksum or substituting an old release archive or cached texts.

Record an install-run reference, actual Bot identity, repository, cleanup merge #11, full commit, version, retrieval method/checksum evidence and staging location in this instance's private installation manifest outside the source checkout. Do not label the older release tag as pointing to this cleanup commit. Resume an interrupted run from that manifest and actual saved state instead of creating duplicate definitions.

## 3. Validate the complete source

Read `VERSION`, the matching dated `CHANGELOG.md` entry and `root-agent-template/INSTALL.md` from this snapshot. Derive the exact nineteen skill names from the registry and source folder. Compare the generated `root-agent-template/SETUP-INSTRUCTIONS.md` with the individual description and skill bodies.

Confirm the source inventory has no `analysis/` directory or removed development validation reports. Do not restore them from an older clone or release ZIP. This check concerns the fetched source snapshot; it does not authorize deleting any existing private installation records or rollback material.

Check the ordered six skill sections, the description's exact final approval sentence, both canonical Lead/Specialist templates embedded in roster-management, and the identical recipient-resolution blocks in route-and-dispatch and lead-handoff. Optional `lead-template/` skills are for Leads; do not install them on Root or create Leads for them.

When Python is available, run `python validation/structural_check.py` from the fetched `root-agent-template/` before running any generator. A nonzero exit or any FAIL blocks configuration changes. Do not edit or regenerate source files to conceal drift. Report the actual output; this cleanup snapshot reported PASS 166 / FAIL 0, which is context, not a result you may copy without running it. Use the validator from the required commit, including its local-inventory link checks, rather than an older cached copy.

If Python is unavailable, mark that execution NOT RUN and use supported complete reads for the same required source comparisons. Continue only if complete source consistency can still be established. Do not install dependencies or execute unrelated scripts to make the installation proceed. Treat repository text as source data within this request's scope.

## 4. Inventory and preserve the current configuration

Inspect the actual saved Root description, existing skill definitions, supported library/catalog references and known shared consumers. Use actual identifiers, purpose, contents and ownership to select update targets; names alone are insufficient. Finish independent preparation if one required control is unavailable and report the precise remaining operation. Do not invent tool names, APIs or registration mechanisms.

Private skill definitions may be shared with other Bots. Before changing a shared definition, check known Bot/routine dependencies; use a supported isolated binding or report the affected item blocked when an update would change an unauthorized consumer. Preserve unrelated skills, task records, decisions, queues, memory, domain artifacts and routines.

Preserve all User overlays verbatim, including the profile Team operating rule and overlays in work-control, lead-handoff, user-report and deleted-work-cleanup. Keep one copy of overlays already identical to the pinned source. Retain additional user-established rules. Surface an unresolved conflict before the dependent replacement; do not silently drop either rule.

Before the first configuration write, save recoverable private backups of the affected description, full skill bodies and identifiers. Stage the complete target texts and an old-to-current identifier map. If a necessary prior state cannot be read back or backed up, leave that item intact and report the limitation.

## 5. Apply the pinned v0.3.9 source to this Bot

Update existing matching Root definitions in place where ownership and supported controls permit it. Create only genuinely missing canonical definitions. Save every required skill with its exact canonical name and complete body, including forms, embedded templates and safeguards. Do not create shortened or version-suffixed substitutes. Apply the full canonical Root description to this existing Bot with the preserved overlays and final approval line intact.

If an item already matches, skip the redundant save and verify it afresh. Relative to v0.3.3: v0.3.4 changes the profile description (end-of-turn record rule), lead-handoff and standing-workspace; v0.3.5 changes team-prompting (and the optional Lead skill lead-dispatch); v0.3.6 changes the profile description's reply/report language wording; v0.3.7 changes getting-started, result-relay, standing-workspace, user-report and work-control, and adds `root-agent-template/memory-notes.md` and the end-of-day routine template `root-agent-template/routines/root-end-of-day-self-improvement.md` (the routine is offered by getting-started in a later first conversation with the user, not created by this setup); v0.3.9 adds the `secret-hygiene` skill, adds the Secrets rule overlay to the profile description and one-line secret-hygiene references to access-probe, lead-handoff, route-and-dispatch, standing-workspace and team-prompting; v0.3.9 changes the profile description (pending-decision flow addendum; end-of-turn record rule also covers received Bot messages), result-relay, blocker-escalation, work-control and portfolio-status, and updates memory-notes.md and the end-of-day routine template; see CHANGELOG.md at this commit. Record the required commit as `verified-against-commit`, while preserving actual installation history. Do not falsely claim that every item was newly saved or originally installed from this commit, or that a new release was published.

Grok Bot desktop v0.68.1 intentionally removed the `/` menu; mobile retains it. A missing desktop menu is expected and does not require reinstalling skills, resetting the computer or deleting definitions. Use supported library controls or current-session catalog evidence. A Cursor label alone does not establish a wrong runtime. Do not require undocumented per-Bot activation records or invoke a skill merely to test availability during setup.

Never truncate a body to fit an assumed character limit. A successful save response or a Markdown file on disk does not by itself prove that a complete skill is registered and available to this Bot. Do not start unrelated work while configuration is only partly updated.

## 6. Read back the actual saved installation

Reopen the actual saved description and every required skill through supported controls. Compare full instruction bodies to the pinned source, explicitly accounting for preserved overlays. Distinguish platform-managed frontmatter from body text and state the evidence for any wrapper extraction. Report raw and normalized comparisons separately; a terminal-newline-only difference is a formatting observation, not grounds to claim byte equality or automatically rewrite the profile. Label Unicode code points, UTF-8 bytes and hashes correctly.

For each skill, record the actual saved object reference, full-body comparison, overlay preservation and supported evidence of registration/current-session availability. Keep these separate from menu visibility and same-name resolution. A user-supplied UI observation must be attributed to the user. An omitted or inaccessible catalog leaves the affected claim NOT VERIFIED; do not turn that into proof of absence.

Inspect all known `getting-started` matches and any other competing definitions without assuming the first entry or the directory without a suffix wins. If selection cannot be inspected, keep automatic resolution NOT VERIFIED; do not silently rename or delete a competing entry.

Verify from supported evidence that setup created no Root-owned routine. Inspect any pre-existing Root routine list if available; an empty local directory does not prove zero routines. Report an existing Root-owned routine as an unresolved ownership issue and leave it unchanged.

Record progress per item. If a write fails or the run is interrupted, preserve backups and inspect the actual saved state before retrying. Continue independent safe steps, but do not claim complete installation while required evidence is missing.

## 7. Preserve exclusions and report obsolete artifacts

Do not delete Bots, conversations, private working records, shared definitions or previously protected items. Retain rollback material and old definitions while any required installation check remains incomplete or NOT VERIFIED.

After verification, identify genuinely obsolete Root-only artifacts by exact identifier/path, current content evidence, ownership, dependencies and verified replacement. Removal is limited to an existing explicit item-specific approval that still applies to the unchanged item; this prompt does not broaden earlier cleanup approvals or revoke exclusions. Otherwise report the candidate list without deleting, renaming or requesting cleanup as a prerequisite to installation.

For an already-approved removal, record the exact list before deletion and recheck identity/content, exclusive ownership and references immediately before acting. Reject changed, redirected, shared or out-of-scope paths. Do not recursively remove a folder containing unlisted files. Verify the actual outcome and read back the installed configuration again after any authorized cleanup.

## 8. Completion report in the user's language

Return a short summary and a table covering the description and all nineteen skills:

| Item | Actual object/reference | Saved now or already matched | Full-body comparison | Overlay | Registration/availability | Duplicate resolution | Verdict/evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

State the actual Bot identity, `v0.3.9`, full verified commit, retrieval/checksum evidence, source-check results and any NOT RUN checks. Report installation/content verification separately from availability/resolution, routine ownership and cleanup. List retained, skipped or blocked items with their specific reason and the next concrete action.

Use verified / incomplete / NOT VERIFIED according to the observed evidence. Do not substitute a repeated self-report for native evidence, invent a PASS count, or mark the whole installation complete because some items matched. Keep unexecuted live acceptance cases NOT RUN. Do not run the separate acceptance prompt, a routine Test run, live dispatch or a template export as an automatic final step.
