# -*- coding: utf-8 -*-
"""Structural checks against shipped Root Agent source texts (not live Grok Bot).

Reads description.md, SETUP-INSTRUCTIONS.md, the ten skills, and the canonical
specialist description. Does not call Grok Bot and does not simulate C01–C42.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SENT = "Sending messages, publishing, deleting, purchasing, and production or account changes always require approval."
HEADINGS = [
    "## When to use",
    "## Required inputs and access",
    "## Sequence of work",
    "## Validate the result",
    "## What to return",
    "## What requires approval",
]
SKILLS = [
    "intake-clarify",
    "scope-guard",
    "work-control",
    "roster-management",
    "access-probe",
    "team-prompting",
    "route-and-dispatch",
    "lead-handoff",
    "quality-review",
    "blocker-escalation",
    "standing-workspace",
    "bind-routine-via-owner",
    "learning-loop",
    "portfolio-status",
    "result-relay",
    "user-report",
]
RESOLUTION_FIRST = "Recipient resolution (identical text in route-and-dispatch and lead-handoff)"
RESOLUTION_LAST = "Never send the same work unit through both."
FENCE4 = "````"
fails: list[str] = []
passes: list[str] = []


def fail(msg: str) -> None:
    fails.append(msg)


def ok(msg: str) -> None:
    passes.append(msg)


def norm(s: str) -> str:
    s = s.replace("\r\n", "\n")
    if not s.endswith("\n"):
        s += "\n"
    return s


def extract_fence(src: str, heading: str, lang: str) -> str | None:
    needle = f"## {heading}\n\n{FENCE4}{lang}\n"
    i = src.find(needle)
    if i < 0:
        return None
    start = i + len(needle)
    end = src.find(f"\n{FENCE4}", start)
    if end < 0:
        return None
    return src[start:end] + "\n"


for rel in ["description.md", "SETUP-INSTRUCTIONS.md", "INSTALL.md", "README.md", "templates/specialist-description.md", "templates/lead-description.md"]:
    p = ROOT / rel
    (ok if p.is_file() else fail)(f"exists {rel}")
for name in SKILLS:
    p = ROOT / "skills" / f"{name}.md"
    (ok if p.is_file() else fail)(f"exists skills/{name}.md")

for name in SKILLS:
    text = (ROOT / "skills" / f"{name}.md").read_text(encoding="utf-8")
    missing = [h for h in HEADINGS if h not in text]
    if missing:
        fail(f"{name} missing headings {missing}")
    else:
        ok(f"{name} six headings")

for rel in ["description.md", "templates/specialist-description.md", "templates/lead-description.md"]:
    t = (ROOT / rel).read_text(encoding="utf-8").replace("\r\n", "\n").rstrip()
    last = t.split("\n")[-1]
    if last == SENT:
        ok(f"{rel} last line exact approval sentence")
    else:
        fail(f"{rel} last line mismatch: {last!r}")

roster = (ROOT / "skills" / "roster-management.md").read_text(encoding="utf-8").replace("\r\n", "\n")
fences = re.findall(r"```text\n(.*?)```", roster, re.S)
if len(fences) != 2:
    fail(f"roster canonical blocks: expected 2 (specialist, lead), found {len(fences)}")
else:
    for idx, (label, rel) in enumerate(
        [("specialist", "templates/specialist-description.md"), ("lead", "templates/lead-description.md")]
    ):
        block = fences[idx]
        last = block.rstrip().split("\n")[-1]
        if last == SENT:
            ok(f"roster {label} embed last line exact")
        else:
            fail(f"roster {label} embed last line mismatch: {last!r}")
        src = norm((ROOT / rel).read_text(encoding="utf-8"))
        if src == norm(block):
            ok(f"{rel} matches roster {label} embed")
        else:
            fail(f"{rel} != roster {label} embed")

# The recipient-resolution rule must be byte-identical in both senders.
_blocks = []
for name in ("route-and-dispatch", "lead-handoff"):
    t = (ROOT / "skills" / f"{name}.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    i = t.find(RESOLUTION_FIRST)
    j = t.find(RESOLUTION_LAST)
    if i < 0 or j < 0:
        fail(f"{name} missing recipient-resolution block")
        _blocks.append(None)
    else:
        _blocks.append(t[i:j + len(RESOLUTION_LAST)])
if all(_blocks) and _blocks[0] == _blocks[1]:
    ok("recipient-resolution block identical in both senders")
elif all(_blocks):
    fail("recipient-resolution block differs between senders")

# No skill may still claim Root Agent prompts every assigned Bot.
_banned = "writes a distinct prompt for every Bot it assigns"
_hits = [n for n in SKILLS if _banned in (ROOT / "skills" / f"{n}.md").read_text(encoding="utf-8")]
if _hits:
    fail(f"superseded Root-prompts-every-Bot rule still present in {_hits}")
else:
    ok("no skill claims Root Agent prompts every assigned Bot")

setup = (ROOT / "SETUP-INSTRUCTIONS.md").read_text(encoding="utf-8").replace("\r\n", "\n")
desc_setup = extract_fence(setup, "Profile description", "text")
desc_file = norm((ROOT / "description.md").read_text(encoding="utf-8"))
if desc_setup is None:
    fail("SETUP description fence missing")
elif norm(desc_setup) == desc_file:
    ok("SETUP description matches description.md")
else:
    fail("SETUP description drift")
for name in SKILLS:
    body = extract_fence(setup, f"Skill: {name}", "markdown")
    src = norm((ROOT / "skills" / f"{name}.md").read_text(encoding="utf-8"))
    if body is None:
        fail(f"SETUP skill fence missing {name}")
    elif norm(body) == src:
        ok(f"SETUP {name} matches skills/{name}.md")
    else:
        fail(f"SETUP {name} drift")

desc = (ROOT / "description.md").read_text(encoding="utf-8")
if "never to Root Agent" in desc and "Recurring work belongs to its specialist owner" in desc:
    ok("description forbids Root-owned routine")
else:
    fail("description missing Root-owned routine prohibition")

if "create a necessary specialist Bot for the requested task without asking again" in desc:
    ok("standing specialist-create authority present")
else:
    fail("standing specialist-create missing")
if "not a private fixed Bot budget" in desc:
    ok("platform capacity not 20-Bot budget")
else:
    fail("platform capacity sentence missing")

if "avoid a long setup questionnaire or an unsolicited team" in desc:
    ok("first-run: no unsolicited team")
else:
    fail("first-run unsolicited-team sentence missing")
if "without inheriting another copy's personal records" in desc:
    ok("first-run: no inherited profile")
else:
    fail("inherited-profile sentence missing")

payload = desc
for name in SKILLS:
    payload += (ROOT / "skills" / f"{name}.md").read_text(encoding="utf-8")
payload += (ROOT / "templates" / "specialist-description.md").read_text(encoding="utf-8")
payload += (ROOT / "templates" / "lead-description.md").read_text(encoding="utf-8")
for pat, label in [
    (r"AKIA[0-9A-Z]{16}", "AWS key"),
    (r"sk-[A-Za-z0-9]{20,}", "sk- token"),
    (r"ghp_[A-Za-z0-9]{20,}", "github token"),
    (r"-----BEGIN", "PEM"),
    (r"(?i)mrbeko", "publisher handle"),
    (r"C:\\\\Users", "C:\\Users path"),
    (r"D:\\\\", "D:\\\\ path"),
    (r"https?://", "absolute URL"),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "email"),
]:
    if re.search(pat, payload):
        fail(f"payload hygiene hit: {label}")
    else:
        ok(f"payload clean of {label}")

install = (ROOT / "INSTALL.md").read_text(encoding="utf-8")
if (
    "Share template" in install
    and "Share a Bot" in install
    and "no separate template file or import package" in install.lower()
):
    ok("INSTALL aligns Share template with Share a Bot, no import package")
else:
    fail("INSTALL share-alignment wording incomplete")

acc = (ROOT / "validation" / "acceptance.md").read_text(encoding="utf-8")
if "not run" in acc.lower() and "NOT RUN" in acc:
    ok("acceptance.md keeps live cases NOT RUN")
else:
    fail("acceptance.md does not keep NOT RUN")

print(f"PASS {len(passes)}  FAIL {len(fails)}")
for msg in passes:
    print("  OK  ", msg)
for msg in fails:
    print("  FAIL", msg)
sys.exit(1 if fails else 0)
