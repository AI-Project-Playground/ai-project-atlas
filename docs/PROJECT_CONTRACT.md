# AI Project Atlas — Project Submission Contract

**Contract Version:** 1.0  
**Purpose:** Standard contract for describing hands-on AI/ML projects so they can be validated, imported, searched, displayed, and used by the AI Project Atlas agent.

---

## 1. Purpose

AI Project Atlas is a catalogue of actual hands-on AI/ML work.

A catalogue entry must represent something that has been built, trained, tested, deployed, integrated, benchmarked, or otherwise demonstrated in practice.

Theory can be included in project documentation, but theory alone is not a catalogue project.

This contract defines the boundary between:

- Contributor-owned project metadata
- Atlas-owned catalogue metadata
- Experiences
- Execution
- Search and AI-agent context

---

## 2. Core Principles

1. **Projects are real hands-on work.**
2. **A project can cover multiple topics.**
3. **A topic can contain multiple projects.**
4. **A project can belong to exactly one primary domain.**
5. **A project can have multiple experiences.**
6. **An experience may or may not be executable.**
7. **Execution is optional and must be explicitly approved by Atlas.**
8. **Contributors describe what they built; Atlas controls publication and execution.**
9. **The contract is the integration boundary between projects and Atlas.**
10. **The contract must remain vendor- and framework-neutral.**

---

# 3. Project Metadata

A project should provide the following metadata where applicable:

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
- `learning_outcomes`
- `artifacts`
- `experiences`
- `relationships`
- `tags`
- AI-context information

Example:

```yaml
schema_version: "1.0"
id: ml-001
title: Ordinary Least Squares Regression from Scratch
domain: Machine Learning

topics:
  - Linear Regression
  - Ordinary Least Squares
  - Optimization
  - Model Evaluation

project_type: algorithm_implementation
difficulty: beginner
status: completed

technologies:
  - Python
  - NumPy
  - scikit-learn

capabilities:
  - PREDICT
  - EVALUATE

learning_outcomes:
  - Implement OLS regression from scratch
  - Understand the normal equation
  - Compare a custom implementation with scikit-learn

tags:
  - regression
  - mathematics
  - from-scratch
```

---

# 4. Domain

Each project has exactly one **primary domain**.

The domain is the project's main catalogue home.

Examples:

- Mathematical Foundations
- Data Science
- Machine Learning
- Deep Learning
- Generative AI
- RAG & Knowledge Systems
- Graph AI
- Agentic AI
- AI Engineering
- MLOps
- Computer Vision
- NLP
- Frontier AI

A project may demonstrate concepts from other domains, but only one domain is its primary catalogue domain.

---

# 5. Topics

A project can have **many topics**.

Topics describe the concepts, methods, technologies, patterns, or techniques demonstrated by the project.

Examples:

- EDA
- Feature Engineering
- Classification
- Random Forest
- Model Evaluation
- RAG
- Semantic Search
- GraphRAG
- Knowledge Graphs
- Agentic AI
- Tool Calling
- Planning
- MLOps
- Monitoring

Topics are not a rigid hierarchy.

A topic does not automatically become a separate project.

For example, a Customer Churn Prediction project may have:

```yaml
topics:
  - EDA
  - Data Cleaning
  - Feature Engineering
  - Classification
  - Random Forest
  - Model Evaluation
```

---

# 6. Project Type

`project_type` describes the nature of the hands-on work.

Suggested initial vocabulary:

- `mathematical_implementation`
- `algorithm_implementation`
- `data_analysis`
- `machine_learning`
- `deep_learning`
- `generative_ai`
- `rag_system`
- `graph_ai`
- `agentic_ai`
- `ai_application`
- `mlops`
- `research_prototype`
- `benchmark`
- `experiment`
- `other`

The vocabulary may be extended in future contract versions.

---

# 7. Difficulty

Suggested values:

- `beginner`
- `intermediate`
- `advanced`
- `expert`

Difficulty describes the expected implementation complexity and prerequisites.

---

# 8. Status

Suggested values:

- `planned`
- `in_progress`
- `completed`
- `experimental`
- `archived`

Status describes the contributor's project lifecycle.

Atlas may maintain additional internal publication states separately.

---

# 9. Technologies

`technologies` is a list of technologies actually used by the project.

Examples:

- Python
- NumPy
- Pandas
- scikit-learn
- PyTorch
- TensorFlow
- FastAPI
- PostgreSQL
- pgvector
- Neo4j
- LangGraph
- Ollama

Technologies are metadata and should not be used as a substitute for topics.

---

# 10. Capabilities

Capabilities describe what the project enables or demonstrates.

Initial vocabulary:

- `LEARN`
- `RETRIEVE`
- `GENERATE`
- `PREDICT`
- `CLASSIFY`
- `REASON`
- `REMEMBER`
- `PLAN`
- `ACT`
- `PERCEIVE`
- `EVALUATE`

A project may have multiple capabilities.

Example:

```yaml
capabilities:
  - RETRIEVE
  - GENERATE
  - REASON
  - EVALUATE
```

---

# 11. Learning Outcomes

`learning_outcomes` describes what a person should understand or be able to do after studying the project.

Examples:

- Understand the normal equation for linear regression
- Implement an algorithm without relying on a library implementation
- Compare custom and library implementations
- Evaluate model performance
- Understand retrieval and generation in a RAG pipeline

Learning outcomes should be concrete and project-specific.

---

# 12. Artifacts

Artifacts are outputs or resources associated with the project.

Possible artifact types include:

- GitHub repository
- Notebook
- Demo
- Model
- Dataset
- Documentation
- Video
- Report
- Results
- Screenshots

A project should not assume that one specific platform is always used.

Example:

```yaml
artifacts:
  github: https://github.com/example/ml-001-ols
  notebook: https://colab.research.google.com/example
  demo: https://example.streamlit.app
  documentation: https://example.com/docs
```

Atlas should internally normalize artifacts into a generic artifact model so additional artifact types can be added later.

Conceptually:

```text
Project
  -> ProjectArtifacts
       -> GitHub
       -> Notebook
       -> Demo
       -> Model
       -> Dataset
       -> Documentation
       -> Video
```

---

# 13. Experiences

An **Experience** is a distinct way to explore, demonstrate, interact with, or execute part or all of a project.

A project may have zero, one, or many experiences.

Examples:

- Notebook walkthrough
- Interactive visualization
- Training experiment
- Prediction interface
- Dashboard
- API
- Live website
- RAG assistant
- Semantic search interface
- Evaluation view
- Documentation view

An experience does not have to be runnable.

Example:

```yaml
experiences:
  - id: regression-visualizer
    title: Interactive Regression Visualizer
    description: Explore how OLS responds to different synthetic datasets.
    topics:
      - Linear Regression
      - Ordinary Least Squares
    capabilities:
      - PREDICT
      - EVALUATE
    artifacts:
      demo: https://example.streamlit.app
```

---

# 14. Execution / Run

Execution describes whether an Experience can actually be run.

Execution is optional.

Initial execution modes:

- `browser`
- `notebook`
- `external_demo`
- `sandbox`

Examples of providers include:

- Streamlit
- Gradio
- Hugging Face Spaces
- Google Colab
- Kaggle
- Jupyter
- Custom hosted application

Provider names are extensible.

Example:

```yaml
execution:
  requested: true
  mode: external_demo
  provider: streamlit
  url: https://example.streamlit.app
```

An experience may also have no execution section when it is not intended to be runnable.

---

# 15. Execution Security

Execution is a security-sensitive Atlas capability.

A contributor may **request** execution, but does not grant execution permission to itself.

Atlas controls:

- `execution_requested`
- `execution_approved`
- `execution_enabled`
- `execution_mode`
- `execution_provider`
- `execution_url`
- `execution_approved_at`

The initial prototype must only expose explicitly approved, pre-built experiences.

The prototype must NOT provide:

- Arbitrary visitor Python execution
- Arbitrary repository URL execution
- Arbitrary uploaded-code execution
- Unrestricted shell/process execution
- Unrestricted network access

User input is treated as **data**, never as executable code.

A future `sandbox` mode may provide controlled execution with limits such as:

- CPU limits
- Memory limits
- Time limits
- Filesystem restrictions
- Network restrictions
- Process restrictions
- Resource quotas

---

# 16. Project Visibility and Locking

Visibility and locking are **Atlas-managed internal controls**.

They are not contributor-controlled publication permissions.

Suggested visibility states:

- `public`
- `private`
- `unlisted`
- `archived`

Atlas may also maintain:

- `locked`
- `execution_approved`
- `execution_enabled`

A project can be visible while execution is disabled.

`locked` means administrative action is required before normal modification, publication, or execution-state changes.

Possible reasons for locking include:

- Security review
- Unsafe functionality
- Compromised external demo
- Dependency investigation
- Content review
- Maintenance

Contributors cannot grant themselves:

- Public visibility
- Unlock status
- Execution approval
- Execution enablement

These controls should normally live in the Atlas database/internal model rather than in the contributor's external project contract.

---

# 17. Relationships

Projects can be related to other catalogue entities.

Potential relationship types include:

- `REQUIRES`
- `BUILDS_ON`
- `RELATED_TO`
- `DEMONSTRATES`
- `USES_TECHNOLOGY`
- `USES_MODEL`
- `USES_DATASET`
- `PRODUCES`

Future graph entities may include:

- Project
- Domain
- Topic
- Technology
- Model
- Dataset
- API
- Capability
- Artifact
- Experience

Potential graph relations include:

```text
BELONGS_TO
HAS_TOPIC
USES_TECHNOLOGY
USES_MODEL
USES_DATASET
DEMONSTRATES
REQUIRES
BUILDS_ON
RELATED_TO
PRODUCES
```

The graph model should be extensible.

---

# 18. AI Context

Each project should provide enough context for an AI assistant to understand the project without reading the entire repository.

A recommended `ai-context.md` contains:

## Project Identity

What the project is and why it exists.

## What the Project Does

Short explanation of the hands-on implementation.

## Main Concepts Demonstrated

Important concepts and topics.

## Technologies

Important libraries, frameworks, models, platforms, and infrastructure.

## Capabilities

What the project can demonstrate or perform.

## What It Does Not Cover

Important boundaries that prevent an AI agent from overclaiming.

## Difficulty

Expected level and prerequisites.

## Who Should Build It

Intended learner profile.

## Suggested Follow-up Projects

Projects that naturally build on this project.

The AI context must describe reality and must not invent capabilities.

---

# 19. Search and Retrieval

Atlas should not use RAG for every type of query.

Different retrieval mechanisms should serve different needs.

### Structured SQL

Use for exact filters such as:

- Domain
- Topic
- Difficulty
- Status
- Technology
- Capability
- Project type

### PostgreSQL Full-Text Search

Use for keyword-oriented project discovery.

### Vector Search

Use `pgvector` for semantic search.

Embeddings may initially be generated locally using `sentence-transformers`.

### Hybrid Retrieval

Use structured filtering, full-text search, and vector retrieval together for complex AI-agent queries.

### Graph Retrieval

Graph-based retrieval can be added later for relationship-heavy questions such as:

> What projects build on RAG and lead toward Agentic AI?

---

# 20. Graph / GraphRAG Compatibility

The project model must remain compatible with a future graph representation.

A possible conceptual graph is:

```text
Project
  |
  +-- HAS_TOPIC --> Topic
  |
  +-- USES_TECHNOLOGY --> Technology
  |
  +-- USES_MODEL --> Model
  |
  +-- USES_DATASET --> Dataset
  |
  +-- DEMONSTRATES --> Capability
  |
  +-- PRODUCES --> Artifact
  |
  +-- BUILDS_ON --> Project
```

The initial implementation does not need a graph database.

PostgreSQL can hold the initial relational model, with graph-compatible relationships.

---

# 21. Provenance

Atlas must preserve the source of project information.

Useful provenance fields include:

- Source repository
- Source file
- Source commit/version
- Import timestamp
- Schema version
- Validation result

The goal is to make catalogue information traceable back to contributor-owned project sources.

---

# 22. Validation

Every project submitted to Atlas should pass schema validation before ingestion.

Validation should check:

- Required fields
- Data types
- Controlled vocabulary values
- URL formats where applicable
- Unique project ID
- Valid relationship structure
- Valid experience structure
- Contract/schema version

Invalid projects should fail validation rather than being silently imported.

---

# 23. Ingestion Pipeline

The intended integration flow is:

```text
Contributor Project
       |
       v
project.yaml
       |
       v
Schema Validator
       |
       v
Importer
       |
       v
Atlas Internal Knowledge Model
       |
       +--> PostgreSQL
       |
       +--> Search Index
       |
       +--> Vector Index
       |
       +--> Future Graph
       |
       v
Website + AI Project Agent
```

The external contract is the integration boundary.

The Atlas internal model may evolve independently from the external contract.

---

# 24. Contributor Responsibilities

Contributors are responsible for:

- Building the actual project
- Maintaining project code
- Maintaining project documentation
- Providing accurate metadata
- Declaring topics
- Declaring technologies
- Declaring capabilities
- Declaring artifacts
- Declaring experiences
- Requesting execution when appropriate
- Keeping project metadata synchronized with reality

Contributors do not control Atlas publication or execution approval.

---

# 25. Atlas Responsibilities

Atlas is responsible for:

- Validation
- Importing project metadata
- Normalizing project information
- Maintaining internal catalogue state
- Publication/visibility controls
- Locking
- Execution approval
- Execution enablement
- Search indexing
- Vector indexing
- AI-agent retrieval
- Provenance
- Future graph representation

---

# 26. Vendor and Framework Independence

The contract must not assume a single:

- LLM provider
- Embedding provider
- Vector database
- Agent framework
- Hosting platform
- Notebook platform
- Demo platform

For example, the Atlas platform may initially use:

- SvelteKit
- FastAPI
- PostgreSQL
- pgvector
- sentence-transformers
- Ollama

while remaining architecturally capable of adding other providers later.

Commercial providers such as OpenAI, Anthropic, Google Gemini, or Mistral may be integrated through adapters rather than becoming hard dependencies of the project contract.

---

# 27. Versioning

The contract uses semantic schema versions.

Current version:

```text
1.0
```

Breaking changes should increment the major version.

Backward-compatible additions should increment the minor version.

Importers should validate the declared schema version before ingestion.

---

# 28. Compatibility Goal

A major success criterion is:

```text
ML-001
  |
  v
project.yaml
  |
  v
validator
  |
  v
importer
  |
  v
PostgreSQL
  |
  v
Website + AI Agent
```

Then a completely different project:

```text
ML-002
  |
  v
project.yaml
  |
  v
same validator
  |
  v
same importer
  |
  v
PostgreSQL
  |
  v
Website + AI Agent
```

The Atlas code should not need ML-002-specific catalogue logic.

---

# 29. Example — Multi-topic Project

```yaml
schema_version: "1.0"

id: ml-002
title: Customer Churn Prediction

domain: Machine Learning

topics:
  - EDA
  - Data Cleaning
  - Feature Engineering
  - Classification
  - Random Forest
  - Model Evaluation

project_type: machine_learning

difficulty: intermediate

status: completed

technologies:
  - Python
  - Pandas
  - scikit-learn

capabilities:
  - CLASSIFY
  - PREDICT
  - EVALUATE

learning_outcomes:
  - Perform exploratory data analysis
  - Engineer useful features
  - Train a classification model
  - Evaluate classification performance

tags:
  - churn
  - classification
  - tabular-data
```

This is one project even though it covers many topics.

---

# 30. Example — Multiple Experiences

```yaml
experiences:

  - id: notebook
    title: Training Notebook
    description: Step-by-step model training and evaluation.
    topics:
      - Classification
      - Model Evaluation
    capabilities:
      - CLASSIFY
      - EVALUATE

  - id: dashboard
    title: Churn Prediction Dashboard
    description: Interactive exploration of predictions and metrics.
    topics:
      - Classification
      - Data Visualization
    capabilities:
      - PREDICT
      - EVALUATE

  - id: api
    title: Prediction API
    description: HTTP API for serving trained-model predictions.
    topics:
      - Model Serving
      - API
    capabilities:
      - PREDICT
```

Each experience may optionally define its own execution.

---

# 31. Example — Full MLOps Project

A complete MLOps project can remain one coherent project even when it contains many topics and experiences.

Possible topics:

```text
Data Pipeline
Feature Engineering
Model Training
Experiment Tracking
Model Registry
CI/CD
Model Serving
Monitoring
Drift Detection
Observability
```

Possible experiences:

```text
Training Pipeline
Experiment Tracking View
Model Registry View
Prediction API
Monitoring Dashboard
```

The project does not need to be split into one project per topic.

---

# 32. Example — Fully Live AI RAG Website

A complete AI-powered RAG website can also remain one coherent project.

Example:

```yaml
schema_version: "1.0"

id: genai-001
title: AI-Powered RAG Website

domain: RAG & Knowledge Systems

topics:
  - RAG
  - Semantic Search
  - Knowledge Systems
  - Conversational AI
  - AI Web Applications
  - Production AI

project_type: rag_system

difficulty: advanced

status: completed

technologies:
  - Python
  - FastAPI
  - PostgreSQL
  - pgvector
  - SvelteKit
  - sentence-transformers

capabilities:
  - RETRIEVE
  - GENERATE
  - REASON
  - EVALUATE

experiences:
  - id: website
    title: Live Website

  - id: assistant
    title: RAG Assistant

  - id: semantic-search
    title: Semantic Search

  - id: evaluation
    title: Retrieval Evaluation
```

A project like this can therefore represent a complete production-style AI application rather than a single algorithm.

---

# 33. Final Architectural Model

The core model is:

```text
Project
|
+-- Domain                 <- exactly one primary
|
+-- Topics[]               <- many
|
+-- Project Type
|
+-- Difficulty
|
+-- Status
|
+-- Technologies[]
|
+-- Capabilities[]
|
+-- Learning Outcomes[]
|
+-- Artifacts[]
|
+-- Relationships[]
|
+-- Experiences[]          <- optional, many
      |
      +-- Topics[]
      |
      +-- Capabilities[]
      |
      +-- Artifacts[]
      |
      +-- Execution         <- optional
            |
            +-- browser
            +-- notebook
            +-- external_demo
            +-- sandbox (future)
```

Atlas-managed controls such as visibility, locking, and execution approval are maintained separately from contributor-owned project metadata.

---

# 34. Contract Principle

The most important rule is:

> **The project contract describes what the contributor actually built. Atlas decides how that project is catalogued, published, searched, personalized, and safely executed.**

This separation keeps the system:

- extensible
- secure
- vendor-neutral
- contributor-friendly
- AI-agent-friendly
- compatible with future GraphRAG
- compatible with future sandbox execution
- suitable for a growing catalogue of real AI/ML projects
