# Marketplace for Claude Code plugins

## Quick Start

```bash
# Add the marketplace
/plugin marketplace add https://github.com/kbjorklid/claude-marketplace.git

# Add the mermaid-diagrams skill
/plugin install mermaid-diagrams@kbjorklid
```

## Mermaid.js Diagram Creator Skill

This skill is a bunch of documentation about creating mermaid.js diagrams. The documentation is mostly from the official repository.

There is some additional documentation (especially for class diagrams) to avoid some common pitfalls LLMs keep making, and generally guide "good habits" for diagram creation.

There are multiple styles for some things, like defining class attributes and method parameters: `NameFirst: string` (UML style), `string NameLast` (Java/C# style), `+DoSomething(justTheName)` (name only, typically for method parameters). Where possible, I aim to instruct for UML compliance, but I aim to do it softly so that overriding is possible. For overrides, you may want to consider creating an agent and adding your preferences to the agent's instructions.

I don't use all the diagram types extensively (or at all) so some diagram types will have just the official documentation - which should mostly be enough.

Feature requests, pull requests etc are welcome.
