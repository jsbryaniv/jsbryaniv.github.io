---
date: 2026-08-31 12:00:01
layout: post
title: "Programming Principles: One Source of Truth"
subtitle: "Prevent Contradictory Information"
description: A discussion of the programming principle of One Source of Truth, and how it prevents contradictory information.
image: assets/coverart_programming_principles.png
category: programming-principles
tags:
  - programming
---

Today I discuss the principle of One Source of Truth.

## Introduction

When a program stores the same piece of information in multiple places, an important question appears: which version should we trust?

Suppose an online store saves the price of a product in its database, a config file, and the code that generates the checkout page. Everything works while those three values agree. But eventually somebody changes one of them and forgets to change the others. Now the product page shows one price, the shopping cart calculates another, and the database contains a third.

The problem is not simply that the value was repeated. The deeper problem is that the program has no single source of truth.

The principle of One Source of Truth says that every important piece of information should have one central source. Other parts of the program should get or calculate the information from that source rather than keeping separate copies.

## Why Is One Source of Truth Important?

Multiple sources of truth make it unclear which value is correct.

Consider a user account with an editable birth date and a separately stored age:

```python
user = {
    "birth_date": "1990-08-31",
    "age": 35,
}
```

At first, these values agree. But age changes over time, and the user might correct their birth date. If the program updates one field without updating the other, the two values contradict each other.

Which one is correct?

A better design stores only the birth date and calculates the age when needed:

```python
user = {
    "birth_date": "1990-08-31",
}


def calculate_age(birth_date, today):
    # Calculate age based on birth_date and today's date
    age = ...
    return age
```

Now the birth date is the source of truth, and age is derived from it. The values can no longer drift apart.

This is the core benefit of One Source of Truth: it prevents the program from contradicting itself.

## How to Establish One Source of Truth

### Decide Which Value Is the Source of Truth

First, decide which value should be the source of truth. In the example above, birth date is stable information supplied by the user, while age is merely a calculation based on that information. Therefore, birth date should be stored and age should be derived.

A good source of truth is usually the value closest to the original fact.

### Derive Values Instead of Storing Them

Whenever one value can be calculated reliably from another, prefer calculating it:

```python
subtotal = sum(item.price for item in cart)
tax = subtotal * TAX_RATE
total = subtotal + tax
```

Avoid storing `subtotal`, `tax`, and `total` as independent editable values unless you have a specific reason to preserve them.


### If You Must Duplicate, Write Consistency Checks

Sometimes it is impossible to avoid defining the same thing in multiple places. For example, I am working on an application with a Python backend and a TypeScript frontend. The backend stores an object as a Python class, but the frontend also needs a TypeScript version of that class. There is no easy way to share the class between the two languages, so I have to define it twice.

In this situation, I can create a JSON Schema that describes what the object should look like. This schema becomes the source of truth. I can then write tests in Python and TypeScript that check both classes against the schema.

The classes are still defined in two places, but now I have a way to make sure they stay consistent. If I change one class and forget to update the other, the tests will fail and let me know that they no longer match.

## Conclusion

Whenever the same information appears in multiple places, ask yourself which place is the source of truth. Store the original information in one place and calculate other values from it whenever possible.

Sometimes the same information has to be copied. When that happens, add tests to make sure the copies stay consistent. Your program should never be confused about which copy is the truth.

Thanks for reading!
