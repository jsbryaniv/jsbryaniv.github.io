---
date: YYYY-MM-DD 12:00:01
layout: post
title: "Programming Principles: Separation of Concerns"
subtitle: "Don't Mix Your Responsibilities"
description: "An essay on the programming principle of Separation of Concerns, and why it is important to follow it."
image: assets/coverart_programming_principles.png
category: programming-principles
tags:
  - programming
---

Here I discuss Programming Principles. Today I discuss the principle of Separation of Concerns.

## Introduction

Separation of Concerns is exactly what it sounds like: if you have different concerns or responsibilities in your code, they should be separated into different modules or components. For example, suppose I want to load data and then analyze it. Loading the data and analyzing the data are two different concerns, so they should be implemented as two different functions or classes. That's it! It's an extremely simple principle.

However, despite how simple Separation of Concerns is to understand, I frequently run into code that mixes concerns together. As I'll explain below, this often becomes a nightmare to work with. If I could get developers to consistently follow one programming principle, it would be Separation of Concerns. So thank you for reading this essay, and please pay attention, because it is extremely easy and tempting to write code that violates this principle!

## Why is Separation of Concerns Important?

The main reason for Separation of Concerns is scalability and maintainability.

Frequently, you will want to reuse somebody else's code for a different use case than the one it was originally written for. If the code mixes concerns together, it can be surprisingly difficult to do so. If instead the code is modular, and each component has a single responsibility, it becomes much easier to pick out the pieces you need and combine them in different ways.

One of the most common examples of code that violates Separation of Concerns is code that mixes data loading and data analysis together. It's really easy and very tempting for junior developers and academics to write one function that both loads a dataset and analyzes it. I used to do this all the time! The thought process is usually something like, "I'm only working with one dataset, so I might as well make one function that does everything. Fewer functions means less code, right?"

Wrong!

The problem appears the first time somebody wants to analyze a different dataset that is stored in a different format. Instead of simply reusing the analysis, they now have to open your function, understand how it works, and rewrite the data loading portion before they can even begin. This is frustrating and time consuming because they are forced to modify code that has nothing to do with the analysis itself. If loading and analyzing had been separated into different functions, then the next developer could simply import the analysis function and write a new data loading function for their dataset. They never have to touch the analysis code at all.

## How to Implement Separation of Concerns

The first step is recognizing what constitutes a "concern." There isn't a strict definition, and it takes experience to recognize them, but a good rule of thumb is to ask yourself:

> Could this piece of code reasonably be reused in a different context?

If the answer is yes, then it is probably a concern that should be separated into its own function or class. Once you identify the concerns, separating them is straightforward: split your code into smaller functions.

Notice that this does **not** mean you can't have a top-level function that runs everything. In fact, that's often desirable. The difference is that the top-level function should coordinate the workflow, while the individual functions perform the actual work.

Here is an example of a function that violates Separation of Concerns:

```python
def nonmodular_pipeline(data_path, save_path):
    # Load the data
    with open(data_path, "r") as f:
        data = float(f.read())

    # Analyze the data
    result = 10 * data + 5

    # Save the result
    with open(save_path, "w") as f:
        f.write(str(result))
```

This function loads the data, analyzes it, and saves the result all in one place.

Now compare it with a modular version:

```python
def load_data(file_path):
    with open(file_path, "r") as f:
        return float(f.read())


def analyze_data(data):
    return 10 * data + 5


def save_result(result, save_path):
    with open(save_path, "w") as f:
        f.write(str(result))


def modular_pipeline(data_path, save_path):
    data = load_data(data_path)
    result = analyze_data(data)
    save_result(result, save_path)
```

These two pipelines do exactly the same thing. They both load a number from a file, apply the same analysis, and save the result.

The modular version contains more functions, so at first glance the nonmodular version may look simpler. As long as this is the only workflow we ever need, the difference may not seem important.

But then the requirements change.

Uh oh! The boss wants us to incorporate our analysis into a much larger pipeline. The input data now comes from a different file format, and we also need to run a postprocessing step before saving the final result.

How do we handle this?

With the nonmodular code, we cannot reuse the analysis by itself. The analysis is trapped inside a function that insists on loading its own input and saving its own output.

One possible workaround would look something like this:

```python
from project.nonmodular_pipeline import nonmodular_pipeline  # <-- The funciton we want to reuse
from project.otherstuff import load_new_format, preprocess_data, postprocess_result


raw_data = load_new_format("new_data.json")
processed_data = preprocess_data(raw_data)

# The existing pipeline only accepts a file path, so we must save the
# intermediate data before we can use it.
with open("temporary_input.txt", "w") as f:
    f.write(str(processed_data))

# This also saves its result to a file instead of returning it.
nonmodular_pipeline(
    data_path="temporary_input.txt",
    save_path="temporary_output.txt",
)

# Load the result back into memory so the pipeline can continue.
with open("temporary_output.txt", "r") as f:
    result = float(f.read())

final_result = postprocess_result(result)
```

This works, but only by adding unnecessary temporary files and extra input/output operations. Our larger pipeline has to reshape itself around the limitations of the original function.

We could instead open `nonmodular_pipeline()`, rewrite it to support the new use case, or copy the analysis logic into our new script. However, all of these options require us to dissect and modify code that should not need to change.

Now consider the modular version:

```python
from project.analysis import analyze_data  # <-- The function we want to reuse
from project.otherstuff import load_new_format, preprocess_data, postprocess_result


raw_data = load_new_format("new_data.json")
processed_data = preprocess_data(raw_data)
result = analyze_data(processed_data)  # One line of code!
final_result = postprocess_result(result)

save_final_result(final_result, "final_result.json")
```

Because the original concerns were separated, we can import exactly the function we need and use it inside the new pipeline. We do not need the original loading function because our data comes from somewhere else, and we do not need the original saving function because the result must first pass through postprocessing.

The modular design clearly makes this derivative code shorter and easier to write. However, the more important benefit is that future developers do not need to dissect your code to figure out how to incorporate it into a larger system. They can simply import the function they need and use it as they would any other function.

That is the real power of Separation of Concerns. It allows each part of your code to stand on its own, making the entire codebase easier to reuse, extend, and maintain.

## Conclusion

Separation of Concerns is one of the simplest programming principles, but it is also one of the most valuable. Whenever you write code, try to identify the different responsibilities your program performs. If two pieces of functionality can reasonably be used independently, they should probably live in different functions, classes, or modules. Doing this will make your code easier to understand, easier to test, easier to extend, and much easier for other developers—including your future self—to reuse!

Thanks for reading, and I hope you found this essay useful!