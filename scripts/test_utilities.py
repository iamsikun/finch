"""Regression tests: python -m unittest discover -s scripts -p 'test_*.py'."""

import contextlib
import hashlib
import importlib.util
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "extract_pdf", ROOT / "skills/finch/scripts/extract_pdf.py"
)
pdf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pdf)


class ExtractionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / "paper with spaces.pdf"
        self.source.write_bytes(b"%PDF-1.4\nfixture")
        self.output = Path(self.temp.name) / "reading.txt"

    def run_helper(self, extracted):
        result = subprocess.CompletedProcess([], 0, extracted, b"")
        with patch.object(sys, "argv", ["extract_pdf", str(self.source), str(self.output)]), \
             patch.object(pdf.shutil, "which", return_value="pdftotext"), \
             patch.object(pdf.subprocess, "run", return_value=result), \
             contextlib.redirect_stdout(io.StringIO()), \
             contextlib.redirect_stderr(io.StringIO()):
            return pdf.main()

    def test_page_indices_survive_empty_middle_and_final_pages(self):
        self.assertEqual(self.run_helper(b"First page\f\fThird page\f\f"), 0)
        text = self.output.read_text()
        self.assertIn("PDF pages: 4", text)
        self.assertIn("===== PDF page 3 =====\nThird page", text)
        self.assertIn("===== PDF page 4 =====", text)
        self.assertIn(hashlib.sha256(self.source.read_bytes()).hexdigest(), text)
        self.assertIn("Sparse pages (<40 non-whitespace characters): [1, 2, 3, 4]", text)

    def test_refuses_to_overwrite(self):
        self.output.write_text("existing notes")
        self.assertEqual(self.run_helper(b"new content\f"), 1)
        self.assertEqual(self.output.read_text(), "existing notes")

    def test_rejects_html_download(self):
        self.source.write_text("<html>Sign in to download</html>")
        self.assertEqual(self.run_helper(b"fake paper\f"), 1)
        self.assertFalse(self.output.exists())

    def test_missing_page_boundary_is_not_silent(self):
        self.assertEqual(self.run_helper(b"no page boundary"), 1)
        self.assertFalse(self.output.exists())

    def test_missing_dependency_is_actionable(self):
        with patch.object(pdf.shutil, "which", return_value=None):
            with self.assertRaisesRegex(ValueError, "Poppler"):
                pdf.extract(self.source)

    def test_extractor_failure_is_not_written_as_evidence(self):
        result = subprocess.CompletedProcess([], 1, b"partial output", b"encrypted PDF")
        with patch.object(pdf.shutil, "which", return_value="pdftotext"), \
             patch.object(pdf.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(ValueError, "encrypted PDF"):
                pdf.extract(self.source)


@unittest.skipUnless(shutil.which("git") and shutil.which("bash"), "git and bash required")
class UpdateTests(unittest.TestCase):
    def git(self, directory, *args):
        return subprocess.run(
            ["git", "-C", str(directory), "-c", "user.name=Finch Test",
             "-c", "user.email=finch-test@example.invalid", "-c", "commit.gpgsign=false", *args],
            check=True, capture_output=True, text=True,
        ).stdout.strip()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = Path(self.temp.name)
        self.remote, self.install = base / "remote", base / "installed"
        self.remote.mkdir()
        self.git(self.remote, "init", "-b", "stable")
        skill = self.remote / "skills/finch"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text('metadata:\n  version: "0.1.0"\n')
        (self.remote / "notes.txt").write_text("original\n")
        self.git(self.remote, "add", ".")
        self.git(self.remote, "commit", "-m", "initial")
        self.git(base, "clone", str(self.remote), str(self.install))
        self.before = self.git(self.install, "rev-parse", "HEAD")
        (skill / "SKILL.md").write_text('metadata:\n  version: "0.2.0"\n')
        self.git(self.remote, "commit", "-am", "release")
        self.env = dict(os.environ, FINCH_HOME=str(self.install), FINCH_REF="stable",
                        XDG_STATE_HOME=str(base / "state"))

    def update(self):
        return subprocess.run(
            ["bash", str(ROOT / "install.sh"), "update"], env=self.env,
            check=True, capture_output=True, text=True,
        ).stdout

    def test_clean_install_fast_forwards(self):
        self.assertIn("updated 0.1.0 -> 0.2.0", self.update())
        self.assertEqual(self.git(self.install, "rev-parse", "HEAD"),
                         self.git(self.remote, "rev-parse", "HEAD"))

    def test_unrelated_tracked_edit_blocks_update(self):
        (self.install / "notes.txt").write_text("personal edits\n")
        self.assertIn("skipping update", self.update())
        self.assertEqual(self.git(self.install, "rev-parse", "HEAD"), self.before)
        self.assertEqual((self.install / "notes.txt").read_text(), "personal edits\n")

    def test_untracked_file_blocks_update(self):
        (self.install / "private-note.txt").write_text("my note")
        self.assertIn("skipping update", self.update())
        self.assertEqual(self.git(self.install, "rev-parse", "HEAD"), self.before)


if __name__ == "__main__":
    unittest.main()
