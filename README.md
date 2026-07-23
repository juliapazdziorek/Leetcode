# LeetCode Solutions

Welcome to my LeetCode repository. Here you'll find my solutions to LeetCode problems, written as I work my way through the [NeetCode 150 roadmap](https://neetcode.io/roadmap). This project is a work in progress and will be updated as I solve more challenges.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://leetcard.jacoblin.cool/juliapazdziorek?theme=dark">
    <img src="https://leetcard.jacoblin.cool/juliapazdziorek?theme=light" alt="My LeetCode stats">
  </picture>
</p>

## Project Structure

```text
Leetcode/
├── README.md
├── leetgo.yaml
├── justfile
└── solutions/
    └── <id>.<slug>/
        ├── solution.py
        ├── question.md
        └── testcases.txt
```

- `solutions/<id>.<slug>/` – one folder per problem, numbered the way LeetCode numbers them, e.g. `0001.two-sum`.
- `solution.py` – my solution to the problem.
- `question.md` and `testcases.txt` – the problem statement and its test cases, both pulled down automatically.
- `leetgo.yaml` and `justfile` – the tooling that scaffolds, tests and submits problems.

## Workflow

Problems are fetched, tested and submitted with [leetgo](https://github.com/j178/leetgo), wrapped in [just](https://github.com/casey/just) shortcuts:

```sh
just new 1 # fetch problem #1 into solutions/0001.two-sum/
just test # run its test cases locally
just submit # submit the solution to LeetCode
```
