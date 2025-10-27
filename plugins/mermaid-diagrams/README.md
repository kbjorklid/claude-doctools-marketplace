# Mermaid Diagrams Plugin

A Claude Code plugin that contains a skill for creating high quality Mermaid.js diagrams. This is enabled by official documentation and some additional documentation.
Goal is to make Claude make fewer mistakes, create diagrams with consistent style, and use the mermaid.js features to create rich and expressive visualizations.

## Installation

### Using Marketplace

```bash
# Add the marketplace
/plugin marketplace add https://github.com/kbjorklid/claude-marketplace.git

# Add the mermaid-diagrams skill
/plugin install mermaid-diagrams@kbjorklid
```

### Manually

1. Clone this repository
2. Copy the `plugins/mermaid-diagrasm/skills/mermaid` directory to your `~/.claude/skills` directory. 

## Activation

Claude should autmatically invoke this skill when you:
- Request diagram creation (e.g., "create a flowchart showing the authentication process")
- Ask for flowchart or visualization design
- Work with `.mmd` files
- Edit mermaid code blocks in markdown files
- Need to visualize processes, data structures, or system architecture

You can be more explicit and ask claude to use this skill "Use mermaid-diagrams skill ..."

## Supported diagram types

This skill supports all 23+ Mermaid.js diagram types:
- **Architecture Diagrams** - System architecture and components
- **Block Diagrams** - Block-based visual representations
- **C4 Diagrams** - Software architecture contexts
- **Class Diagrams** - Object-oriented structures
- **Entity Relationship Diagrams (ERD)** - Database schemas
- **Flowcharts** - Process flows and decision trees
- **Gantt Charts** - Project timelines and schedules
- **Git Graphs** - Version control branching and commits
- **Kanban Boards** - Task management workflows
- **Mind Maps** - Concept hierarchies and brainstorming
- **Packet Diagrams** - Network packet structures
- **Pie Charts** - Data distribution and proportions
- **Quadrant Charts** - 2x2 matrix visualizations
- **Radar Charts** - Multi-dimensional data comparison
- **Requirement Diagrams** - Requirements and relationships
- **Sankey Diagrams** - Flow and quantity visualization
- **Sequence Diagrams** - Interaction and message flows
- **State Diagrams** - State machines and transitions
- **Timelines** - Historical events and milestones
- **Treemaps** - Hierarchical data as nested rectangles
- **User Journey Diagrams** - User experience flows
- **XY Charts** - Coordinate-based data plots
- **ZenUML Sequence Diagrams** - Alternative sequence diagram syntax

## Attribution

This plugin includes documentation from the [Mermaid.js project](https://github.com/mermaid-js/mermaid), which is licensed under the MIT License.

### Mermaid.js License

The Mermaid.js documentation included in this plugin is:

- **Copyright:** (c) 2014 - 2022 Knut Sveidqvist
- **License:** MIT License
- **Source:** https://github.com/mermaid-js/mermaid
- **Website:** https://mermaid.js.org/

The full MIT License text is available in `skills/mermaid/mermaid_docs/LICENSE`.

## Usage

The plugin activates when users request diagram creation, flowchart design, visualization of processes/data/architecture, system documentation, or when working with `.mmd` files or mermaid code blocks.

## Third-Party Materials

All documentation files in `skills/mermaid/mermaid_docs/` are sourced from the Mermaid.js project and remain the copyright of their original authors. These materials are used in accordance with the MIT License, which permits redistribution with proper attribution.