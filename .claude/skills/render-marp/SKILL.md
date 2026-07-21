---
name: render-marp
description: Renders a Marp markdown presentation file to HTML, PDF, or PPTX using the Marp CLI. Use when the user wants to render or export a Marp slide deck.
allowedTools:
  - Bash(marp*)
  - mcp__playwright__browser_navigate
---

When asked to render a Marp presentation:

1. Identify the target `.md` file — use the file provided by the user, or if none is specified, look for a recently created or opened `.md` file in the project that contains `marp: true` in its frontmatter.

2. Run `marp` in server-mode to serve the directory of the file: `marp --server <directory>`

3. Report the server URL that was printed when running the server.

4. If possible, use the Playwright MCP to open the HTML for the file in a browser, such
as `http://localhost:8080/<md-file>`
