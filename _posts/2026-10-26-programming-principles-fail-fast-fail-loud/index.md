---
layout: post
title: "Programming Principles: Fail Fast, Fail Loud"
subtitle: "Don't Let Errors Pass Silently"
description: A discussion of why code should flag errors immediately, and how overly forgiving error handling can hide bugs.
image: assets/coverart_programming_principles.png
category: programming-principles
tags:
  - programming
---

Here I discuss Programming Principles. Today I discuss the principle of Fail Fast, Fail Loud.

## Introduction

If you are going to fail, fail loudly and make sure everyone knows! I'm talking about coding, of course. This would be terrible advice for regular life.

The principle of Fail Fast, Fail Loud says that when errors inevitably arise in our code, we should flag them immediately and make it clear what went wrong. There is often a temptation to make code bulletproof by adding generic error handling so that it keeps running no matter what happens. However, naive error handling can introduce **silent errors**, where the code runs without reporting a problem, but it does something different from what we intended.

This is especially important in the age of vibe coding because AI coding agents sometimes add unnecessary robustness that allows bad data to slip through. When we ask an agent to get code running, it may introduce a fallback that makes an error disappear without fixing the underlying problem. The program runs, but that does not mean it does what we want! Getting code to run does not guarantee that an agent has caught every error. If you have a skill or instruction file for your coding agent, I highly recommend adding a line about failing loudly.

## Examples of Silent Errors

Pay attention to these patterns when you are writing code to avoid silent errors.

### Using Defaults for Required Inputs

Suppose we are writing a program that calculates the total price of an order. Each item is represented by a dictionary containing its price and quantity, and we have a function that reads the item dictionary to calculate the total. We might be tempted to use `.get()` with a default value for the quantity, like this:

```python
item = {
    "price": 20,
    "quantity": 3,
}


def calculate_item_total(item):
    price = item.get("price", 0)
    quantity = item.get("quantity", 1)
    return price * quantity
```

This works for our example, and we might even think it's nice that we supply helpful defaults when values are missing from the input. However, suppose another part of the program accidentally gives us this dictionary instead:

```python
item = {
    "price": 20,
    "quanity": 3,  # A typo!
}
```

The function cannot find `"quantity"`, so it uses the default value of `1` and returns a total of `20` instead of `60`. Nothing crashes. We simply get the wrong answer.

Now compare that with this implementation:

```python
def calculate_item_total(item):
    price = item["price"]
    quantity = item["quantity"]
    return price * quantity
```

The beauty of indexing the dictionary directly with the key instead of using `.get()` is that if the key is missing, Python immediately raises a `KeyError`. With the malformed dictionary above, we get `KeyError: 'quantity'`. We know which required key is missing, and the traceback tells us where the code tried to access it. We can fix the typo before an incorrect total gets saved or used somewhere else.

### Catching Errors and Returning an Empty Result

Another common pattern is wrapping an operation in a broad `try`/`except` block and returning a default when anything goes wrong:

```python
import json


def load_orders(file_path):
    try:
        with open(file_path) as file:
            return json.load(file)
    except Exception:
        return []
```

If the file is missing, unreadable, or contains malformed JSON, this function returns an empty list. The rest of the program can then continue normally:

```python
orders = load_orders("orders.json")
total_revenue = sum(order["total"] for order in orders)
```

Now our report shows zero revenue. But we did not successfully load the orders and discover that there were none. We failed to load them at all!

**The exception handler has made those two situations indistinguishable**. A failed operation now looks like a successful operation that returned no results.

In this case, the simplest improvement is to remove the exception handler:

```python
def load_orders(file_path):
    with open(file_path) as file:
        return json.load(file)
```

If loading fails, the original exception tells us what went wrong. We can then fix the file, its permissions, or the code supplying its path. Returning an empty list does none of those things. It just hides the problem.

## How to Write Fail Fast, Fail Loud Code

Here are five habits that help prevent silent errors:

1. **Make required inputs required.** Use `data["key"]` when the key must exist. Use `.get()` and defaults when absence is an expected, valid situation.

   ```python
   # Don't supply a default for a required quantity.
   quantity = item.get("quantity", 1)

   # Require the quantity instead.
   quantity = item["quantity"]

   # Defaults are fine for genuinely optional fields.
   note = item.get("note", "")
   ```

2. **Check inputs before using them.** Validate incoming data for missing fields, incorrect types, and invalid values before passing it through the rest of the program. Here is a simple check for a positive integer quantity:

   ```python
   def validate_quantity(quantity):
       if type(quantity) is not int or quantity <= 0:
           raise ValueError("quantity must be a positive integer")
   ```

3. **Only catch errors you can meaningfully handle.** Catch specific exceptions that your program can recover from, and let other errors propagate. For example, if a settings file is optional, we can use defaults when it is missing:

   ```python
   import json

   try:
       with open("settings.json") as file:
           settings = json.load(file)
   except FileNotFoundError:
       # Use defaults when the optional file is missing.
       settings = {"theme": "light"}
   # Malformed JSON and permission errors still propagate.
   ```

4. **Fix the cause instead of accommodating the mistake.** Investigate why a required value is missing rather than adding a default to make the error disappear. This is especially important when directing coding agents.

   ```python
   # Fix the typo where the data is created.
   item = {"quanity": 3}   # Wrong
   item = {"quantity": 3}  # Correct
   ```

5. **Check that bad inputs actually fail.** Test missing required keys, malformed data, and failed operations. Make sure they produce clear errors instead of plausible-looking results. For example, using `pytest`:

   ```python
   import pytest


   def test_invalid_quantity_fails():
       with pytest.raises(ValueError, match="positive integer"):
           validate_quantity(-3)
   ```


For an AI coding agent, a useful instruction is:

> Follow Fail Fast, Fail Loud. Trace errors to their source and fix the underlying problem. Do not add silent fallbacks or make required inputs optional to suppress errors. Use defaults only for genuinely optional inputs, and test that invalid inputs fail clearly.

## Conclusion

Silent errors are the most dangerous errors because they give us results that look like they can be trusted. A program that crashes tells us that something needs attention. A program that quietly produces the wrong answer might go unnoticed for a long time.

Be intentional about error handling. Decide which situations your code can reasonably recover from, and let it fail loudly when it cannot. Trying to make a program robust to every possible error can make its actual bugs much harder to find.

Thanks for reading!
