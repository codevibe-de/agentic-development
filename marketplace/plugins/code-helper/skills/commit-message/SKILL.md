---
name: commit-message
description: Write a clear, conventional git commit message from staged changes. Use when the user asks to write, draft, or improve a commit message.
---

# Commit Message

Draft a commit message that follows the Conventional Commits style.

## Steps

1. Inspect what is staged with `git diff --staged`. If nothing is staged, look at `git diff` instead and note that the changes are unstaged.
2. Determine the type: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, or `build`.
3. Write the subject line: `type(scope): summary` — imperative mood, lowercase, no trailing period, ≤ 72 chars. The scope is optional.
4. If the change is non-trivial, add a blank line and a short body explaining *why*, wrapped at ~72 chars.

## Output

Present the message in a fenced code block so it is easy to copy. Do not run `git commit` yourself unless the user explicitly asks.
