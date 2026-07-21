# Codevibe Demo Marketplace

A demo [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces.md).
Add it to Claude Code and install the example plugins to see how commands, agents,
skills, and hooks are packaged.

## Layout

```
marketplace/
├── .claude-plugin/
│   └── marketplace.json          # marketplace manifest (lists the plugins)
└── plugins/
    ├── hello-world/              # minimal starter: one slash command
    │   ├── .claude-plugin/plugin.json
    │   └── commands/hello.md
    └── code-helper/              # command + agent + skill + hook
        ├── .claude-plugin/plugin.json
        ├── commands/review.md
        ├── agents/reviewer.md
        ├── skills/commit-message/SKILL.md
        └── hooks/hooks.json
```

## Add the marketplace

From Claude Code, point it at this folder (use the absolute path or a path
relative to your session):

```
/plugin marketplace add ./marketplace
```

## Install a plugin

```
/plugin install hello-world@codevibe-demo
/plugin install code-helper@codevibe-demo
```

## Try it

- `/hello` — greeting from the **hello-world** plugin.
- `/code-helper:review` — review the current git diff.
- Ask to "review this function" — the **reviewer** agent can be delegated to.
- Ask to "write a commit message" — triggers the **commit-message** skill.
- Edit any file — the **code-helper** `PostToolUse` hook prints a reminder.

## Validate

```
/plugin validate ./marketplace
```
