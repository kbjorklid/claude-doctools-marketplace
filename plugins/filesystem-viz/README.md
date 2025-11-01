# Filesystem Visualization Plugin

A Claude Code plugin that provides expertise in creating ASCII art visualizations of directory structures and file systems in markdown documents.

## Overview

This plugin teaches Claude how to create clear, consistent, and professional-looking filesystem visualizations using ASCII and Unicode box-drawing characters. Perfect for documenting project structures, README files, and technical documentation.

## Installation

### Using Marketplace

```bash
# Add the marketplace
/plugin marketplace add https://github.com/kbjorklid/claude-marketplace.git

# Install the filesystem-viz plugin
/plugin install filesystem-viz@claude-doctools
```

### Manually

1. Clone this repository
2. Copy the `plugins/filesystem-viz/skills/filesystem-viz` directory to your `~/.claude/skills` directory

## Activation

Claude should automatically invoke this skill when you:
- Request directory tree visualizations (e.g., "show me the project structure")
- Ask for filesystem layouts (e.g., "create a directory tree for this project")
- Request folder hierarchy diagrams
- Need to document project organization
- Want to visualize file structure in documentation

You can explicitly request the skill: "Use filesystem-viz skill to show the directory structure"

## Features

### Character Set Support

- **Unicode Box-Drawing Characters**: Modern, clean appearance
  ```
  ├── folder/
  │   └── file.txt
  ```

- **ASCII Characters**: Universal compatibility
  ```
  |-- folder/
  |   `-- file.txt
  ```

### Visualization Types

1. **Basic Directory Trees**: Simple hierarchical structures
2. **Detailed File Listings**: Include file descriptions and annotations
3. **Multi-Level Deep Structures**: Complex hierarchies with many nested levels
4. **Selective Focus**: Show only relevant parts with ellipsis
5. **Horizontal Layouts**: Compact inline representations
6. **Categorized Structures**: Group files by type or purpose

### Use Cases

- Project README files
- Architecture documentation
- Setup and installation guides
- Configuration file locations
- Build output directories
- Monorepo/workspace structures
- Repository organization

## Examples

### Simple Project Structure

```
my-website/
├── index.html
├── css/
│   ├── style.css
│   └── reset.css
├── js/
│   ├── main.js
│   └── utils.js
└── images/
    ├── logo.png
    └── banner.jpg
```

### Documented Structure

```
api-server/
├── src/
│   ├── index.ts           # Server entry point
│   ├── routes/
│   │   ├── auth.ts        # Authentication endpoints
│   │   └── users.ts       # User management
│   ├── middleware/
│   │   └── errorHandler.ts
│   └── config/
│       └── database.ts
├── tests/
│   ├── unit/
│   └── integration/
└── package.json
```

### Monorepo Structure

```
workspace/
├── packages/
│   ├── @company/core/
│   │   ├── src/
│   │   └── package.json
│   ├── @company/utils/
│   │   └── package.json
│   └── @company/ui/
│       └── package.json
└── apps/
    ├── web/
    └── mobile/
```

## Skill Capabilities

The filesystem-viz skill provides:

- Comprehensive patterns for different visualization needs
- Best practices for clarity and consistency
- Guidelines for information density and formatting
- Common patterns organized by use case
- Advanced techniques for showing relationships and states
- Troubleshooting guidance for common issues
- Integration strategies with documentation

## When to Use

Use this plugin when:
- Creating or updating project documentation
- Writing README files that explain project structure
- Documenting build outputs or generated directories
- Explaining configuration file locations
- Showing package organization in monorepos
- Illustrating file relationships in technical guides

## Best Practices

1. **Consistency**: Choose one character set and stick with it
2. **Clarity**: Use trailing slashes for directories, add comments for clarity
3. **Information Density**: Balance detail with readability
4. **Formatting**: Always wrap in markdown code blocks

## Contributing

This plugin is part of the Claude Code marketplace. Contributions and improvements are welcome!

## License

This plugin is provided as-is for use with Claude Code.
