# General Guidelines for creating mermaid.js diagrams

## Line Breaks

### General Syntax

The method for creating line breaks varies by diagram type:

#### Most Diagram Types (Recommended)
Use `<br>` or `<br/>` tags for line breaks in text labels, notes, and descriptions.

```mermaid
classDiagram
    note for Duck "can fly<br>can swim<br>can dive<br>can help in debugging"
```

## HTML Escaping and Special Characters

### Entity Code Escaping

Mermaid supports numeric entity codes for escaping special characters that might conflict with diagram syntax.

#### Syntax
```
#decimal_number;
```

#### Common Examples
| Character | Entity Code | Description |
|-----------|-------------|-------------|
| `"` | `#quot;` | Double quote |
| ♥ | `#9829;` | Heart symbol |
| # | `#35;` | Hash symbol |
| ∞ | `#infin;` | Infinity symbol |
| ; | `#59;` | Semicolon (since semicolons are used for line breaks) |

#### Usage Examples
```mermaid
sequenceDiagram
    Alice->John: "A double quote:#quot;"
    Alice->Bob: "A dec char:#9829;"
```

### Standard HTML Entities

Some diagrams also support standard HTML entities:

| Entity | Character | Usage |
|--------|-----------|-------|
| `&lt;` | `<` | Less than |
| `&gt;` | `>` | Greater than |
| `&amp;` | `&` | Ampersand |

#### Example in State Diagrams
```mermaid
stateDiagram
    [*] --> <<choice>>
    <<choice>> --> <<fork>>
```

---

## ⚠️ Reserved Words That Break Diagrams

### Critical Reserved Words

#### "end" (Case-sensitive)
The word "end" in lowercase will break flowcharts and sequence diagrams.

**❌ This will break:**
```mermaid
flowchart TD
    A --> end
```

**✅ Solutions:**
1. **Capitalize it:**
```mermaid
flowchart TD
    A --> End
```

2. **Use quotes:**
```mermaid
flowchart TD
    A --> "end"
```

3. **Use brackets:**
```mermaid
flowchart TD
    A --> [end]
```

#### Special Characters in Flowcharts
Letters like "o" or "x" as the first character can create unintended edges.

**❌ This might create unwanted edges:**
```mermaid
flowchart TD
    A --> oB
    A --> xC
```

**✅ Solutions:**
```mermaid
flowchart TD
    A --> B  # Remove the prefix
    A --> "oB"  # Use quotes
    A --> OB  # Capitalize
```

---

## Colors

When selecting colors, make sure text is dark if background is light, and text is light if background is dark. For example, if you have selected a light peach as the color for a diagram element, make sure that the text written in that diagram element is dark (black/close to black).

## Syntax guidance

When possible - and not otherwise adviced by the user / context - use UML syntax.