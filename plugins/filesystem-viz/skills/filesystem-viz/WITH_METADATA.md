# Filesystem Visualization with Metadata

This guide covers patterns for including metadata in filesystem visualizations, such as file sizes, states, dates, and other attributes.

## File States

Use symbols to show file states (modified, added, deleted, renamed):

```
src/
├── [M] modified.ts
├── [A] new-file.ts
├── [D] deleted.ts
└── [R] renamed.ts
```

- `[M]` - Modified
- `[A]` - Added
- `[D]` - Deleted
- `[R]` - Renamed

## File Sizes

Include file sizes when relevant (useful for build outputs, assets, bundles):

```
dist/
├── bundle.js              (245 KB)
├── vendor.js              (1.2 MB)
├── styles.css             (48 KB)
└── assets/
    └── logo.png           (15 KB)
```

## File Permissions (Unix/Linux)

Show file permissions and ownership:

```
/var/www/
├── html/                           drwxr-xr-x  www-data:www-data
│   ├── index.html                  -rw-r--r--  www-data:www-data
│   └── assets/                     drwxr-xr-x  www-data:www-data
├── logs/                           drwxrwx---  www-data:adm
│   ├── access.log                  -rw-rw----  www-data:adm
│   └── error.log                   -rw-rw----  www-data:adm
└── config/                         drwx------  root:root
    └── .env                        -rw-------  root:root
```

## Timestamps

Include modification or creation dates:

```
backups/
├── 2024-01-15/
│   ├── database.sql                2024-01-15 02:00:00
│   └── uploads.tar.gz              2024-01-15 02:15:00
├── 2024-01-16/
│   ├── database.sql                2024-01-16 02:00:00
│   └── uploads.tar.gz              2024-01-16 02:15:00
└── latest -> 2024-01-16/           (symlink)
```

## Git Status Integration

Combine filesystem structure with git status:

```
project/
├── src/
│   ├── [M] App.tsx
│   ├── [ ] index.tsx
│   ├── [A] NewFeature.tsx
│   └── [ ] utils/
│           ├── [M] helpers.ts
│           └── [D] deprecated.ts 
├── [M] package.json
└── [?] README.md
```

- `[M]` - Modified
- `[A]` - Added
- `[D]` - Deleted
- `[ ]` - No change
- `[?]` - Untracked


## Line Counts and Complexity

Show code metrics:

```
src/
├── components/
│   ├── Header.tsx                  156 lines  (complexity: 12)
│   ├── Footer.tsx                  89 lines   (complexity: 5)
│   └── Dashboard.tsx               542 lines  (complexity: 45)
├── utils/
│   ├── validation.ts               234 lines  (complexity: 18)
│   └── formatting.ts               67 lines   (complexity: 3)
└── index.ts                        23 lines   (complexity: 1)
```