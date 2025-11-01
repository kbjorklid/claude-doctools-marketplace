# Filesystem Visualization with Comments and Annotations

This guide covers patterns for adding comments, annotations, and explanations to filesystem visualizations to make them more informative and self-documenting.

## Inline Comments

Add brief explanations directly after file or directory names:

```
project-root/
├── package.json         # Project dependencies
├── tsconfig.json        # TypeScript configuration
├── .gitignore           # Git ignore rules
├── src/
│   ├── index.ts         # Application entry point
│   ├── app.ts           # Main application logic
│   └── routes/
│       ├── api.ts       # API endpoints
│       └── web.ts       # Web routes
└── dist/                # Build output (generated)
```

## Selective Focus with Comments

Highlight specific areas of interest while showing context:

```
src/
├── components/
│   ├── auth/
│   │   ├── Login.tsx        # Focus: New login component
│   │   ├── Register.tsx
│   │   └── ...
│   ├── dashboard/
│   │   └── ...
│   └── ...
├── services/
│   └── ...
└── ...
```

## Categorized Comments

Group and label sections for clarity:

```
project/
├── Frontend
│   ├── src/             # React application source
│   ├── public/          # Static assets
│   └── package.json     # Frontend dependencies
├── Backend
│   ├── api/             # Express API server
│   ├── database/        # Database migrations and seeds
│   └── requirements.txt # Python dependencies
└── Infrastructure
    ├── docker/          # Docker configuration
    └── kubernetes/      # K8s deployment manifests
```


## Callback References

For detailed explanations, use callback markers (a, b, c, etc.) with descriptions below:

```
project/
├── src/
│   ├── core/
│   │   ├── engine.ts           (a)
│   │   ├── scheduler.ts        (b)
│   │   └── optimizer.ts        (c)
│   ├── plugins/
│   │   ├── validator.ts        (d)
│   │   └── transformer.ts
│   └── utils/
│       └── helpers.ts
├── config/
│   └── defaults.json           (e)
└── tests/
    └── integration/            (f)
```

**(a)** Main execution engine - handles the core processing pipeline, manages worker
    threads, and coordinates between different subsystems. This is the entry point
    for all computational tasks.

**(b)** Task scheduler implementing a priority queue system with deadline awareness.
    Supports both immediate execution and deferred scheduling with configurable
    retry policies.

**(c)** Performance optimizer that analyzes execution patterns and automatically tunes
    parameters. Uses machine learning models to predict optimal configurations
    based on workload characteristics.

**(d)** Plugin validation framework ensuring all extensions meet security and
    performance requirements before loading. Implements sandboxing and resource
    limits.

**(e)** Default configuration values loaded at startup. Can be overridden by
    environment-specific configs or runtime parameters. See docs/config.md for
    all available options.

**(f)** Integration test suite covering end-to-end workflows. Requires Docker for
    database and cache dependencies. Run with: npm run test:integration

## When to Use Callbacks vs Inline Comments

### Use Inline Comments When:
- Explanation is short (< 40 characters)
- One-line description is sufficient
- Comment adds immediate context
- Quick identification is the goal

### Use Callback References When:
- Explanations require multiple sentences
- Technical details need elaboration
- Relationships between files need explanation
- Examples, commands, or code snippets are helpful
- Setup or usage instructions are needed

## Best Practices

### Keep Comments Concise
- Aim for 40 characters or less for inline comments
- Use callbacks for longer explanations

### Be Consistent
- Use the same comment style throughout
- Choose either `#` or `//` and stick with it
- Maintain consistent spacing

### Add Value
- Don't state the obvious (`index.ts # An index file`)
- Explain the "why" not just the "what"
- Highlight non-obvious relationships or purposes