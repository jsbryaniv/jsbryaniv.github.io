---
date: 2026-06-26 12:00:01
layout: post
title: "Project AIVID: Week 4 - The Verdict"
subtitle: Week 4 of the Project of the Month
description: Reflecting on Project AIVID and deciding whether it is worth continuing.
image: assets/coverart_aivid_w4.png
category: project
tags:
  - project
  - ai
  - coding
---

This month my Project of the Month was AIVID, a local AI video editing framework. In week 1, [The Problem](https://shep4.com/blog/2026/06/project-aidvid-week1/) I introduced the project, in week 2, [The Build](https://shep4.com/blog/2026/06/project-aidvid-week2/), I discussed the engineering challenges involved in the software, in week 3, [The Product](https://shep4.com/blog/2026/06/project-aidvid-week3/) I introduced the finished software framework and discussed the performance of local AI video generation. This week, in week 4, I'll wrap everything up and answer the original question: was this project actually worth pursuing? 


## The Verdict

While I was ultimately able to edit a video for a client using my local AI video framework, the end product is not practical for anything other than a proof-of-concept. The verdict is **abandon**.

![Abandon Verdict](assets/abandon_verdict.png)

The main issue is that the computational requirements for local AI video generation are too high. Even on my 4090 I was only able to generate a few seconds of video at a time, and the process was slow and resource intensive. While I was able to complete the client's project, it required substantial engineering effort and compute resources to achieve results that could often be obtained more easily using existing commercial tools. As of now, it does not appear that the advantages of local AI video generation outweigh the costs, so it does not make sense to continue pursuing this project.


## Reflections

While Project AIVID was ultimately a failure, I think it was a great experience. Along the way I learned a tremendous amount about AI video generation, Hugging Face, video codecs, GPU memory management, and the current state of the open-source video ecosystem. Just as importantly, the project forced me to become re-acquainted with traditional video editing software. I came away with a newfound respect for the existing commercial tools and plan to use them over the coming months as I begin producing video content for my website and social media.

Perhaps the biggest success to come out of this month wasn’t Project AIVID itself, but the Project of the Month format. Building in public forced me to make steady progress and package my work into something I could share every week. Limiting each project to a single month also encourages a "fail fast" mentality. Rather than spending years pursuing an idea that may never become practical, I can quickly evaluate it, learn from it, and move on to the next experiment. I enjoyed this format far more than I expected, and I plan to continue it indefinitely.

Stay tuned for next month’s project!