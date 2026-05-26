
# Code Style Guide — Classes

Classes are used in this codebase to model structured state with clear invariants.
This chapter defines both:
- How classes should be written at the code level
- How classes should be designed at the architecture level


## Section 1: Class Code Style

First let us discuss the code style rules for writing individual classes.

### Top comment

Every class should have a one-line comment directly above it that explains what the class represents.

The goal is to make class intent visible when scanning a file.

```python
# Hold normalized model configuration values
class ModelConfig:
    ...
```


### Class docstring (NumPy required)

A NumPy-style docstring is required for standard classes.

Docstring structure:
- First line: short summary of what the class represents
- Optional detail block: behavioral or invariant notes when needed
- `Parameters`: constructor arguments with type and purpose
- `Attributes`: important stored fields and meanings
- `Raises` (optional): expected construction-time errors

Keep descriptions concise but clear.

```python
# Store bounded threshold configuration
class ThresholdConfig:
    """
    Configuration object for decision thresholds.

    Parameters
    ----------
    lower : float
        Minimum allowed threshold.
    upper : float
        Maximum allowed threshold.

    Attributes
    ----------
    lower : float
        Stored lower bound.
    upper : float
        Stored upper bound.

    Raises
    ------
    ValueError
        If `lower > upper`.
    """

    ...
```


### Typed attributes and method signatures

All class attributes and method signatures must be explicitly typed.

This applies to:
- Constructor parameters
- Stored attributes
- Method arguments
- Method return types

Use class-level annotations for key stored fields when helpful for readability.

```python
# Represent a bounded interval
class Interval:
    lower: float
    upper: float

    def __init__(self, lower: float, upper: float) -> None:
        ...

    def width(self) -> float:
        ...
```


### __init__ rules

The constructor should establish valid object state and do only initialization work.

- Validate invariants in `__init__` (or a dedicated validator it calls)
- Keep initialization explicit and readable
- Avoid heavy I/O, network calls, and long-running workflows in `__init__`
- Do not mutate external state during construction

If expensive setup is required, use an explicit method or factory classmethod.


### Defaults and mutable state

Default values must be explicit and safe.

- Never use mutable defaults in constructors
- Use `None` for deferred initialization
- Initialize mutable containers inside `__init__`

```python
# Track feature flags for a run
class RunState:
    def __init__(self, flags: list[str] | None = None) -> None:
        if flags is None:
            flags = []
        self.flags = flags
```


### Deferred initialization

Some classes use multi-stage initialization: the object is created first, and specific attributes are populated later.

In these cases, use the dedicated `Unset` module to represent intentionally-unset values while preserving clear type consistency.
Do not use ambiguous placeholders such as `None` when `None` is also a valid domain value.

See more regarding unset variables in Motifs.


### Method kinds: instance, classmethod, staticmethod

Use each method kind intentionally.

- Instance methods (`self`) are the default for behavior that depends on object state
- `@classmethod` is for alternate constructors or behavior tied to class-level semantics
- `@staticmethod` is rare; use only when logic is truly class-local but state-independent

If a staticmethod is broadly reusable, move it to a module-level function.


### Dataclass usage

Prefer `@dataclass` for classes that primarily store data.

As a default policy, use dataclasses for internal structured data instead of raw dictionaries.
String-key dictionary access should be treated as a boundary/dynamic pattern, not a core data-model pattern.

Use dataclasses when:
- The class mostly stores typed fields
- Boilerplate (`__init__`, `__repr__`, comparisons) is standard
- Validation needs are simple or can be handled in `__post_init__`

Avoid dataclasses when:
- Construction logic is complex
- Lifecycle management is non-trivial
- Behavior dominates over stored state

Dictionaries are still acceptable when:
- Schema is truly dynamic at runtime
- Handling endpoint/request/response payloads at system boundaries
- Passing through external data that should not be prematurely coerced


### Properties

Use `@property` only when it improves API clarity.

Good uses:
- Read-only computed values derived from internal state
- Controlled writes that enforce strict invariants

Avoid using properties to hide expensive operations or side effects.
Property access should feel lightweight and predictable.


### Private members and API surface

Mark non-public implementation details with a leading underscore.

- Public members form the supported class API
- Private members are internal and may change
- Keep public surface area minimal and intentional

Do not expose internal state directly unless it is safe and stable.


### Dunder method policy

Implement dunder methods only when they provide meaningful, standard behavior.

Common allowed cases:
- `__repr__` for clear debugging display
- `__eq__` for value comparison when semantically valid
- `__len__`, `__iter__`, `__contains__` for container-like classes

Do not implement dunder methods purely for cleverness.
Behavior should match normal Python expectations.


### Logic structure inside methods

Method bodies should follow the same logical block style as functions.

- Use block comments to label each conceptual step
- Separate validation, core logic, and output/update steps
- Keep methods focused and short when possible

If a method grows too large, extract helper functions or helper methods.


### Exceptions to code-style rules

The following exceptions are allowed:

- Standard dunder methods do not require full NumPy docstrings
- Very small data-only dataclasses may use compact docstrings
- Private helper methods may use reduced docstrings when behavior is obvious


## Section 2: Class Philosophy

Next let us discuss the architectural design principles for classes in this codebase.

### Classes model state; functions model workflows

Classes should represent structured state and invariants.

Functions should perform multi-step workflows and orchestration.
Do not use classes as a default container for procedural pipelines.


### One class, one concept

Each class should model one coherent domain concept.

Avoid classes that combine unrelated responsibilities (configuration, execution, I/O, reporting) in one object.
If responsibilities diverge, split into multiple classes or move workflow logic to functions.


### Invariants are first-class

A class should preserve valid state throughout its lifecycle.

- Validate assumptions at construction time
- Guard state-changing methods with clear checks
- Do not allow partially valid intermediate states to leak through the public API

After object creation, methods should maintain class invariants unless explicitly documented otherwise.


### Prefer composition over deep inheritance

Favor composition of small objects over deep class hierarchies.

- Use inheritance only when there is a true subtype relationship
- Keep inheritance shallow and explicit
- Avoid fragile base-class patterns and implicit override contracts

If shared behavior is utility-like, prefer module-level helpers or composed collaborators.


### Stable, minimal public interfaces

Class APIs should be small, explicit, and stable.

- Expose only what callers need
- Keep method names descriptive and predictable
- Avoid adding convenience methods that duplicate existing operations without clear value

A smaller API is easier to test, document, and maintain.


### Controlled mutation and side effects

Prefer immutable-by-default design when practical.

When mutation is required:
- Keep mutation localized and explicit
- Document which methods mutate state
- Avoid hidden writes to external systems from ordinary state methods

If a method performs I/O or external side effects, it should be clearly named and documented.


### Fail fast, fail clear

Class construction and methods should raise explicit errors when assumptions are violated.

- Do not silently coerce invalid state
- Error messages should identify what failed and why
- Prefer immediate, local failure over delayed downstream errors

This keeps object behavior predictable and debugging straightforward.


### Tests should demonstrate class contracts

Class tests should act as executable documentation.

At minimum, tests should show:
- Valid construction and typical usage
- Invariant-preserving behavior
- Expected failure paths for invalid inputs or invalid state transitions

A reader should be able to understand the class contract by reading its tests.
