---
layout: post
title: "Programming Principles: Explicit Is Better Than Implicit"
subtitle: "Put Your Assumptions on the Page"
description: A discussion of why code should state its assumptions openly, in the code itself, in the data it handles, and in its comments.
image: assets/coverart_programming_principles.png
category: programming-principles
tags:
  - programming
---

Here I discuss Programming Principles. Today I discuss the principle of Explicit Is Better Than Implicit.

## Introduction

"Explicit is better than implicit" is the second line of the Zen of Python, right after "Beautiful is better than ugly." It is also pretty good advice for relationships, but I'll stick to programming.

The principle says that **everything that affects what your code does should be visible where the code is read**. Implicit code relies on something the reader can't see: a convention, a default, a unit, or something the author just happened to know when they wrote it. Explicit code puts those assumptions on the page.

Implicit code is not wrong. It usually works perfectly well, as long as everyone who touches it has similar context and understanding. The problem is that if a new person touches the code, they may not have the same context. This makes your code hard to understand for new teammates and for your future self. Tests only go so far, and they can't catch every misunderstanding. Often implicit bugs don't cause errors immediately, but they can lead to subtle and hard-to-find issues down the line.

But, being explicit does **not** mean being verbose. Adding words is only worth it when those words carry information the reader would otherwise have to guess. In this post I look at three places where hidden assumptions tend to live: in the code itself, in the data, and in the things only comments and documentation can say.

## Be Explicit in Your Code

The first level to explicit coding is being explicit in the code itself. Small choices about how we write a call or a condition decide whether the reader can see what the code does, or has to go look it up.

### Name Your Arguments

Here is a function call:

```python
resize(image, 800, True, False)
```

We can probably guess that `800` is a width. But what are `True` and `False`? To find out, we have to open the function's definition:

```python
def resize(image, width, keep_aspect=True, crop=False):
    ...
```

Now compare the call above with this one:

```python
resize(image, width=800, keep_aspect=True, crop=False)
```

It does exactly the same thing, but anyone reading it knows what it does without leaving the line. It is also much harder to get wrong. In the first version, swapping `True` and `False` by accident produces a cropped image with a distorted aspect ratio, and nothing complains.

If you are writing the function, you can require callers to name the flags by putting a `*` in the signature. Every argument after the `*` must be passed by name:

```python
def resize(image, width, *, keep_aspect=True, crop=False):
    ...
```

Now `resize(image, 800, True, False)` raises a `TypeError`, and the only way to call the function is the readable way.

### Say What Your Conditions Check

Suppose we have a function that removes readings below an optional threshold:

```python
def filter_signal(signal, threshold=None):
    """Remove readings below a threshold, if one is given."""

    # Apply the threshold if one is given
    if threshold:
        signal = signal[signal >= threshold]

    # Return the filtered signal
    return signal
```

This looks fine. Now suppose we want to drop every negative reading, so we call `filter_signal(signal, threshold=0)`. The function returns the signal unchanged, negative readings and all.

The problem is the line `if threshold:`. We meant to ask, "Was a threshold given?" But the code actually asks, "Is the threshold truthy?" In Python, `0` counts as `False`, just like `None`, an empty list, and an empty string. So a threshold of zero is treated exactly the same as no threshold at all.

The fix is to write the question we actually mean:

```python
    # Apply the threshold if one is given
    if threshold is not None:
        signal = signal[signal >= threshold]
```

`if value:` is a handy shortcut, and it is fine when every falsy value really means the same thing. But when zero or an empty collection is a valid input, the shortcut hides a decision that the reader can't see, and that the author may not have realized they were making.

### Don't Depend on Where the Code Is Run

Here is a function that loads a settings file:

```python
import json


def load_settings():
    with open("data/settings.json") as file:
        return json.load(file)
```

The path `"data/settings.json"` is relative, and relative paths are resolved from the folder you were in when you started Python, not from the folder the script lives in. If you run the script from the project folder, it works. If you run it from somewhere else, or a scheduled job runs it from your home folder, it can't find the file. Worse, if a different `data/settings.json` happens to exist in that other folder, it loads the wrong settings without complaint.

The code silently depends on something that isn't in the code at all: the folder it was run from. We can make that explicit by building the path from a known location:

```python
import json
from pathlib import Path

# Folder that contains this script
PATH_PROJECT = Path(__file__).resolve().parent


def load_settings():
    path_settings = PATH_PROJECT / "data" / "settings.json"
    with open(path_settings) as file:
        return json.load(file)
```

Now the function loads the same file no matter where it is run from. An even more explicit option is to have the caller pass the path in as an argument, so the function makes no assumption about where its file lives.

## Be Specific About Your Data

The second level to explicit coding is being explicit about the data. A number in a program is just a number. Whatever it means, whether that's a unit, a time zone, or which axis is which, exists only in the programmer's head unless we write it down.

### Put Units in Names

What does this call do?

```python
simulate(duration=5, step=10)
```

Is the duration 5 seconds or 5 milliseconds? Is the step 10 milliseconds or 10 microseconds? The code can't tell us, so the caller has to guess, or open the source code and hope it says.

This kind of mistake has destroyed a spacecraft. In 1999, NASA lost the Mars Climate Orbiter because one piece of software reported thruster impulse in pound-force seconds, and the navigation software that read those numbers expected newton-seconds. Every number was correct in its own units. The units themselves were implicit, and the mismatch put the orbiter on the wrong path to Mars, where it was lost.

The simplest fix is to put the unit in the name:

```python
simulate(duration_s=5, step_ms=10)
```

This matters most for **public interfaces**: function arguments, configuration files, and columns in data files that other people will read. Your callers can't see your internals, so the name is often the only place they will ever see the unit.

Inside a project, the strongest habit is to **pick one convention and convert at the edges**. For example, decide that every time inside your code is in seconds. When data comes in using other units, convert it right away, in one place:

```python
# Unit conversions
MS_PER_S = 1000


def load_timestamps(path_file):
    """Load timestamps, converting them from milliseconds to seconds."""

    # The file stores timestamps in milliseconds
    timestamps_ms = np.loadtxt(path_file)

    # Convert to seconds, the unit used everywhere else in this project
    timestamps_s = timestamps_ms / MS_PER_S

    # Return the timestamps
    return timestamps_s
```

Everything past this function can assume seconds. This is [One Source of Truth](/blog/2026/08/programming-principles-one-source-of-truth/) applied to units: the conversion happens in exactly one place, so there is exactly one place to get it right.

### Time Zones Are Units Too

Times have a hidden unit of their own: the time zone.

```python
from datetime import datetime, timezone

# Local time of whatever machine runs this code
t_now = datetime.now()

# UTC, the same everywhere
t_now = datetime.now(timezone.utc)
```

The first version returns a "naive" datetime, which has no time zone attached. The same code run at the same moment on your laptop in Phoenix and on a server in Virginia gives two different answers, and neither one says which zone it is in. The second version states its time zone, so it means the same thing everywhere. A useful convention is to store and compute everything in UTC, and only convert to local time when showing it to a person.

### Pick a Shape Convention

Arrays have their own version of the units problem. Suppose we have a recording from several sensors, and a function that averages across them:

```python
def average_channels(signal):
    return signal.mean(axis=1)
```

This assumes the signal has shape `(n_time, n_channels)`, with time running down the first axis and channels across the second. If someone passes in an array with shape `(n_channels, n_time)` instead, NumPy doesn't complain. It averages over time instead of over channels and returns an array that has the wrong meaning and the wrong length.

The fix is to choose one shape convention for the whole project, write it down, and check it where you can:

```python
# Shape convention for this project: (n_time, n_channels)
N_CHANNELS = 64


def average_channels(signal):
    """Average a signal across its channels."""

    # Check that channels run along the second axis
    if signal.shape[1] != N_CHANNELS:
        raise ValueError(
            f"Expected shape (n_time, {N_CHANNELS}), got {signal.shape}"
        )

    # Average across channels
    return signal.mean(axis=1)
```

Now a transposed array produces a clear error instead of a quietly wrong answer, which is the principle of [Fail Fast, Fail Loud](/blog/2026/10/programming-principles-fail-fast-fail-loud/) at work.

The same problem appears with coordinates. GeoJSON, a common format for map data, stores points as `[longitude, latitude]`, while Google Maps and most people write `(latitude, longitude)`. Mix them up, and your points end up somewhere else entirely, often with no error at all. Storing coordinates with names, like `{"lat": 33.45, "lon": -112.07}`, removes the guesswork, for the same reason naming function arguments does.

## Say It in Comments and Docs

The third level to explicit coding covers everything we can't make obvious in the code itself. Some assumptions can't be expressed in a name or a check. When code depends on a rule like that, a comment or docstring should state it.

### Comment the Rules Your Code Relies On

In my post on [Optimize Last](/blog/2026/10/programming-principles-optimize-last/), I wrote a fast function that checks whether any appointments overlap. It sorts the appointments by start time and then only compares each appointment with the one right before it. That works because of a rule that is true but not obvious: once the appointments are sorted, if any two of them overlap, then some neighboring pair overlaps too.

Nothing in the code says that. Someone who doesn't know the rule might "fix" the function by removing the sort, which breaks it without any error. So the rule belongs in a comment:

```python
# Sort by start time. Once sorted, if any two appointments overlap,
# some neighboring pair overlaps too, so checking neighbors is enough.
appointments_sorted = sorted(
    appointments,
    key=lambda appointment: appointment.t_start,
)
```

The same goes for rules borrowed from libraries. NumPy's trigonometry functions expect radians, so `np.sin(90)` doesn't return `1`. A short comment like `# np.sin expects radians` next to a conversion tells the reader why the conversion is there.

### Put Units, Shapes, and Meanings in Docstrings

A docstring is where a function states its assumptions for anyone who calls it. For functions other people use, it should say what the code itself can't: the units, the expected shapes, and what special values like `None` mean.

Here is the `filter_signal` function from earlier with a docstring that does that:

```python
def filter_signal(signal, threshold=None):
    """Remove readings below a threshold.

    Args:
        signal:    1D array of voltage readings, in microvolts.
        threshold: Minimum reading to keep, in microvolts.
                   None keeps every reading. Zero is a valid threshold.

    Returns:
        signal:    The readings at or above the threshold.
    """
```

When things are clear, it still helps to say them. Comments that walk through what each block of code does make code easier to scan, and I use them all the time. But the comments that matter most are the ones that state an **assumption**. `# Loop over each appointment` saves the reader a few seconds. `# Assumes the appointments are sorted by start time` can save them an afternoon.

## Conclusion

Every program depends on assumptions. What matters is whether those assumptions are written down where the reader can see them, or kept in the author's head where they are guaranteed to be lost eventually.

Name your arguments, write the conditions you actually mean, and don't depend on where code is run. Put units in names, pick one convention for units and shapes, and convert at the edges. When a rule can't be made visible in the code itself, write it in a comment.

Hidden assumptions rarely cause crashes. They cause code that runs perfectly and means something different from what you thought. Put them on the page.

Thanks for reading!
