"""Submit the last problem and, if accepted, remind me to write its notes."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

SOLUTIONS = Path(__file__).resolve().parent.parent / "solutions"

BOLD = "\033[1m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def run_submit() -> str:
    process = subprocess.Popen(
        ["leetgo", "submit", "last"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    output = []
    for line in process.stdout:
        print(line, end="", flush=True)
        output.append(line)
    process.wait()
    return "".join(output)


def find_problem(output: str) -> Path | None:
    match = re.search(r"question=(\S+)", output)
    if match:
        folders = list(SOLUTIONS.glob(f"*.{match.group(1)}"))
        if folders:
            return folders[0]
    solutions = list(SOLUTIONS.glob("*/solution.py"))
    return max(solutions, key=lambda p: p.stat().st_mtime).parent if solutions else None


def notes_missing(folder: Path) -> bool:
    notes = folder / "notes.md"
    # An untouched template from new_notes.py still has empty complexity placeholders.
    return not notes.exists() or "O()" in notes.read_text()


def notify(title: str, message: str) -> None:
    if sys.platform == "darwin":
        script = f'display notification "{message}" with title "{title}"'
        subprocess.run(["osascript", "-e", script], check=False)


def main() -> None:
    output = run_submit()
    if "Accepted" not in output:
        return

    folder = find_problem(output)
    if folder is None or not notes_missing(folder):
        return

    print(f"\n{BOLD}{YELLOW}Accepted! Don't forget to fill in solutions/{folder.name}/notes.md "
          f"(topics, idea, time/space complexity).{RESET}\n")
    notify("LeetCode: accepted 🎉", f"Write notes for {folder.name}")


if __name__ == "__main__":
    main()
