# On Windows, run recipes through cmd instead of the default `sh` (which isn't installed).
# Ignored on macOS/Linux, so this file stays portable.
set windows-shell := ["cmd.exe", "/c"]

# Show the list of recipes.
default:
    @just --list

# Fetch a problem into solutions/<id>.<slug>/
new id:
    leetgo pick {{id}} -l python3
    python3 scripts/new_notes.py {{id}}

# Run the last problem's test cases locally.
test:
    leetgo test last -L

# Submit the last problem to LeetCode (reminds you to write notes if accepted).
submit:
    python3 scripts/submit.py

# Open a problem's page in the browser.
open id:
    leetgo open {{id}}

# Pick a random solved problem to review.
review:
    python3 scripts/review.py
