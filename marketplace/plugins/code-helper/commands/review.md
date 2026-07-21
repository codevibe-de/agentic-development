---
description: Review the current git diff for bugs and quick wins.
---

Review the current working changes.

1. Run `git diff` (and `git diff --staged`) to see what changed.
2. Look for correctness bugs, missing error handling, and obvious simplifications.
3. Report findings as a short, prioritized list. If nothing stands out, say so.

Focus only on the changed lines and their immediate context. Additional focus from the user: $ARGUMENTS
