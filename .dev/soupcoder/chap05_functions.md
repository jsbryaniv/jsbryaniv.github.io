
# Code Style Guide — Functions

Functions are the primary building block of this codebase.
This chapter defines both:
- How functions should be written at the code level
- How functions should be designed at the architecture level


## Section 1: Function Code Style

First let us discuss the code style rules for writing individual functions.

### Top comment

Every function should have a one-line comment directly above it that explains what the function does.

The goal is to make function intent visible when scanning a file.

```python
# Compute normalized feature vector
def compute_feature_vector(...) -> np.ndarray:
    ...
```


### Typed arguments and return

All function arguments must have explicit type annotations.
All functions must also declare their return type.

This applies to both public and private functions.

```python
# Scale vector by constant factor
def scale_vector(x: np.ndarray, factor: float) -> np.ndarray:
    ...
```


### Defaults, optional arguments, and argument kinds

Default values must be explicit and safe.

- Never use mutable default values (e.g. `[]`, `{}`, `set()`).
- Use `None` defaults when deferred initialization is needed.
- Initialize inside the function body.

```python
# Append tags to a list
def append_tags(tags: list[str] | None = None) -> list[str]:
    """..."""
    if tags is None:
        tags = []
    ...
```

Use optional arguments only when they represent true optional behavior, not multiple unrelated modes.

Prefer keyword-only arguments for tuning/configuration parameters so call sites remain readable and stable.

```python
# Smooth signal with configurable settings
def smooth_signal(
    x: np.ndarray,
    *,
    window_size: int = 5,
    normalize: bool = True,
) -> np.ndarray:
    ...
```


### Docstring (NumPy required)

A NumPy-style docstring is required for standard functions.

Docstring structure:
- First line: short summary of what the function does
- Optional detail block: additional behavior notes when needed
- `Parameters`: each argument with type and short purpose
- `Returns`: output type and short meaning
- `Raises` (optional): expected exception cases

Keep descriptions concise but clear.

```python
# Convert raw counts to probabilities
def normalize_counts(counts: np.ndarray) -> np.ndarray:
    """
    Normalize count vector to a probability vector.

    Parameters
    ----------
    counts : np.ndarray
        One-dimensional array of non-negative values.

    Returns
    -------
    np.ndarray
        Probability vector summing to one.
    """

    ...
```

Leave exactly one blank line after the docstring before function logic begins.


### Logic structure

Function bodies should be split into clear logical blocks, following Chapter 2.

- Use block comments to label each step
- Keep each block focused on one conceptual action
- Separate argument handling, core logic, and output formatting into distinct blocks

```python
# Prepare cleaned input
...

# Run core transformation
...

# Format output
...
```


### Return style

The final return statement should return a named variable, not an inline expression with logic.

Preferred pattern:
```python
# Compute adjusted score
score_adjusted = score_raw + offset

# Return output
return score_adjusted
```

Avoid complex inline returns that hide intermediate state.

Exception:
- If the function is truly trivial and can be written as a single short line (under 100 characters), inline return is acceptable.


### Exceptions to code-style rules

The following exceptions are allowed:

- Private helper functions (leading underscore) may use reduced docstrings when behavior is obvious.
- Standard dunder methods (e.g. `__init__`, `__repr__`) do not require docstrings.
- Trivial one-line functions may use compact docstring and return style as described above.
```
def add_one(x: int) -> int:
    """Add one to the input."""
    return x + 1
```


## Section 2: Function Philosophy

Next let us discuss the architectural design principles for functions in this codebase.

### Clear inputs and outputs

Functions should have explicit, predictable inputs and outputs.

- Inputs should be clearly defined and typed
- Outputs should be stable in type and shape across normal execution paths
- Avoid hidden contracts and implicit assumptions

Readers should understand what goes in and what comes out without inspecting internal implementation details.


### Separation of concerns via wrappers

Functions should be modular and composable.
Do not combine unrelated phases in one large function.

In particular:
- Keep core logic in a dedicated function
- Use thin wrappers for I/O, preprocessing, postprocessing, or orchestration
- Keep wrapper code minimal and focused on coordination

I/O should not be mixed with core business logic.


### Avoid behavior-changing arguments

Do not overload one function with arguments that fundamentally change behavior or output contract.

Avoid mode-flag designs such as:
- `mode="train" | "predict" | "debug"`
- booleans that switch between unrelated workflows

If behavior branches significantly, split into:
- A shared base function for common logic
- Separate wrapper/router functions for each behavior


### Avoid mutation and side effects

Prefer pure functions whenever practical.

- Avoid mutating input arguments
- Avoid hidden writes to global state, files, or external systems
- Return new values instead of modifying values in place, unless mutation is necessary

If side effects or mutation are required, document them explicitly in the docstring and keep them localized.


### Fail fast, fail clear

Validate assumptions early and raise explicit errors when inputs are invalid.

- Do not allow invalid state to silently propagate
- Error messages should clearly state what failed and why
- Prefer immediate, local failure over delayed, ambiguous failure downstream

This aligns with the project-wide principle of failing loudly and making debugging straightforward.

