---
date: YYYY-MM-DD 12:00:01
layout: post
title: "Programming Principles: Keep Code DRY"
subtitle: "Don't Repeat Yourself"
description: A discussion of the programming principle of DRY code, and how to write code that is easy to understand and maintain.
image: assets/coverart_programming_principles.png
category: programming-principles
tags:
  - programming
---

Here I discuss Programming Principles. Today I discuss the principle of DRY (Don't Repeat Yourself).

## Introduction

DRY stands for "Don't Repeat Yourself". DRY code is code where every important function or variable is defined in exactly one place. Keeping code DRY makes it much easier to maintain. If you have to make a change to your code and the same code is repeated in multiple places, you have to make the change in every place, and every time you do that you invite the possibility of making a mistake. If instead you define the code in one place and import it elsewhere, you only have to make the change once, and you can be confident that it is consistent everywhere.

## Why is DRY Important?

Every line you write in a codebase is a line of code you need to maintain. If you have WET (write every time) code where you write the same thing in multiple places, then you need to maintain each separate copy. But not only do you need to maintain each copy, you also need to ensure that the copies are consistent with each other. The more things you need to maintain, the more opportunities there are for you to make a mistake when project requirements change. For this reason, it's extremely advantageous to write code in ways where every variable, function, or piece of knowledge has a single source of truth.

## How to Implement DRY

The easiest way to make sure code is DRY is to define things once and derive related quantities from there. Here are a few common techniques:

### Use Shared Constants

Instead of repeating the same value throughout your code:

```python
resize(image, 224)
crop(image, 224)
assert image.shape == (224, 224)
```

Define it once as a shared constant:

```python
IMAGE_SIZE = 224

resize(image, IMAGE_SIZE)
crop(image, IMAGE_SIZE)
assert image.shape == (IMAGE_SIZE, IMAGE_SIZE)
```

Now, if the image size ever changes, you only need to update one line of code.

### Derive Related Values

Sometimes two variables always contain the same information. Rather than defining each one independently:

```python
SQUARE_WIDTH = 224
SQUARE_HEIGHT = 224
```

Define one value and derive the others from it:

```python
SQUARE_SIDE = 224
SQUARE_WIDTH = SQUARE_SIDE
SQUARE_HEIGHT = SQUARE_SIDE
```

This ensures there is only one source of truth for the image size. If the value changes, every dependent variable updates automatically.

### Extract Helper Functions

Instead of copying the same sequence of operations throughout your code:

```python
results = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
}

with open(file_path, "w") as file:
    json.dump(results, file, indent=4)
```

Extract the repeated logic into a helper function:

```python
def save_results(
    accuracy,
    precision,
    recall,
    file_path,
):
    results = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
    }

    with open(file_path, "w") as file:
        json.dump(results, file, indent=4)
```

Now, whenever you need to save results, you simply call:

```python
save_results(
    accuracy,
    precision,
    recall,
    "results.json",
)
```

If you later decide to change the file format, add another field, or modify how the data is written, you only need to update the helper function. Every place that calls it immediately benefits from the change.

One important caveat is that DRY does **not** mean eliminating every duplicated line of code. Sometimes two pieces of code look similar today but represent different concepts. If they are likely to evolve independently in the future, they should remain separate.

The goal of DRY is not to eliminate duplicated code. The goal is to eliminate duplicated knowledge.

## Conclusion

WET code is like wet garbage: it attracts bugs! Try to keep your code DRY instead. DRY code is easier to maintain, easier to understand, and less likely to attract bugs.

Thanks for reading! 

