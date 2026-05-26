
# Code Style Guide — Overview


## Introduction

This guide defines the coding standards for this repository. Its purpose is to ensure consistency, readability, and maintainability across the codebase.

It covers how code should be structured at multiple levels, including:
- Project organization
- File structure
- Function and class design
- Typing and conventions

This guide is organized into:
- **Overview** — high-level principles and philosophy  
- **Chapters** — concrete rules for specific areas (e.g. files, functions, typing)  
- **Motifs** — preferred solutions for recurring design problems  
- **Templates** — standard code scaffolds for common patterns  

The overview defines the high-level principles and goals. The chapters show how to apply those principles in practice.


## Philosophy

### Clarity is the highest priority

Code should be easy to read and understand.  
Avoid clever or overly compact solutions if they reduce readability.  
Prefer explicit, straightforward implementations.  
Be verbose about every action; *you cannot be too pedantic* and *redundancy is good*.  
Use descriptive names for variables, functions, and modules.  
Write code that is self-explanatory and easy to follow.

### Aesthetics matter

Code should not only be correct, but also visually organized and easy to scan.

- Maintain consistent spacing and alignment where it improves readability  
- Group related lines into clear logical blocks  
- Use whitespace intentionally to separate concepts  
- Avoid dense, cluttered code  

Well-formatted code reduces cognitive load and makes structure immediately apparent.

### Colocation of related code, testing, & documentation

Related code, tests, and documentation should be colocated in the same file or module.  
Tests should be colocated with the code they test, rather than in a separate test directory.  
Documentation should be integrated into the codebase as docstrings and comments, rather than in separate files.
There is no separate documentation, *the code is the documentation*.
In particular, tests should be set up in such a way that they double as documentation.  
The goal is to create a self explanatory codebase that updates itself as the code changes, without requiring separate maintenance of documentation or tests.  
This improves discoverability and makes it easier to maintain the relationship between code, tests, and documentation.

### Function-first framework

The codebase should be structured as a library of well-defined functions.

Functions should:
- Have clear inputs and outputs  
- Perform a single, well-defined task  
- Be reusable and composable  

Avoid hidden state and implicit behavior. Prefer pure or near-pure functions when possible.

### Modular design: one action, one function

Each function should do exactly one thing.  
Do not mix responsibilities (e.g. loading data and processing it).  
This improves testability, reuse, and clarity.

### Objects hold data, not behavior

Objects should represent structured state with identity, not workflows.  
Use classes when data has a clear structure, maintains invariants, or benefits from a stable interface (e.g. indexing or caching).
Avoid using classes to hide multi-step processing.

Class methods should only be used for behavior intrinsic to the object (e.g. representation, validation, container access, or domain-standard updates like `model.fit`). The notable exception is when the class object's stored data exists solely to support a function's behavior (like parameters of a model), then it is acceptable for the class to have methods that perform the main behavior of the object. In this case, the class is essentially a structured namespace for the parameters, and the methods are the main interface for using those parameters. However, even in this case, it is important to ensure that the class does not become a catch-all for unrelated functionality or state.

Objects hold data, functions perform logic -- avoid mixing these responsibilities.

### Clear hierarchy of modules

Modules should form a clear, directed hierarchy.  
Imports should be one-directional.  
Lower-level modules should not depend on higher-level modules.  
Cyclic dependencies are not allowed, except for annotation imports (e.g. for type hints), which may reference higher-level modules when necessary.

### Fail loudly

Do not write overly robust code when you do not have to.
If an error occurs, it should be immediately obvious and provide a clear message about what went wrong.  
Avoid silent failures, hidden exceptions, or complex error handling that obscures the root cause.
Failing loudly makes it easier to identify and fix issues quickly, rather than allowing bugs to propagate unnoticed.

### Use industry standards

When a standard solution exists (libraries, patterns, conventions), prefer it over custom implementations.  
Do not reinvent common functionality without a strong reason.

### Set up code to work well with tooling

Code should be structured to work well with linters, formatters, type checkers, and IDEs.
This means following standard conventions, being explicit about types, and avoiding patterns that confuse tools (e.g. dynamic imports, metaprogramming).
Code should be clear and well documented so that AI tools can easily understand and assist.
In particular, create code that is compatible with the "Rename Symbol" feature in IDEs, so that names can be easily refactored without breaking references.


## Conclusion

Many of our principles will inevitably lead to heavier, more verbose code. 
This is intentional and by design. 
The goal is to create a codebase that is easy to read, understand, and maintain, even if it means writing more lines of code or being more explicit.

These rules and principles are designed to create a codebase that is easy to understand, maintain, and extend.  
This ensures the codebase remains structured, predictable, and scalable.
