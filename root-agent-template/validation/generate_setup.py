# -*- coding: utf-8 -*-
"""Regenerate SETUP-INSTRUCTIONS.md from description.md and the skill sources."""
import ast
import os
import pathlib
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
FENCE4 = "````"


def norm(s: str) -> str:
    s = s.replace("\r\n", "\n")
    if not s.endswith("\n"):
        s += "\n"
    return s


def skill_names(root: pathlib.Path) -> list[str]:
    """Read the static registry without executing the validator or relying on asserts."""
    tree = ast.parse((root / "validation" / "structural_check.py").read_text(encoding="utf-8"))
    assignments = [node for node in tree.body if isinstance(node, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == "SKILLS" for t in node.targets)]
    if len(assignments) != 1:
        raise ValueError("expected one static SKILLS list in structural_check.py")
    names = ast.literal_eval(assignments[0].value)
    if (not isinstance(names, list) or not names
            or any(not isinstance(name, str) or not name for name in names)
            or len(names) != len(set(names))):
        raise ValueError("SKILLS must be a nonempty list of unique names")
    if sorted(names) != sorted(p.stem for p in (root / "skills").glob("*.md")):
        raise ValueError("SKILLS list and skills/ differ")
    return names

WORDS = {16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty"}
def render_setup(root: pathlib.Path = ROOT) -> str:
    skills = skill_names(root)
    count_word = WORDS.get(len(skills), str(len(skills)))

    header = f"""# Root Agent — current setup instructions

This is a single readable attachment for configuring the intended Bot. It contains the exact current profile description and all {count_word} skill bodies. It is not a native import manifest or a replacement for desktop Share template sharing.

## Authorized setup

1. Configure the current Bot as Root Agent when the user gives you this document for that purpose. Do not create a duplicate Root Agent. Set its name to Root Agent and save the complete profile description below through supported profile controls.
2. Save or update the {count_word} supplied skill definitions using the exact supplied names and complete text. Preserve the canonical specialist and Lead descriptions embedded in roster-management, the task-prompt forms in team-prompting, the handoff package form in lead-handoff, and the recipient-resolution block that appears identically in route-and-dispatch and lead-handoff. Preserve existing User overlay text verbatim and retain the current explicit precedence/exception rules; report any unresolved local overlay conflict before dependent execution. Check existing definitions first; update the matching Root Agent methods without deleting or overwriting unrelated skills. Inspect the supported library and Bot availability controls rather than assuming a particular UI label or cross-Bot installation capability.
3. Enable each supplied skill for this Bot through supported controls. Reopen the saved profile and skills to verify their full contents and actual enablement. The fenced bodies below are the full procedures; do not shorten a skill body to fit a host limit, and do not keep a shortened variant beside the full text. A truncated host save is a failed setup. If an action or field is unsupported, inaccessible or truncated, identify the specific blocked item; do not invent a successful action, shorten the text silently or claim that writing a local file registered a skill.
4. Keep setup separate from business execution. Do not create specialists or Leads, connect accounts, activate routines, run paid actions or publish a share link merely because example instructions describe those workflows. Necessary specialists are created later for the user's real tasks under the description's standing authority.
5. Treat the methods as unvalidated until actual safe tasks demonstrate their behavior. Save/readback checks do not constitute live workflow tests. Do not claim that the behavioral test cases have passed.
6. Return a short result in the user's language: actual Bot name/reference, description saved/read back or blocked, each skill's saved/enabled state, and any missing step. The user will share the configured Bot using Share template in the desktop app.

## Source boundaries

Only the fenced description and skill bodies below are configuration payloads. Keep their approval boundaries intact. Private user profiles, task records, queue entries, capability observations, decisions and prompt histories belong to the recipient's own verified workspace and must not be inserted into public configuration. The setup document does not provide credentials, task evidence or a prebuilt specialist team.

## Profile description

{FENCE4}text
{norm((root / "description.md").read_text(encoding="utf-8"))}{FENCE4}
"""

    parts = [header]
    for name in skills:
        body = norm((root / "skills" / f"{name}.md").read_text(encoding="utf-8"))
        parts.append(f"\n## Skill: {name}\n\n{FENCE4}markdown\n{body}{FENCE4}\n")
    return "".join(parts)


def main() -> int:
    temporary = None
    try:
        out = render_setup(ROOT)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n",
                                         dir=ROOT, prefix=".setup-", suffix=".tmp",
                                         delete=False) as stream:
            temporary = pathlib.Path(stream.name)
            stream.write(out)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, ROOT / "SETUP-INSTRUCTIONS.md")
        print(f"SETUP-INSTRUCTIONS.md regenerated with {len(skill_names(ROOT))} skills, {len(out)} Unicode code points (LF)")
        return 0
    except (OSError, ValueError, SyntaxError) as exc:
        print(f"ERROR: setup generation failed: {exc}", file=sys.stderr)
        return 1
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


if __name__ == "__main__":
    sys.exit(main())
