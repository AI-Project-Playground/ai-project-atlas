# AI Project Template

This directory is the starting point for creating a project that can be
submitted to AI Project Atlas.

## 1. Create Your Project

Copy this template into a new project directory.

Example:

```text
projects/
└── ml-001/
    ├── project.yaml
    ├── README.md
    ├── ai-context.md
    ├── src/
    ├── tests/
    ├── notebooks/
    ├── results/
    └── assets/
```

Your project should be a real hands-on implementation, experiment,
application, research prototype, benchmark, or AI system.

Theory-only topics should not be submitted as projects.

## 2. Complete `project.yaml`

Start by filling in the required metadata:

- `schema_version`
- `id`
- `title`
- `domain`
- `topics`
- `project_type`
- `difficulty`
- `status`
- `technologies`
- `capabilities`

Then add optional information where applicable:

- `learning_outcomes`
- `tags`
- `artifacts`
- `experiences`
- `relationships`

Refer to:

```text
docs/PROJECT_CONTRACT.md
```

for the meaning and rules of each field.

## 3. Build the Project

Put the actual implementation in the project directory.

Typical locations:

```text
src/          Source code
tests/        Automated tests
notebooks/    Exploratory or demonstration notebooks
results/      Generated results and evaluation outputs
assets/       Images and other supporting assets
```

The exact structure may vary depending on the project.

For example, a research prototype or a frontend application may need
additional directories.

## 4. Add Artifacts

If your project produces or uses important artifacts, reference them in
`project.yaml`.

Examples:

```yaml
artifacts:
  github: "https://github.com/..."
  notebook: "https://..."
  demo: "https://..."
```

Only add artifacts that actually exist.

## 5. Add Experiences

A project may provide multiple ways to explore or demonstrate it.

For example:

```text
Experience 1 — Notebook
Experience 2 — Interactive Visualization
Experience 3 — Live Demo
```

Experiences are optional.

If an experience can actually be run, describe its execution configuration
according to the project contract.

## 6. Validate Before Submission

From the AI Project Atlas repository, validate your project with:

```powershell
python -m validator.validate projects\YOUR_PROJECT\project.yaml schemas\project.schema.json
```

A valid project should produce:

```text
VALIDATION PASSED
```

An invalid project should produce:

```text
VALIDATION FAILED
```

Fix validation errors before submitting the project.

## 7. Submission Workflow

The expected workflow is:

```text
Create project
     ↓
Complete project.yaml
     ↓
Build and test project
     ↓
Add artifacts/results
     ↓
Run Atlas validator
     ↓
Commit changes
     ↓
Push branch
     ↓
Create Pull Request
     ↓
Review
     ↓
Merge
```

## Important Principles

### Build first, describe second

Do not create catalogue metadata for a project that does not actually exist.

### Be truthful

Only claim technologies, capabilities, artifacts, experiences, and results
that the project genuinely demonstrates.

### No arbitrary code execution

A project may request an executable experience, but Atlas controls whether
that experience is approved and enabled for execution.

### Keep projects independent

A project should contain enough information and artifacts for another
developer to understand and reproduce the work.

### Atlas owns catalogue administration

Contributors define project metadata.

Atlas controls things such as:

- visibility
- locking
- execution approval
- execution enablement
- ingestion
- catalogue indexing
