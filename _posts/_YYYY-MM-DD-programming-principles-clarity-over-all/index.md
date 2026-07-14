---
date: YYYY-MM-DD 12:00:01
layout: post
title: "Programming Principles: Clarity Over All"
subtitle: 
description: 
image: assets/coverart_clarity_over_all.png
category: programming-principles
tags:
  - programming
---

Here I discuss Programming Principles. Today I discuss the principle of Clarity Over All.

## Introduction

For every program that a person might want to write, there are an infinite number of ways to write it. So which way is the best? It depends on context: if you are prototyping something then you might prioritize speed of development, if you are writing a high performance library then you might prioritize performance, if you are writing a program in the early days of computing when memory was limited then you might prioritize shorter code. But in general, the best way to write a program is to write it in a way that makes it easy to understand.

"Clarity Over All" is a principle that states that when writing code, clarity should be prioritized over all other considerations. This means that code should be written in a way that is easy to read and understand, even if it means sacrificing performance or brevity.

## Why Clarity Matters

> Code is read more often than it is written. - Guido van Rossum (Creator of Python)

First, if you write a program that actually does something useful, then it will be read by other people. When these other people read it, they will want to understand what it does and how it works. Our job is to make it as easy as possible for them to do that.

Second, if you write a program that people actually use for a long time, then you and others will have to maintain it. It doesnt matter how well you know the codebase when you write it, at sometime down the line you will have to come back to it to make changes. If you write code that is hard to understand, then it will be hard to maintain. If you write code that is easy to understand, then it will be easy to maintain.

The bottom line is that if you plan to write useful code, then you need to make it easy to understand. I'm not talking about one off scripts that you write and execute one time, for those you can write it however you want. But for anything that you actually want to make an impact with, you need to write it in a way that is easy to understand.

Write Code for Humans to Read.


## How to Write Clear Code

I will break this guideline into 5 categories: Comments, Docs & Docstrings, Naming Conventions, Explicit Code, and File Organization. Each of these categories has its own set of guidelines that can help you write clear code.

### Comments

- Dont buy into the idea that "the code explains itself". That misses the point. If I need to quickly understand what a code does then I want to be able to read a summary, not spend minutes going through line by line to see what the thing does. Comments are a way to provide that summary. All code should have comments placed throughout the codebase that explain what is going on.

- Some tips for good comments:
  - Focus on explaining "why" rather than "what". The general purpose is the important part, and if I need the details, then I can read the code.
  - Separate code into blocks and provide a comment at the top of each block that explains what the block does.

- The end goal is to make programs that can be easily understood by just looking at the comments.

### Docs & Docstrings

- For larger projects you should aim to have some sort of documentation.
- AI programming assistants can instantly write docs for you so there is really no excuse anymore.
- Docs should be a separate file, typically written in markdown, that explains high level how to use the program and what it does.
- Use example code to show how to use the program, explaining the inputs and the outputs.
- Again the important part is to explain "why" rather than "what"/"how".
- Good docs are concise and precise, they tell you everything you need to know but nothing more.

- Next, **docstrings** are extremely useful!
- I get the feeling that most programmers don't even know what a docstring is, so let me exalain:
- A docstring is a type of comment that is placed a the top of a function, class, or module that explains what it does, but unlike a regular comment, docstrings are accessible to your IDE (integrated development environment) and let you quickly see what a function, class, or module does without having to read through the code.
- Look below at an example of how you can create docstrings in python then see the docstring in vscode

![Docstring Example](assets/docstring_example.png)

This is extremely useful because you can access information about a function without having to read through the code. I showed an example in python, but many other programming languages have similar features.


### Naming Conventions

- Use descriptive names for variables.
- Avoid abbreviations unless they are well known.
- Try to stick to case conventions for the programming language you are using. For example, in python, use `snake_case` for variables and functions, and `CamelCase` for classes.

- I personally like to name objects with the base name of the object first, then followed by the description, that way similar objects are grouped together. I name objects sort of exactly the reverse of how you would say it verbally, so a big dog would be `dog_big` and a small dog would be `dog_small`. This is just my personal preference, but it is important to have a consistent naming convention throughout your codebase.

### Explicit Code

- Python makes it really easy to pack a lot of code into a single line, but just because you can doesnt mean you should.
- In general, it is easier to write code if it is straightforward and explicit, rather than clever and implicit.
- This means you should break up your code into small logical chunks.

- As an example, consider the following two code snippets:

```python
# Clever and implicit
def can_purchase_item(price, discount, tax_rate, credit_limit):
    if price * (1 - discount) * tax_rate > credit_limit:
        return False
    else:
        return True
```

```python
# Straightforward and explicit
def can_purchase_item(price, discount, tax_rate, credit_limit):
    discounted_price = price * (1 - discount)
    total_price = discounted_price * tax_rate
    if total_price > credit_limit:
        return False
    else:
        return True
```

- Even without comments, its probably much easier to understand the second snippet than the first because it breaks the code down into smaller logical chunks.
- Theoretically it adds a small amount of overhead to write explicit code, but in practice the overhead is negligible compared to the time savings of being able to understand the code quickly and easily.


### File Organization

- Organize your files in a way that makes sense for your project.
- Every programming language has its own conventions for how to organize files, the important part is to be consistent and follow the conventions of the language you are using.

- Some common conventions are:
  - Use `utils` or `helpers` for utility functions that are used throughout the codebase.
  - Use `tests` for unit tests.
  - Use `docs` for documentation.
  - Use `src` for source code (code that core to the program).
  - Use `scripts` for scripts that are used to run the program or perform tasks related to the program.
  - Use `assets` for images, videos, and other media files.

## Conclusion

- By now I hope i have convinced you that clarity is imporant.
- I have provided you some guidelines for how to write clear code.
- I hope that by following these guidelines you will be able to save yourself an enormous amount of time and effort in the future by making your code easy to understand and maintain.
- I wish I could send this back in time to myself 10 years ago, because man, I am still trying to figure out what some of my programs do!
