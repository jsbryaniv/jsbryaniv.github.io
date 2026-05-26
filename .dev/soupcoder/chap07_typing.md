
# Code Style Guide — Typing

Typing is required in this codebase, but typing style should remain practical and consistent.


## Typing is required

All production code should include explicit type hints for:
- Function arguments
- Function return values
- Class attributes

Private helpers may be less strict only when the intent remains obvious.


## Generic type style (preferred but optional)

Both of the following styles are allowed:
- `List[int]`, `Dict[str, int]`, `Tuple[str, ...]`
- `list[int]`, `dict[str, int]`, `tuple[str, ...]`

Preferred house style is capitalized typing generics (`List`, `Dict`, etc.) because it is easier to visually distinguish types from runtime container constructors.

The key requirement is consistency within a file or module.


## Structured data typing

For internal structured data, prefer dataclasses or typed classes over raw dictionaries.

If dictionary-shaped data is unavoidable, prefer explicit schema typing (e.g. `TypedDict`) over broad `Dict[str, Any]` where practical.

Use raw dictionary typing primarily for:
- Dynamic schemas
- Endpoint/request/response payloads
- External pass-through data


## Use `Any` sparingly

`Any` is allowed only when strong typing is genuinely impractical.

When using `Any`, include a short comment explaining why type narrowing is not feasible.


## Type aliases

Use type aliases for repeated or complex types to improve readability.

```python
Vector = List[float]
FeatureRow = Dict[str, float]
```

Aliases should represent meaningful concepts, not just shorter names.


## Runtime expectations

Type hints are primarily for static checking, readability, and tooling.

**Do not assume hints enforce runtime validation unless explicit runtime checks are added.**
