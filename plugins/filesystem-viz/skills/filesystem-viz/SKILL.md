---
name: filesystem-viz
description: Expert guide for creating ASCII art visualizations of directory structures and file systems in markdown. Use when documenting project structure, showing folder hierarchies, creating directory trees, or visualizing file organization. Activate when user requests filesystem visualization, directory trees, folder structure diagrams, or project layout documentation.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Filesystem Visualization with ASCII Art

This skill provides comprehensive guidance for creating clear, consistent, and visually appealing filesystem visualizations using ASCII/Unicode characters in markdown documents.

## Subtopics

For specialized visualization patterns, see these detailed guides:

- **[WITH_COMMENTS.md](./WITH_COMMENTS.md)** - Comprehensive patterns for adding comments and annotations to filesystem trees, including inline comments, callback references for detailed explanations, task-oriented comments (TODO, FIXME), and documentation cross-references.

- **[WITH_METADATA.md](./WITH_METADATA.md)** - Patterns for including metadata in visualizations such as file sizes, modification states, timestamps, permissions, git status integration, and complexity metrics.

## Character Sets for Tree Structures

### Box Drawing Characters (Recommended for Modern Systems)

Use Unicode box-drawing characters for clean, professional-looking trees:

```
├── (branch with continuation)
│   (vertical line)
└── (final branch)
```

**Example:**
```
project/
├── src/
│   ├── components/
│   │   ├── Header.tsx
│   │   └── Footer.tsx
│   └── utils/
│       └── helpers.ts
└── tests/
    └── unit/
        └── helpers.test.ts
```

### ASCII Characters (Universal Compatibility)

Use ASCII characters for maximum compatibility. Use only if you know that the box drawing characters style is not working, or if user tells you to use this style.

```
|-- (branch with continuation)
|   (vertical line)
`-- (final branch)
```

**Example:**
```
project/
|-- src/
|   |-- components/
|   |   |-- Header.tsx
|   |   `-- Footer.tsx
|   `-- utils/
|       `-- helpers.ts
`-- tests/
    `-- unit/
        `-- helpers.test.ts
```

## Visualization Patterns

### 1. Basic Directory Tree

For simple hierarchical structures:

```
app/
├── public/
│   ├── images/
│   └── styles/
├── src/
│   ├── pages/
│   ├── components/
│   └── lib/
└── config/
```

### 2. Multi-Level Deep Structures

For complex hierarchies with many levels:

```
monorepo/
├── packages/
│   ├── ui/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── Button/
│   │   │   │   │   ├── Button.tsx
│   │   │   │   │   ├── Button.test.tsx
│   │   │   │   │   └── index.ts
│   │   │   │   └── Input/
│   │   │   │       ├── Input.tsx
│   │   │   │       └── index.ts
│   │   │   └── index.ts
│   │   └── package.json
│   └── utils/
│       ├── src/
│       └── package.json
└── apps/
    ├── web/
    └── admin/
```

### 3. Selective Focus with Ellipsis

When showing only relevant parts:

```
src/
├── components/
│   ├── auth/
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   └── ...
│   ├── dashboard/
│   │   └── ...
│   └── ...
├── services/
│   └── ...
└── ...
```

**Use ellipsis (...)** to indicate omitted content when showing selective focus
