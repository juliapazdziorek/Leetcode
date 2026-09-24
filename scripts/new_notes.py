"""Create an empty notes.md template for a freshly picked problem."""

import re
import sys
from pathlib import Path

SOLUTIONS = Path(__file__).resolve().parent.parent / "solutions"

TEMPLATE = """{title}

**Topics:**
**Time:** O() · **Space:** O()

## Idea


## Pitfalls
-
"""


def main() -> None:
    problem_id = sys.argv[1].zfill(4)
    for folder in SOLUTIONS.glob(f"{problem_id}*/"):
        notes = folder / "notes.md"
        if notes.exists():
            continue
        first = (folder / "question.md").read_text().splitlines()[0]
        match = re.match(r"# \[(.+?)\]\[link\] \((\w+)\)", first)
        title = f"# {match.group(1)} ({match.group(2)})" if match else f"# {folder.name}"
        notes.write_text(TEMPLATE.format(title=title))
        print(f"Created {notes.relative_to(SOLUTIONS.parent)}")


if __name__ == "__main__":
    main()
