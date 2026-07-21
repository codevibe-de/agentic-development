# hello-world

A minimal demo [Claude Code plugin](https://docs.claude.com/en/docs/claude-code/plugins). It exists to show the three most common extension points in one small package.

## What's inside

```
plugins/hello-world/
├── .claude-plugin/
│   └── plugin.json      # manifest: name, version, and paths to the parts below
├── commands/
│   └── hello.md         # slash command → /hello
├── agents/
│   └── greeter.md       # subagent → "greeter"
├── hooks/
│   └── hooks.json       # SessionStart hook that prints a welcome banner
└── README.md
```

## The extension points

| Part | File | How you use it |
| --- | --- | --- |
| **Slash command** | `commands/hello.md` | Type `/hello` — greets you and summarizes the repo. |
| **Agent** | `agents/greeter.md` | Ask Claude to use the `greeter` agent for a plugin tour. |
| **Hook** | `hooks/hooks.json` | Runs automatically on `SessionStart`, printing a banner. |

## Trying it out

Add this folder as a plugin marketplace / local plugin, e.g.:

```bash
# from a Claude Code session, add the local directory as a plugin source
/plugin marketplace add ./plugins
/plugin install hello-world
```

Then run `/hello` or ask Claude to "use the greeter agent". The `SessionStart`
hook fires on its own the next time a session starts.

> This is intentionally tiny. Copy the structure and replace the contents to
> build something real.
