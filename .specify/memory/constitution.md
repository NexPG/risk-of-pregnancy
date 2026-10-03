<!-- Sync Impact Report
Version change: [CONSTITUTION_VERSION] → 1.0.0
Modified principles: Replaced all template placeholders with project-specific principles
Added sections: Technology Constraints, Development Workflow, Documentation & Artifacts
Removed sections: Generic template sections
Deferred TODOs: RATIFICATION_DATE set to today (2026-10-03)
-->

# Ecosystem Alpha Constitution

## Core Principles

### I. Educational ML Project Scope
This is an educational ML project for pregnancy risk classification (low/mid/high). Existing EDA, model comparisons, and final pipeline logic must not be altered. Core logic and evaluation metrics are preserved as-is.

### II. Final Model Specification (Locked)
The final model is sklearn SVM with RBF kernel, parameters C=100, gamma=0.03, class_weight=balanced. All numerical values for model configuration must be taken only from README.md and notebooks. These specifications are non-negotiable.

### III. Dependency & Environment Management
All dependencies are managed with Poetry. Only pyproject.toml and poetry.lock are tracked in git. The .venv directory must remain in .gitignore and must not be committed.

### IV. Code Quality & Style (NON-NEGOTIABLE)
All code must adhere to black (line length 88), isort, and flake8. Pre-commit hooks enforce these standards. Production code lives in src/; notebooks must not be deleted.

### V. Transparency & Safety Documentation
A Model Card following Mitchell et al. 2019 must be maintained. It must include an explicit disclaimer that this is not a clinical tool. Documentation must be clear about intended use and limitations.

## Additional Constraints

### Technology Constraints
- No Docker, FastAPI, or CI/CD workflows are to be added until explicitly specified in tasks.md.
- Only the specified tools and libraries are introduced without documented justification in alignment with project scope.

### Documentation & Artifacts
- Project lifecycle must be documented using BPMN 2.0 and Mermaid diagrams.
- All model configuration references must cite README.md or notebooks as the source of truth.

## Development Workflow

### Code Organization & Review
- Code changes must maintain consistency with existing project structure, naming, style, and patterns.
- Style checks (black 88, isort, flake8) and pre-commit hooks are mandatory for all commits.
- Notebooks are preserved as historical documentation and reference material.

## Governance

This Constitution supersedes conflicting practices. Amendments require clear documentation of changes, versioning updates per policy, and preservation of educational project constraints. All contributions must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2026-10-03 | **Last Amended**: 2026-10-03