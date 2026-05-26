
# Code Style Guide — Project Structure


## Overall project layout

Every project should be structured like a Python package.

Even if the project is not immediately published, it should be organized as though it could become a real pip package later.  
This keeps the codebase modular, reusable, and easy to install, test, and extend.

A standard project should contain the following top-level files and directories:

- README.md
- pyproject.toml
- src/
- scripts/
- .venv/
- .env
- .env-example
- .gitignore (derived from GitHub Python template)

Not every project will need additional directories, but this is the default foundation.


## README.md

README.md should contain the high-level project information.

It should usually include:
- What the project does
- Why it exists
- Basic installation instructions
- Basic usage instructions

The README is the main entry point for a human reader.  
A new contributor should be able to open the repository and quickly understand what the project is for and how to get started.


## pyproject.toml

pyproject.toml is the central configuration file for the project.

It should contain:
- Project metadata
- Dependencies
- Optional dependency groups
- Build system configuration
- Tool configuration for linters, formatters, type checkers, and related tooling

Project configuration should be centralized in pyproject.toml whenever possible rather than being split across many separate config files.


## src/

src/ contains the actual library code.

All reusable code should live under src/, structured as if it were a true package intended for installation and reuse.  
Code in src/ should be modular, importable, and independent of any one-off execution context.
If logic is worth keeping, testing, or reusing, it belongs in src/.

The src/ directory should be organized as a clear hierarchy of submodules.
Code should be grouped by responsibility.  
Each submodule should have a clear conceptual role.
Modules should be arranged to preserve one-directional imports and avoid circular dependencies.  
Lower-level modules should not depend on higher-level modules.

Some common submodules include:
- src/utils/ for general-purpose utilities
- src/data/ for data processing and transformations
- src/model/ for domain-specific logic and modeling

## scripts/

scripts/ contains single-use or entry-point scripts.

These are the scripts that are actually run directly for tasks such as:
- Data processing
- Batch jobs
- Maintenance tasks
- Manual utilities
- Development helpers

Scripts should remain thin whenever possible.  
They should primarily:
- Parse configuration or arguments
- Call reusable functions from src/
- Coordinate execution

Do not place core logic in scripts/ unless it is truly one-off and not worth reusing.


## .venv/

.venv/ is the project-local virtual environment.
Each project should maintain its own isolated virtual environment.  
This keeps dependencies scoped to the project and avoids cross-project contamination.
Always create the venv using `python -m venv .venv` to ensure it is properly configured for the project.


## .env & .env-example

If a project requires environment variables, it should use .env and .env-example files to manage them. 
The .env file should always be listed in the .gitignore to prevent sensitive information from being committed.
The .env-example file should be included in version control to document the required environment variables.
A contributor should be able to copy .env-example to .env and know exactly which fields must be filled in.

## .gitignore

.gitignore should be copied from the standard GitHub Python template.

Custom additions may be added at the bottom under a dedicated section:
```
# ------------------------------------
# --- Custom Ignores
# ------------------------------------
```

Do not scatter project-specific ignore rules throughout the file.  
Keep custom rules grouped in one place.

## Summary

Projects should be structured as installable Python packages by default.

- README.md explains the project
- pyproject.toml centralizes metadata and tooling
- src/ contains reusable code
- scripts/ contains runnable one-off scripts
- .env-example documents required environment variables
- .gitignore should follow the GitHub template with custom ignores grouped at the bottom

Inside src/, code should be organized into a clear module hierarchy with reusable utilities separated from domain-specific logic and imports flowing in one direction.
