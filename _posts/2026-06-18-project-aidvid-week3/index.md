---
date: 2026-06-18 12:00:01
layout: post
title: "Project AIDVID: Week 3 - The Product"
subtitle: Week 3 of the Project of the Month
description: Building a local AI video editing framework using open-source models, week 3.
image: assets/coverart_aivid_w3.png
category: project
tags:
  - project
  - ai
  - coding
---

Last week I discussed the engineering challenges involved in building a local AI video editing framework. If you missed it, you can read the previous update here: [Project AIDVID: Week 2 - The Build](https://shep4.com/blog/2026/06/project-aidvid-week2/)

This week I'll discuss the resulting software and whether it was capable of solving the original problem.

## The Product

After solving the API and memory management challenges, I packaged everything into a reusable Python project:

[AIVideoSandbox](https://github.com/jsbryaniv/AIVideoSandbox)

The project is structured like a traditional Python package and includes example scripts demonstrating common video editing workflows. My goal was not simply to edit a single video, but to build a foundation that could support future AI video editing projects as well.

At a high level, the framework allows me to load videos, manipulate them programmatically, perform AI-powered editing operations, and save the results back to disk. From a software engineering perspective, I was quite happy with the result.

## Performance

Unfortunately, software architecture was not the primary bottleneck.

Despite all of the memory optimizations discussed last week, the underlying video generation process remained extremely resource intensive. Even with an RTX 4090, generation times were slow and practical limits on video length and resolution were much lower than I originally expected.

The good news is that the framework worked. I was ultimately able to complete the client's project and successfully remove the defects from the video.

The bad news is that solving a problem once and solving it repeatedly are very different things. While the workflow was technically successful, it required substantial compute resources and engineering effort to achieve results that could often be obtained more easily using existing commercial tools.

## Current Status

At this point I had answered the original technical question and completed the work I was hired to do.

However, the question was no longer whether local AI video editing was possible.

The question had become whether it was practical.

Next week I'll share my final verdict on Project AIDVID and discuss whether this is a project worth continuing.
