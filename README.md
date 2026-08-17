# AI

A monorepo housing multiple independent projects, each in its own folder under `projects/`.

## Structure

```
AI/
├── projects/
│   └── <project-name>/     # each project is self-contained
├── .gitignore
└── README.md
```

## Adding a new project

```bash
mkdir projects/<project-name>
cd projects/<project-name>
```

Give each project its own README, dependencies, and virtual environment as needed.
