
# Code Style Guide — Errors

Error handling in this codebase is designed for clarity, speed of debugging, and predictable failure behavior.


## Section 1: Error Handling Code Style

First let us discuss the code style rules for writing error handling.

### Use explicit exceptions in production code

Use explicit `raise` statements for runtime validation and invalid state.

- Prefer specific exception types (`ValueError`, `TypeError`, etc.)
- Include a clear error message that explains what failed
- Do not rely on `assert` for production input/state validation

```python
# Validate score range
if score < 0 or score > 1:
    raise ValueError(f"score must be in [0, 1], got {score}")
```


### Assert is allowed in tests

`assert` is allowed and preferred in tests when it is shorter and clearer.

In production logic, use explicit exceptions instead.


### Avoid silent fallback patterns

Do not use fallback patterns that hide missing or invalid data unless fallback behavior is explicitly intended.

Prefer strict access:
```python
value = data["field"]
```

Avoid silent access by default:
```python
value = data.get("field")
```

Use `.get(...)` only when missing keys are an intentional and documented case.


### Let Python raise natural errors when appropriate

Do not add redundant checks that only duplicate built-in Python failures.

If a function contract already guarantees a type/shape, it is acceptable to rely on natural exceptions from normal operations.

The goal is to avoid defensive boilerplate that increases code size without improving clarity.


### Never suppress errors silently

Avoid patterns that hide failures:
- `except: pass`
- Returning default success values after critical failures
- Swallowing exceptions without logging or re-raising

If an operation fails, that failure should remain visible.


## Section 2: Error Handling Philosophy

Next let us discuss the architectural design principles for error handling in this codebase.

### Fail fast, fail loud

Errors should surface immediately at the point of invalid state or invalid input.

- Do not defer known failures
- Do not continue execution in corrupted state
- Prefer immediate local failure over delayed downstream failure

This keeps root causes obvious and debugging straightforward.


### Clarity over defensive complexity

Error handling should improve understanding, not obscure it.

- Use explicit checks only where they add real clarity
- Avoid stacking many pre-checks "just in case"
- Keep validation close to where assumptions matter

Simple, direct failure behavior is preferred over overly defensive code.


### Boundary validation, internal trust

Validate aggressively at boundaries (external inputs, files, user config).

Inside well-typed internal code paths, trust established contracts and let Python enforce them naturally.

This keeps core logic clean while still protecting real input risk points.


### Errors are part of the API contract

A caller should be able to understand expected failure modes from reading function/class documentation and tests.

Tests should include representative failure cases so error behavior remains explicit and stable.
