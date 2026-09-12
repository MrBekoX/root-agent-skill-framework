# Configure and share Root Agent in the desktop app

The user shares the configured Bot through the desktop app's **Share template** action. The official documentation describes this as sharing a Bot's public link. This workspace supplies the English description and skill text; no separate template file or import package is needed.

For remote-control convenience, [SETUP-INSTRUCTIONS.md](SETUP-INSTRUCTIONS.md) contains the current description and all sixteen skill bodies in one attachment. Give it to the intended Bot and ask it to configure that Bot, save/enable the sixteen skills and verify the results. This is a written setup request, not a native import format. A Windows `D:` path refers to the user's local computer, so the Bot needs permitted local-computer access to read that path; otherwise attach the file through the composer. [Local computer access](https://docs.x.ai/grok-bot/computer-and-apps), [file attachments](https://docs.x.ai/grok-bot/files-and-results).

## 1. Set the description

Open the intended Bot's profile, set its name to **Root Agent**, and paste the full contents of [description.md](description.md) into Description. Save and reopen it to verify that all text is present. If the Bot already exists, use it rather than creating a duplicate. [Create and manage Bots](https://docs.x.ai/grok-bot/bots).

## 2. Save and enable the skills

Use the sixteen instruction bodies linked in the [README](README.md) to create or update the corresponding skills in Grok Bot. For an existing ten-skill setup, update all ten and add scope-guard, access-probe, lead-handoff, blocker-escalation, portfolio-status and result-relay; the updates are not optional, because the earlier texts told Root Agent to prompt every team member itself. Keep the canonical specialist and Lead descriptions embedded in roster-management, the prompt forms inside team-prompting, the handoff package form inside lead-handoff, and the recipient-resolution block identical in route-and-dispatch and lead-handoff. Check that each saved skill is enabled for Root Agent; if it is missing from the `/` menu, inspect Settings → Plugins → Yours and its Bot enablement. [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations).

For a real team task, Root Agent sizes the structure, composes and verifies each new Bot's tailored description, and then either prompts the owner directly or delegates the domain to a Lead that prompts its own members. Root Agent keeps reviewer selection in every tier. Existing unrelated Bot roles are not silently rewritten. The optional Lead-side skills in [lead-template](../lead-template/README.md) are installed by hand on a Lead Bot; a Bot cannot register skills for another Bot. The user's task authority covers necessary specialist creation and scoped internal handoffs. Do not pre-create a team or activate monitoring simply while saving these skills.

Test written methods with safe real tasks and refine them from the results. Before scheduling recurring work, establish a successful task, saved method, second input test and failure/retry behavior. Root Agent delegates recurring execution to its specialist owner. [Use cases](https://docs.x.ai/grok-bot/use-cases).

## 3. Share the configured Bot

Use **Share template** on Root Agent in the desktop app and share its public link. The label is supplied by the user's app; the official guide describes copying the Bot's share link and the recipient choosing **Add to Grok Bot**. The recipient adds only Root Agent, using the application to finish the flow. [Share a Bot](https://docs.x.ai/grok-bot/bots).

The shared configuration includes identity, description, skills and routines. Check that it contains no private data and that Root Agent has no unintended owned routines. The recipient gets a copy, without your computer, logins or conversation history. Their instance establishes its own profile and access. [Share a Bot](https://docs.x.ai/grok-bot/bots).

## Optional verification reference

[Acceptance checks](validation/acceptance.md) contains suggested behavioral scenarios and the source coverage review. Local checks have been performed; live Bot behavior and public-preview contents have not been verified from this workspace. You do not need to return installation logs to complete the description and skill-writing work.
