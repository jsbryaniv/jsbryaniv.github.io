
# Code Style Guide — General Code Style


## Clarity above all

Clarity is the highest priority in code. We should structure code with the goal of making it as easy as possible for someone else to read and understand it.

It is almost always better to write out steps explicitly rather than compress logic into a single clever line.
Avoid dense expressions, nested logic, or implicit transformations that obscure intent.

Prefer:
- Step-by-step transformations
- Intermediate variables with clear names
- Explicit control flow

Code should be understandable on first read without mental unpacking.


## Logical grouping and spacing

Code should be organized into clear, logical blocks.
- Group related operations together
- Separate unrelated blocks with whitespace
- Each block should represent a single conceptual step

A reader should be able to scan the file and immediately identify:
- Where one step ends
- Where the next begins

Avoid long, uninterrupted blocks of code.
Avoid scattered unconnected lines that break the flow.


## Indentation and alignment

Aesthetics matter. Code should be visually organized and easy to scan.

Indentation is used to reinforce structure and improve readability.
- Align related lines when it improves clarity
- Keep indentation visually consistent across similar constructs
- Use parentheses to break long lines across multiple lines
- Indent function arguments at the parentheses level for better readability

Example:
```
result = (
    process_data(data=data, config=config)
    + adjust_offset(offset=offset)
    - correction_term
)

x = myfunc(
    data=data,
    config=config,
    offset=offset,
)
```


## Explicit function arguments

When a function has multiple arguments, especially if they are of the same type, use keyword arguments to improve readability and reduce errors.
```
x = myfunc(data=data, config=config, offset=offset)
```
This makes it clear which value corresponds to which parameter, especially when scanning code quickly.  
Do not rely on positional arguments, as they reduce readability and are unstable to changes in the function signature. 


## Explicit variables over strings

When possible, avoid accessing data via strings (e.g. `data["field"]`) and instead use variables or attributes (e.g. `data.field`).  
This improves readability, allows for better tooling support (e.g. autocompletion, refactoring), and reduces the risk of typos.  
If you must use strings (e.g. for dynamic access), consider defining constants for the keys to improve readability and maintainability.


## Structured data over raw dictionaries

For internal structured data, prefer typed objects and attributes over raw string-key dictionaries.

- Prefer dataclasses or typed classes for stable schemas
- Reserve dictionaries for dynamic schemas or boundary data (e.g. API payloads, endpoint I/O)
- Avoid passing raw `dict[str, Any]` through core logic when structure is known

This improves refactor safety, static checking, and IDE tooling (rename, autocomplete, jump-to-definition).


## Naming conventions

Use consistent and descriptive naming.
Names involving multiple words should go from left to right largest scope to smallest (e.g. `data_train, data_test` rather than `train_data, test_data`), as this improves readability when scanning vertically. 

When possible, use consistent naming lengths to improve visual alignment:
```
t_start = ...
t_final = ...

f_load  = ...
f_save  = ...

x_source = ...
x_target = ...
```
It turns out that many opposite pairs in the world have the same number of letters. Try to use them when possible.

We follow standard Python (PEP 8) naming conventions.

- Variables: lowercase snake_case
  - Short names are acceptable for simple or local variables
  - Prefer descriptive names for non-trivial values

- Functions: lowercase snake_case
  - Use verbs or verb phrases that describe the operation

- Classes: CamelCase (CapWords)
  - Names should represent entities or structured data

- Constants: UPPERCASE_SNAKE_CASE
  - Used for fixed values and sentinels

- Private/internal names: leading underscore
  - Indicates non-public API (e.g., `_helper`, `_InternalClass`)

- Modules/files: lowercase snake_case
  - Keep names short and descriptive

Avoid:
- Abbreviations unless they are standard or clear from context
- Single-letter names outside of well-understood contexts (e.g. `i` for loop index, `x` for generic data)


## Comments

Comments are required to explain structure and intent.

### Block comments

Every logical block of code should have a comment above it, even if the operation is simple.
```
# Normalize vector
v = v / np.linalg.norm(v)

# Compute loss
loss = compute_loss(predictions, targets)
```
The goal is to make the structure of the code immediately clear when scanning.

### Inline comments

Use inline comments sparingly.
- Only when additional clarification is needed
- Do not restate obvious operations

### Section comments

Use section comments to separate larger regions of code.  
Use sparingly, only when grouping multiple related blocks.
```
# ------------------------------------
# --- Data Processing
# ------------------------------------
```

Avoid overusing section headers, as they reduce their effectiveness.


## Summary

Code should be:
- Clear and explicit
- Visually organized
- Consistently structured

A reader should be able to understand both the structure and intent of the code by scanning it, without deep inspection.
