---
layout: post
title: "Programming Principles: Optimize Last"
subtitle: "Make It Clear Before You Make It Fast"
description: A discussion of why you should write clear, correct code first and only optimize it when performance becomes a real problem.
image: assets/coverart_programming_principles.png
category: programming-principles
tags:
  - programming
---

Here I discuss Programming Principles. Today I discuss the principle of Optimize Last.

## Introduction

Programmers love making code faster. There is something deeply satisfying about replacing a slow algorithm with a fast one, eliminating unnecessary work, or watching a benchmark improve. The problem is that faster code is often harder to understand. An optimization that saves the computer a little work can create a lot more work for the next person who has to read it. This is why I believe in putting [Clarity Over All](/blog/2026/07/programming-principles-clarity-over-all/): readability should be the default, and any code that sacrifices it should have a good reason for doing so.

The principle of Optimize Last says that you should begin with the clearest correct solution to a problem. Then, if the program is not fast enough, measure its performance, find the actual bottleneck, and optimize that specific part.

This does **not** mean performance is unimportant. Sometimes performance is a requirement, and sometimes an optimized implementation is dramatically better. It means that additional complexity should have to justify itself. If you cannot demonstrate that the clear version is too slow, then making it harder to understand is probably not an improvement.

## Why Is Optimizing Early a Problem?

The biggest problem with optimizing early is that optimized code can become unreadable very quickly.

A straightforward implementation usually mirrors the problem it solves. It uses descriptive variables, explicit steps, and familiar control flow. An optimized implementation may instead rely on a less obvious algorithm, combine several steps, store additional state, or take advantage of assumptions that are not immediately visible. Each of these decisions makes the code a little harder to understand and a little easier to break.

That tradeoff can be worthwhile when performance matters. However, before measuring the program, you do not know whether it matters. The code that looks inefficient may already be more than fast enough. It may also account for only a tiny fraction of the program's runtime, while the real bottleneck is somewhere completely different.

Optimizing early therefore risks paying a definite cost in readability for a performance benefit that users may never notice.

## A Simple Example

Suppose we are writing a scheduling application and need to determine whether any appointments overlap. The most direct solution is to compare every appointment with every appointment that comes after it:

```python
def has_overlapping_appointments(appointments):
    """Check whether any appointments overlap."""

    # Loop over each appointment
    for index, appointment_1 in enumerate(appointments):

        # Loop over each appointment that comes after it
        for appointment_2 in appointments[index + 1:]:

            # Get the start and end times of both appointments
            start_1 = appointment_1.t_start
            end_1 = appointment_1.t_end
            start_2 = appointment_2.t_start
            end_2 = appointment_2.t_end

            # Check if appointment_2 starts before appointment_1 ends
            if start_2 < end_1:
                # Check if appointment_1 starts before appointment_2 ends
                if start_1 < end_2:
                    # appointment_1 and appointment_2 overlap
                    return True

    # If we reach this point, no appointments overlap
    return False
```

This implementation is easy to follow. For each appointment, it checks every appointment that comes after it and returns `True` if it finds a conflict. The code closely matches how we might explain the solution in plain English.

However, it is not very efficient. As the number of appointments grows, the number of comparisons grows much faster. With enough appointments, the double loop could become a real performance problem.

We can optimize the function by first sorting the appointments by their start time. Once they are sorted, we only need to move through the list once and compare each appointment with the one immediately before it:

```python
def has_overlapping_appointments(appointments):
    """Check whether any appointments overlap."""

    # Fewer than two appointments cannot overlap
    if len(appointments) < 2:
        return False

    # Sort the appointments by their start times
    appointments_sorted = sorted(
        appointments,
        key=lambda appointment: appointment.t_start,
    )

    # Start with the first appointment
    appointment_previous = appointments_sorted[0]

    # Loop over each remaining appointment
    for appointment_current in appointments_sorted[1:]:

        # Get the relevant times of the two appointments
        start_current = appointment_current.t_start
        end_previous = appointment_previous.t_end

        # Check if the current appointment starts before the previous one ends
        if start_current < end_previous:
            # The appointments overlap
            return True

        # Move to the next pair of appointments
        appointment_previous = appointment_current

    # If we reach this point, no appointments overlap
    return False
```

This version is significantly faster for large inputs. Instead of comparing every possible pair, it sorts the appointments and then makes one pass through them.

It also requires more thought to understand. The reader has to recognize why sorting makes the scan possible and why checking neighboring appointments is enough to detect every overlap. The double loop requires almost none of that explanation.

So which version should we use?

If the application only handles ten appointments at a time, I would use the double loop. Its performance will be perfectly adequate, and its behavior is immediately obvious. If the application must process hundreds of thousands of appointments and measurements show that this function is a bottleneck, then the optimized version has earned its additional complexity.

The important point is that we should not make that decision based only on the sight of a double loop. Code that looks inefficient is not necessarily code that causes a meaningful performance problem.

## How to Optimize Responsibly

Start by writing the clearest implementation that you know is correct. A clear implementation is easier to test, and it can serve as a guide when you later write a more complicated version.

Next, decide what "fast enough" actually means. A script that runs once a month may be fine taking several minutes. An operation that runs every time someone clicks a button may need to finish almost immediately. Without a concrete requirement, there is no way to know whether an optimization is necessary.

Then measure the program using realistic inputs. If it is too slow, profile it to find where the time is actually being spent. When your program follows [Separation of Concerns](/blog/2026/07/programming-principles-separation-of-concerns/), you can optimize the slow component without rewriting unrelated parts of the program. Confirm that the new version is measurably faster, and use tests to make sure it still produces the same results.

Finally, stop when the program meets its performance requirements. A function does not need to be as fast as theoretically possible. It only needs to be fast enough for its real use case.

## Optimize Last in the Age of AI

One last thought: AI coding agents make it extremely easy to generate optimized code from the start and explain anything you do not understand. Even so, an agent cannot know whether an optimization is worthwhile until the project's real requirements are clear.

The same principle also applies at a higher level. It is often better to begin with a simple scratch file than to immediately build a complete Python package. A local CSV may be enough before the project needs a database. Just because an agent can build a complicated architecture in seconds does not mean the project needs one yet.

Maybe I am old school, but I still like to understand my codebases. If I need to work in the nitty-gritty details, I will sometimes ask my coding agents to simplify an implementation even if that makes it less optimal. For a disposable vibe-coded project, I may not care. But otherwise, I would rather understand the code than blindly trust the agent. I resonate with Han Solo on this: I don't trust the droids.

## Conclusion

Optimization is a tradeoff. Faster code is valuable, but readable code is valuable too. We should not give up readability merely because we can imagine a more efficient implementation.

Write the clear version first. Test it, run it with realistic data, and measure its performance. If it is fast enough, keep it. If it is not, use those measurements to guide the optimization.

Make your code fast when it needs to be fast. Until then, make it easy to understand.
