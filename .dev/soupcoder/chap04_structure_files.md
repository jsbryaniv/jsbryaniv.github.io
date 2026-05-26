
# Code Style Guide — File Structure

Every file in the repository follows the same four-part outline:

1. File documentation
2. Imports
3. Logic / Functions / Classes
4. Test or main entry point.

This consistency keeps every module instantly familiar, keeps imports tidy, and guarantees that each file remains testable on its own.


## File documentation

Every file should begin with a brief comment describing its purpose and contents.
- This should be a high-level summary, not a line-by-line explanation.
- It should explain the overall intent and structure of the file, not just what it does.
- It should have a title explaining in a few words what the file is about followed by a more detailed description of the file's role in the project and how it achieves its goals.
- Only include examples if the file's purpose is non-obvious and requires additional context to understand.
- The goal is to give a reader an immediate understanding of the file's role and how it fits into the larger project when scanning the codebase.

### Examples:

Here is an example for I/O functions, where the intent is clear and no detailed explanation is necessary:
```python
# Documentation
"""
I/O Functions

This module contains functions for reading and writing data to various formats (CSV, JSON, databases, etc.).
"""
```

Here is an example for a more complex file that requires a detailed overview to explain its purpose and structure:
```python
# Documentation
"""
Unset / Missing Attribute Helpers

This file creates a framework for handling unset / missing values during class initialization.

The problem it solves is when we have classes with two initialization periods, one where the
object is created, and another where the attributes are populated. During the first period, 
we want to be able to distinguish between attributes that are intentionally left unset and those 
that are missing, without setting the attribute to None or some other sentinel that could break 
type checking down the line.

The solution is to define a special object called Unset that can be used as a default value for 
attributes that are intentionally left unset. Then we create two helper functions, unset() and 
is_unset(x), to create unset objects and check if a value is unset, respectively.
"""
```


## Imports

Imports are always grouped and labeled in this exact order:

```python
# Annotation imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any, Dict, List
    # Additional type-only imports ...

# Regular imports
import os
import numpy as np
import matplotlib as pyplot
from pandas import DataFrame

# Local imports
from myproject.core import models
from myproject.services.runner import Runner
```

Detailed rules:
- Include the header comments exactly as written to make sections scannable.
- Annotation imports contain anything used exclusively for type checking or forward references. Prefer guarding heavyweight imports behind `if TYPE_CHECKING` so they do not execute at runtime.
- Regular imports are for standard library or third-party packages.
- Local imports bring symbols from within the current project/package.
- Inside each section, list strict `import module` statements first, followed by `from module import name` statements.
- Leave a blank line between sections, never inside sections unless separating the `if TYPE_CHECKING` block from the header comment.
- Optional: within each import subsection (e.g., all strict imports), sort shortest to longest so the visual flow is stable and more readable.


## Logic

All executable logic belongs inside functions or classes.

- Avoid executing code at import time. Wrap any necessary setup logic in a function or class.
- Keep the top level reserved for constant definitions, configuration, dataclass declarations, or other immutable metadata.
- Avoid free-floating statements (database calls, print statements, etc.) at import time. If absolutely necessary, wrap them in a helper function and call it from the `__main__` guard.
- Prefer small, composable functions over monolithic blocks so they can be imported and tested independently.

Within the logic section, prefer the following order when applicable:
- Constants and configuration
- Data structures (e.g. dataclasses)
- Helper functions
- Core functions
- Public API functions

## Tests or Main Entry Point

Most every file ends with either a `test_file` shim or a `main` entry point, that is executed when the file is run directly. This does not apply to extremely simple files that contain only a few lines of logic, but for any file with more than a handful of lines, this is required. This ensures that every file is testable on its own and provides a clear example of how to use the module.

Note that not every test needs to be colocated with the code it tests for. For example, test that check system wide behavior can be placed in a dedicated test folder. But every file should still have a test shim at the bottom that can be used for quick smoke tests and documentation.

### Test template

Here is the template for a test shim at the bottom of a module:
```python
# ------------------------------------
# --- Test
# ------------------------------------

# Define test
def test_file() -> None:
    """Module-level smoke test."""

    # ... test logic here ...

    # Done
    print(f"All tests passed for {__file__}")
    return

# Run test when executed directly
if __name__ == "__main__":
    test_file()
```

***IMPORTANT***: One major design philosophy when creating the testing logic is that *tests should double as documentation*.  
The test function should be a clear example of how to use the module, and it should be easy to understand the module's purpose and API just by reading the test.
This way, when a test passes, we automatically have up-to-date documentation with no extra work.

### Main script variant

When the file represents an executable script, expose a `main()` function and call it from the guard. You may still include a lightweight test helper if it makes sense, but the guard must stay at the bottom.

```python
# ------------------------------------
# --- Main
# ------------------------------------

# Define main entry point
def main() -> None:
    """Entrypoint for this script."""

    # ... main logic here ...

    # Done
    print(f"Finished executing {__file__}")
    return

# Run main when executed directly
if __name__ == "__main__":
    main()
```

## Summary

Every file should follow the same four-part structure: documentation, imports, logic, and test / main entry point.
- Documentation should be a high-level summary of the file's purpose and structure, not a line-by-line explanation.
- Imports are grouped into annotation, regular, and local sections with specific ordering rules.
- Logic is encapsulated in functions or classes, with no free-floating statements at the top level.
- Each file ends with a standardized test shim or a `main` entry point, never both, and the guard is always at the bottom.
This structure ensures that every file is immediately familiar, keeps imports organized, and guarantees that all code is testable on its own.
