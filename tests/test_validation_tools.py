"""Local tooling regressions. These do not execute a Grok Bot scenario."""
from __future__ import annotations

import importlib.util
import io
from contextlib import redirect_stderr
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO = Path(__file__).resolve().parents[1]
VALIDATION = REPO / "root-agent-template" / "validation"


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, VALIDATION / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


check = load_tool("structural_check")
generate = load_tool("generate_setup")


def temporary_directory():
    # Restricted runners can name an explicitly writable fixture directory.
    base = Path(os.environ.get("ROOT_AGENT_TEST_TMP", tempfile.gettempdir())).resolve()
    temporary = tempfile.TemporaryDirectory(dir=base)
    target = Path(temporary.name).resolve()
    if target.parent != base or target == base:
        raise RuntimeError("fixture cleanup target escaped its temporary base")
    return temporary


class SourceContracts(unittest.TestCase):
    def test_sections_reject_duplicate_extra_reordered_and_fenced_only(self):
        correct = "\n\n".join(check.HEADINGS)
        self.assertEqual(check.skill_headings(correct), check.HEADINGS)
        for text in (correct + "\n## When to use", correct + "\n## Extra",
                     "\n".join(reversed(check.HEADINGS)), "```markdown\n" + correct + "\n```"):
            self.assertNotEqual(check.skill_headings(text), check.HEADINGS)
        self.assertEqual(check.skill_headings(correct + "\n```text\n## Example\n```"), check.HEADINGS)

    def test_recipient_comparison_retains_newline_bytes(self):
        block = (check.RESOLUTION_FIRST + "\nrule\n" + check.RESOLUTION_LAST).encode()
        self.assertNotEqual(check.recipient_block(block), check.recipient_block(block.replace(b"\n", b"\r\n")))
        self.assertIsNone(check.recipient_block(block + block))
        self.assertIsNone(check.recipient_block(check.RESOLUTION_LAST.encode()))

    def test_hygiene_covers_local_network_paths_and_new_token_shape(self):
        samples = [r"Q:\private\sample.txt", "Q:/private/sample.txt", r"\\sample-host\private\sample.txt",
                   "/home/sample/private.txt", "/Users/sample/private.txt", "file:///sample/private.txt",
                   "github_pat_" + "A" * 30, "access_token=" + "A" * 30]
        for sample in samples:
            with self.subTest(sample_class=sample[:4]):
                self.assertTrue(check.hygiene_hits(sample))
        self.assertEqual(check.hygiene_hits("Use /workspace/<domain-slug>/ and the current task."), [])

    def test_registry_accepts_single_quotes_and_rejects_invalid_lists(self):
        with temporary_directory() as temporary:
            root = Path(temporary)
            (root / "validation").mkdir()
            (root / "skills").mkdir()
            (root / "skills" / "sample.md").write_text("example", encoding="utf-8")
            registry = root / "validation" / "structural_check.py"
            registry.write_text("SKILLS = ['sample']\n", encoding="utf-8")
            self.assertEqual(generate.skill_names(root), ["sample"])
            for source in ("SKILLS = []", "SKILLS = ['sample', 'sample']", "SKILLS = ['missing']",
                           "SKILLS = [1]", "OTHER = ['sample']"):
                registry.write_text(source, encoding="utf-8")
                with self.assertRaises(ValueError):
                    generate.skill_names(root)

    def test_failed_atomic_replace_preserves_snapshot_and_cleans_staging_file(self):
        with temporary_directory() as temporary:
            root = Path(temporary)
            (root / "validation").mkdir()
            (root / "skills").mkdir()
            (root / "validation" / "structural_check.py").write_text("SKILLS = ['sample']\n", encoding="utf-8")
            (root / "skills" / "sample.md").write_text("sample skill\n", encoding="utf-8")
            (root / "description.md").write_text("sample description\n", encoding="utf-8")
            snapshot = root / "SETUP-INSTRUCTIONS.md"
            snapshot.write_bytes(b"previous snapshot\n")
            errors = io.StringIO()
            with mock.patch.object(generate, "ROOT", root), \
                    mock.patch.object(generate.os, "replace", side_effect=PermissionError("synthetic failure")), \
                    redirect_stderr(errors):
                self.assertEqual(generate.main(), 1)
            self.assertEqual(snapshot.read_bytes(), b"previous snapshot\n")
            self.assertEqual(list(root.glob(".setup-*.tmp")), [])
            self.assertIn("synthetic failure", errors.getvalue())


class ToolProcessRegressions(unittest.TestCase):
    def setUp(self):
        self.temporary = temporary_directory()
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name) / "fixture"
        shutil.copytree(REPO, self.folder,
                        ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"))
        self.root = self.folder / "root-agent-template"

    def run_tool(self, name, *, optimized=False):
        command = [sys.executable, "-X", "utf8"]
        if optimized:
            command.append("-O")
        command.append(str(self.root / "validation" / f"{name}.py"))
        return subprocess.run(command, cwd=self.temporary.name, capture_output=True,
                              encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"}, timeout=45)

    def test_generator_from_unrelated_directory_is_deterministic(self):
        self.assertEqual(self.run_tool("generate_setup").returncode, 0)
        first = (self.root / "SETUP-INSTRUCTIONS.md").read_bytes()
        self.assertNotIn(b"\r\n", first)
        self.assertEqual(self.run_tool("generate_setup").returncode, 0)
        self.assertEqual(first, (self.root / "SETUP-INSTRUCTIONS.md").read_bytes())
        self.assertFalse((Path(self.temporary.name) / "SETUP-INSTRUCTIONS.md").exists())

    def test_complete_valid_fixture_passes_structural_check(self):
        self.assertEqual(self.run_tool("generate_setup").returncode, 0)
        result = self.run_tool("structural_check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertRegex(result.stdout, r"PASS \d+  FAIL 0")

    def test_generator_missing_source_preserves_existing_snapshot(self):
        snapshot = self.root / "SETUP-INSTRUCTIONS.md"
        previous = snapshot.read_bytes()
        (self.root / "skills" / "intake-clarify.md").unlink()
        result = self.run_tool("generate_setup")
        self.assertEqual(result.returncode, 1)
        self.assertIn("SKILLS list and skills/ differ", result.stderr)
        self.assertEqual(previous, snapshot.read_bytes())

    def test_optimized_python_does_not_disable_registry_validation(self):
        path = self.root / "validation" / "structural_check.py"
        body = path.read_text(encoding="utf-8").replace('"intake-clarify",', '"intake-clarify", "intake-clarify",', 1)
        path.write_text(body, encoding="utf-8")
        result = self.run_tool("generate_setup", optimized=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("unique names", result.stderr)

    def test_missing_file_reports_fail_without_traceback(self):
        (self.root / "skills" / "intake-clarify.md").unlink()
        result = self.run_tool("structural_check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required files", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_setup_header_drift_is_detected(self):
        self.assertEqual(self.run_tool("generate_setup").returncode, 0)
        path = self.root / "SETUP-INSTRUCTIONS.md"
        path.write_text(path.read_text(encoding="utf-8").replace("## Authorized setup", "## Changed setup", 1), encoding="utf-8")
        result = self.run_tool("structural_check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("complete SETUP snapshot drift", result.stdout)

    def test_optional_skill_hygiene_is_checked_without_echoing_value(self):
        path = self.folder / "lead-template" / "skills" / "lead-integrate.md"
        sample = "Q:/private/synthetic-path.txt"
        path.write_text(path.read_text(encoding="utf-8") + "\n" + sample + "\n", encoding="utf-8")
        result = self.run_tool("structural_check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("payload hygiene hit: local drive path", result.stdout)
        self.assertNotIn(sample, result.stdout + result.stderr)

    def test_undated_changelog_entry_is_rejected(self):
        path = self.folder / "CHANGELOG.md"
        body = re.sub(r"(?m)(^## \[\d+\.\d+\.\d+\]) - \d{4}-\d{2}-\d{2}$", r"\1", path.read_text(encoding="utf-8"), count=1)
        path.write_text(body, encoding="utf-8")
        result = self.run_tool("structural_check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("CHANGELOG has headings outside", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
