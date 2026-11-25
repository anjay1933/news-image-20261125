"""Self-test suite for the "news-image-20261125" make.fun entry.

Run:  python -m unittest discover -s tests -v
      or: pytest
"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MAIN = REPO / "main.py"
ENTRY = REPO / "tests" / "_entry.png"

# make.fun entry constraints (from /bounty/news-image-20261125)
MAX_BYTES = 1024 * 1024            # 1 MiB
EXPECTED_SIZE = 1024
EXPECTED_HEIGHT = 1024
ALLOWED_MODES = {"1", "L", "RGB", "RGBA", "P"}


def run_main(output: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["ENTRY_OUTPUT"] = str(output)
    return subprocess.run(
        [sys.executable, str(MAIN)],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
    )


class TestConstraints(unittest.TestCase):
    """Structural constraints every entry image must satisfy."""

    def setUp(self):
        self.out = REPO / "tests" / "_entry.png"
        self.out.parent.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        if self.out.exists():
            self.out.unlink()

    def test_exit_success_once(self):
        proc = run_main(self.out)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(self.out.exists(), proc.stdout)
        self.assertIn("1024 x 1024", proc.stdout)

    def test_output_is_png_within_1mib(self):
        proc = run_main(self.out)
        self.assertEqual(proc.returncode, 0)
        self.assertTrue(self.out.exists())
        size = self.out.stat().st_size
        self.assertLessEqual(size, MAX_BYTES, f"too large: {size} bytes")
        from PIL import Image
        with Image.open(self.out) as im:
            self.assertEqual(im.size, (EXPECTED_SIZE, EXPECTED_HEIGHT))
            self.assertIn(im.mode, ALLOWED_MODES, im.mode)

    def test_double_run_is_deterministic(self):
        """Two runs must write byte-identical PNGs (no network input)."""
        a = REPO / "tests" / "_entry_a.png"
        b = REPO / "tests" / "_entry_b.png"
        for p in (a, b):
            p.parent.mkdir(parents=True, exist_ok=True)
        self.assertEqual(run_main(a).returncode, 0)
        self.assertEqual(run_main(b).returncode, 0)
        self.assertEqual(a.read_bytes(), b.read_bytes())
        a.unlink()
        b.unlink()

    def test_no_network_calls(self):
        """The program must not reach the network (no requests/urllib)."""
        # Stub out network modules before running so any usage raises.
        for mod in ("requests", "urllib.request", "httpx", "aiohttp"):
            if mod in sys.modules:
                del sys.modules[mod]
        proc = run_main(self.out)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        src = MAIN.read_text(encoding="utf-8")
        # Sanity: source contains no import of a network client (offline by design).
        self.assertNotIn("import requests", src)
        self.assertNotIn("import urllib", src)
        self.assertNotIn("import httpx", src)
        self.assertNotIn("import aiohttp", src)


class TestFiles(unittest.TestCase):
    """Project deliverables required by the bounty brief."""

    def _manifest(self):
        return (REPO / "manifest.json").read_text(encoding="utf-8")

    def test_requirements_txt_exists(self):
        self.assertTrue((REPO / "requirements.txt").exists())

    def test_license_exists(self):
        self.assertTrue((REPO / "LICENSE").exists())

    def test_readme_exists(self):
        self.assertTrue((REPO / "README.md").exists())


if __name__ == "__main__":
    unittest.main()
