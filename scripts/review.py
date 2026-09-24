"""Pick a random solved problem and walk through it: question -> notes -> code."""

import random
import re
import sys
from pathlib import Path

SOLUTIONS = Path(__file__).resolve().parent.parent / "solutions"

BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def header(text: str) -> None:
    print(f"\n{BOLD}{CYAN}── {text} {'─' * max(0, 60 - len(text))}{RESET}\n")


def wait(prompt: str) -> str:
    try:
        return input(f"\n{DIM}{prompt}{RESET}").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        sys.exit(0)


def solved_problems() -> list[Path]:
    return sorted(p.parent for p in SOLUTIONS.glob("*/solution.py"))


def solution_code(folder: Path) -> str:
    source = (folder / "solution.py").read_text()
    match = re.search(r"# @lc code=begin\n(.*?)# @lc code=end", source, re.S)
    return (match.group(1) if match else source).strip()


def main() -> None:
    problems = solved_problems()
    if not problems:
        print("No solved problems found.")
        return

    folder = random.choice(problems)
    notes = folder / "notes.md"

    header("Question")
    print((folder / "question.md").read_text().strip())
    print(f"\n{YELLOW}Try to recall the idea and its complexity before revealing the notes.{RESET}")

    if notes.exists():
        wait("Press Enter to reveal the notes...")
        header("Notes")
        print(notes.read_text().strip())
    else:
        print(f"\n{YELLOW}No notes yet for {folder.name} — add solutions/{folder.name}/notes.md{RESET}")

    if wait("Show code? [y/N] ") == "y":
        header("Solution")
        print(solution_code(folder))
    print()


if __name__ == "__main__":
    main()
