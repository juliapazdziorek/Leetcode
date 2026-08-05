# On Windows, run recipes through cmd instead of the default `sh` (which isn't installed).
# Ignored on macOS/Linux, so this file stays portable.
set windows-shell := ["cmd.exe", "/c"]

# Show the list of recipes.
default:
    @just --list

# Fetch a problem into solutions/<id>.<slug>/
new id:
    leetgo pick {{id}} -l python3

# Run the last problem's test cases locally.
test:
    leetgo test last -L

# Submit the last problem to LeetCode.
submit:
    leetgo submit last

# Open a problem's page in the browser.
open id:
    leetgo open {{id}}
