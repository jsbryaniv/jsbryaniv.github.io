---
date: 2025-8-11 12:00:01
layout: post
title: Who killed Pip?
subtitle: A Python murder mystery.
description: Last weekend I played detective in a crazy debugging mystery thriller with an unexpected twist! 
image: https://jsbryaniv.github.io/assets/img/blog/blog_who_killed_pip.png
optimized_image: https://jsbryaniv.github.io/assets/img/blog/blog_who_killed_pip.png
category: essay
tags:
  - funny
  - python
author: jsbryaniv
paginate: true
math: true
comments: true
---


## Chapter 1 — The Crime Scene

It was a quiet weekend in my project folder.

I had just created a fresh Python virtual environment — a private, self-contained folder that keeps all the packages a project needs in one place. I called it `.venv`.

Pip, the tool Python uses to install and manage packages, was alive and well. Everything worked… until I ran the most innocent of commands:

```bash
pip --version
```

But instead of a simple output, I was met with a chilling message:

```bash
ModuleNotFoundError: No module named 'pip'
```

Pip had been murdered!

Who would murder Pip? How could this happen? And why? I was on the case to solve this mystery.

## Chapter 2 — The First Suspect

The obvious culprit? The most recent package I had installed: `litellm`, a simple wrapper tool for language model APIs. It looked guilty — the environment often broke right after importing it.

To investigate if `litellm` was the killer, I created a new virtual environment without `litellm` and tried to see if the problem persisted. I tried using pip to install a popular math package, `numpy`. Surely, with the culprit behind bars, pip would be safe...

...But then it happened again!

A serial pip killer was still on the loose. `litellm` was not the murderer after all.

## Chapter 3 — Forensics

I began my investigation.

I checked the "interpreter paths" — the Python program my commands were using — to make sure they pointed to the `.venv` environment. They did.

I looked at the pip launcher script — the little file in `.venv/bin` that actually starts pip. Nothing unusual.

I checked Python’s own environment settings to see if the virtual environment had somehow been switched. Nope. It was still the right one.

Finally, I looked inside .venv and saw the evidence: the entire `.venv/lib` folder — where Python keeps all its packages — had been deleted!

The killer was clean. No fingerprints.

## Chapter 4 — The Breakthrough

The big clue came when I realized something chilling: pip would disappear even if I did nothing. I could walk away from my computer and come back to find the pip gone. How could pip disappear if I wasn't running any python commands? In order for something within python to kill pip, it would still need me to execute a script.

This meant the killer wasn’t inside Python at all. It was somewhere outside, lurking in the operating system.

## Chapter 5 — The Real Culprit

I did some digging. It was then that I realized that my project was located on my Desktop. On Mac, the Desktop is automatically synced to iCloud Drive — Apple’s cloud storage service. And evidently, iCloud was getting a little too aggressive with its optimizations. In order to optimize storage, iCloud would remove local copies of large or "inactive" files, leaving only a cloud placeholder.

To iCloud, `.venv/lib` looked like a giant, strange folder that could be safely offloaded. So, iCloud quietly deleted the local lib folder, leaving pip and my packages to vanish in the middle of my work.

The killer was iCloud!

## Chapter 6 — Protecting Pip

With the killer identified, I could strategize about how to protect pip from future murder attempts, building a sort of "witness protection program" for programs.

I identified three ways to protect pip:

1. Turn off iCloud storage optimization. This protects pip, but leaves the cloud drive vulnerable to storage issues.
2. Rename the virtual environment folder from `.venv` to `.venv.nosync`. The ".nosync" suffix tells iCloud to ignore the contents of the directory during cloud storage. This is safe, but cumbersome to work with.
3. Move the entire project folder off of my desktop and onto a non-synced location, such as `~/Code` or `~/Projects`. This is the safest long term fix, leaving python safe and iCloud storage optimized. And you can even keep a shortcut to the projects directory on my desktop, leaving your workflows intact as well.

I decided to go with option 3, moving all my projects off of the Desktop and into `~/Projects` From that moment on, pip lived in peace.

## Epilogue — Lessons for Future Detectives

If you keep your projects in Desktop or Documents and use iCloud sync:

Move them to a non-synced folder like `~/Code` or `~/Developer`.

Or add .nosync to the environment’s folder name.

Or turn off "Optimize Mac Storage" in iCloud settings.

Remember: In the wrong neighborhood, even the quietest Python environment can become another cold case.
