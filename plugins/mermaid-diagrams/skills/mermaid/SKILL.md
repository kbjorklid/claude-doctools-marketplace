---
name: mermaid-diagrams
description: Expert guide for creating and modifying Mermaid.js diagrams. Supports all diagram types including architecture diagrams, block diagrams, C4 diagrams, class diagrams, ERDs, flowcharts, Gantt charts, git graphs, kanban boards, mind maps, packet diagrams, pie charts, quadrant charts, radar charts, requirement diagrams, Sankey diagrams, sequence diagrams, state diagrams, timelines, treemaps, user journey diagrams, XY charts, and ZenUML. Activate when user requests diagram creation, visualization of processes/data/architecture, system documentation, or when working with .mmd files or mermaid code blocks in markdown files.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Mermaid.js diagram editor

To create sophisticated, well structured mermaid.js diagrams or charts, follow these instructions.

You should not deviate from the syntax presented in the documentation: Do not create / edit diagrams based on your internal knoweledge; rather let the documentation guide you.

## Workflow

1. Identify based on the context what type(s) of diagrams need to be worked on.

2. Read relevant documentation (see below for instructions)

3. Create the diagram(s)

## Documentation reading guidance

1. ALWAYS read [GENERAL_GUIDELINES.md](./GENERAL_GUIDELINES.md)

2. ALWAYS read the specific documentation related to the diagram type you're about to modify or create, see "Specific diagram type reading instructions" below.

2. ALWAYS read [Mermaid.js Documentation Index](./DOC_INDEX.md)

4. If you think other documentation is beneficial based on what you see in `DOC_INDEX.md`, use the Task tool with subagent_type=general-purpose to read the file and create a focused report on what's relevant to the current diagram task. The agent should analyze the documentation and extract only information applicable to the specific diagram type or feature you're implementing.

### Specific diagram type reading instructions

#### Architecture Diagrams (`architecture-beta`)

- Read [architecture diagram](./mermaid_docs/syntax/architecture.md)

#### Block Diagrams (`block`)

- Read [block diagram](./mermaid_docs/syntax/block.md)

#### C4 Diagrams (`c4Diagram`)

- Read [C4 diagram](./mermaid_docs/syntax/c4.md)

#### Class Diagrams (`classDiagram`)

- Read [class diagram](./mermaid_docs/syntax/classDiagram.md)h
- Read [class diagrams - advanced](./ADVANCED_CLASS_DIAGRAMS.md)

#### Entity Relationship Diagrams (ERD) (`erDiagram`)

- Read [entity relationship diagram](./mermaid_docs/syntax/entityRelationshipDiagram.md)

#### Flowcharts (`flowchart`)

- Read [flowchart](./mermaid_docs/syntax/flowchart.md)

#### Gantt Charts (`gantt`)

- Read [Gantt chart](./mermaid_docs/syntax/gantt.md)

#### Git Graphs (`gitGraph`)

- Read [git graph](./mermaid_docs/syntax/gitgraph.md)

#### Kanban Boards (`kanban`)

- Read [kanban board](./mermaid_docs/syntax/kanban.md)

#### Mind Maps (`mindmap`)

- Read [mind map](./mermaid_docs/syntax/mindmap.md)

#### Packet Diagrams (`packet-beta`)

- Read [packet diagram](./mermaid_docs/syntax/packet.md)

#### Pie Charts (`pie`)

- Read [pie chart](./mermaid_docs/syntax/pie.md)

#### Quadrant Charts (`quadrantChart`)

- Read [quadrant chart](./mermaid_docs/syntax/quadrantChart.md)

#### Radar Charts (`radar-beta`)

- Read [radar chart](./mermaid_docs/syntax/radar.md)

#### Requirement Diagrams (`requirement`)

- Read [requirement diagram](./mermaid_docs/syntax/requirementDiagram.md)

#### Sankey Diagrams (`sankey`)

- Read [Sankey diagram](./mermaid_docs/syntax/sankey.md)

#### Sequence Diagrams (`sequenceDiagram`)

- Read [sequence diagram](./mermaid_docs/syntax/sequenceDiagram.md)

#### State Diagrams (`stateDiagram-v2`)

- Read [state diagram](./mermaid_docs/syntax/stateDiagram.md)

#### Timelines (`timeline`)

- Read [timeline](./mermaid_docs/syntax/timeline.md)

#### Treemaps (`treemap-beta`)

- Read [treemap](./mermaid_docs/syntax/treemap.md)

#### User Journey Diagrams (`journey`)

- Read [user journey diagram](./mermaid_docs/syntax/userJourney.md)

#### XY Charts (`xychart`)

- Read [XY chart](./mermaid_docs/syntax/xyChart.md)

#### ZenUML Sequence Diagrams (`zenuml`)

- Read [ZenUML sequence diagram](./mermaid_docs/syntax/zenuml.md)
