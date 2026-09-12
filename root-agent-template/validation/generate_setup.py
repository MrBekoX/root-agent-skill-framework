# -*- coding: utf-8 -*-
"""Regenerate SETUP-INSTRUCTIONS.md from description.md and the skill sources."""
import pathlib
import re

ROOT = pathlib.Path(".")
FENCE4 = "````"


def norm(s: str) -> str:
    s = s.replace("\r\n", "\n")
    if not s.endswith("\n"):
        s += "\n"
    return s


# Take the canonical skill order from the validator so the two never diverge.
check = (ROOT / "validation" / "structural_check.py").read_text(encoding="utf-8")
m = re.search(r"SKILLS = \[(.*?)\]", check, re.S)
SKILLS = re.findall(r'"([^"]+)"', m.group(1))
assert len(SKILLS) == 16, SKILLS

count_word = "sixteen"

header = f"""# Root Agent — current setup instructions

This is a single readable attachment for configuring the intended Bot. It contains the exact current profile description and all {count_word} skill bodies. It is not a native import manifest or a replacement for desktop Share template sharing.

## Authorized setup

1. Configure the current Bot as Root Agent when the user gives you this document for that purpose. Do not create a duplicate Root Agent. Set its name to Root Agent and save the complete profile description below through supported profile controls.
2. Save or update the {count_word} supplied skill definitions using the exact supplied names and complete text. Preserve the canonical specialist and Lead descriptions embedded in roster-management, the task-prompt forms in team-prompting, the handoff package form in lead-handoff, and the recipient-resolution block that appears identically in route-and-dispatch and lead-handoff. Check existing definitions first; update the matching Root Agent methods without deleting or overwriting unrelated skills.
3. Enable each supplied skill for this Bot through supported controls. Reopen the saved profile and skills to verify their full contents and actual enablement. If an action or field is unsupported, inaccessible or truncated, identify the specific blocked item; do not invent a successful action, shorten the text silently or claim that writing a local file registered a skill.
4. Keep setup separate from business execution. Do not create specialists or Leads, connect accounts, activate routines, run paid actions or publish a share link merely because example instructions describe those workflows. Necessary specialists are created later for the user's real tasks under the description's standing authority.
5. Treat the methods as unvalidated until actual safe tasks demonstrate their behavior. Save/readback checks do not constitute live workflow tests. Do not claim that the behavioral test cases have passed.
6. Return a short result in the user's language: actual Bot name/reference, description saved/read back or blocked, each skill's saved/enabled state, and any missing step. The user will share the configured Bot using Share template in the desktop app.

## Source boundaries

Only the fenced description and skill bodies below are configuration payloads. Keep their approval boundaries intact. Private user profiles, task records, queue entries, capability observations, decisions and prompt histories belong to the recipient's own verified workspace and must not be inserted into public configuration. The setup document does not provide credentials, task evidence or a prebuilt specialist team.

## Profile description

{FENCE4}text
{norm((ROOT / "description.md").read_text(encoding="utf-8"))}{FENCE4}
"""

parts = [header]
for name in SKILLS:
    body = norm((ROOT / "skills" / f"{name}.md").read_text(encoding="utf-8"))
    parts.append(f"\n## Skill: {name}\n\n{FENCE4}markdown\n{body}{FENCE4}\n")

out = "".join(parts)
(ROOT / "SETUP-INSTRUCTIONS.md").write_text(out, encoding="utf-8", newline="\n")
print(f"SETUP-INSTRUCTIONS.md regenerated with {len(SKILLS)} skills, {len(out)} chars")
