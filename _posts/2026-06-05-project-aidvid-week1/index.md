---
date: 2026-06-05 12:00:01
layout: post
title: "Project AIDVID: Week 1 - The Problem"
subtitle: Week 1 of the Project of the Month
description: Discussing the overall goal and motivation for Project AIDVID.
image: assets/coverart_aivid_w1.png
category: project
tags:
  - project
  - ai
  - coding
---

# Project of the Month: AIVID - AI Video Editing Tools

As I mentioned in my last post, I'm going to start regularly working on more projects and sharing the process along the way.

Rather than focusing on a single large project, each month I'll highlight a different project and document the journey from idea to product. At the end of the month I'll assign a verdict. Some projects will earn further investment and iteration, while others will be abandoned so I can move on to the next experiment.

The mantra here is: "From first principles to first customer and beyond!"

This month, the featured project is AI video editing.

## The Problem

The project started with what I thought would be a fairly straightforward request.

My wife was working with a client who needed some company videos edited. Specifically, the videos contained a few visual defects in the background that needed to be removed. In image editing, this type of task is commonly called inpainting: removing an unwanted object and having AI fill in the missing pixels.

I've spent a lot of time running AI models locally on my own hardware. Text generation, image generation, image editing, image segmentation, and other machine learning tasks are now routine. I have an RTX 4090 in my workstation and regularly run open-source models downloaded from Hugging Face.

So naturally, I assumed video editing would be straightforward.

Additionally, I've recently become interested in video production. One of my goals this year is to produce more video content for my website and social media. If I can build a local AI video editing toolkit, it would not only solve this client's problem but could become a useful foundation for future projects. I could potentially extend it with new features, automate parts of my workflow, and build tools tailored to my own needs.

Of course, commercial video editing tools already exist. I could simply pay for a subscription, do the inpainting, and move on. But before doing that, I wanted to answer a question:

Can a solo developer with a high-end consumer GPU build a practical AI video editing workflow using open-source tools?

Over the next few weeks I'll walk through what I built, the technical challenges I encountered, and whether the final result was actually worth the effort.

Going into the project, I expected the primary challenge to be software engineering.

I was wrong.