---
date: 2026-10-13 12:00:01
layout: post
title: "Project One Video: How I Made My First Video"
subtitle: The conclusion of the Project of the Month for September
description: How I filmed and edited my first YouTube video without ever opening a video editor.
image: assets/coverart_onevideo_final.png
category: project
tags:
  - project
  - youtube
  - video-production
  - AI
---

Last month's [project of the month](/blog/2026/09/project-one-video-w1/) was to make and publish my first YouTube video, and I'm happy to say I finished it! Check it out below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/cw7BeaIxu9c" title="How to Build an AI Trainer That Writes Your Workouts" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this blog post I'm going to discuss how I made it.

The video teaches you how to build an AI agent that writes your workouts for you, and it is deliberately written for people who do not code. This post is the opposite. It's for the people who want to know how the video itself got made, because the method turned out to be far more interesting than I expected.

Here is the short version: the hard part was physical. The editing, which is the part I had dreaded for years, turned out to be nearly free.

## Hardware Is the Hard Part

Every cliché about filming yourself is true. The camera lies in exactly one direction, and it is not the flattering one. Any blemish you would walk past in a mirror becomes the main character on screen.

My original plan was to record myself talking straight into my Mac. The quality was atrocious. Not "needs a little color correction" atrocious — unusable. Bad lighting, bad angle, bad everything.

Luckily, my wife has accumulated some minimal filming equipment over the years for her business, so I raided her setup. What I ended up with:

- A cheap Amazon green screen as a backdrop
- A ring light
- A phone stand built into the ring light
- A teleprompter app ([PromptSmart Pro](https://my.promptsmart.com/))

That teleprompter app was the single biggest lifesaver of the whole project. I recorded on my phone's **front** camera specifically so I could read the script while filming, which meant I could get through long stretches of narration without memorizing anything or losing my place.

Roughly $100 of equipment did more for the final quality of this video than every piece of software I used combined. If you are thinking about making videos and wondering where to start spending, start there.

### The Mistake I Made

The ring light has a phone holder mounted dead center, which seems convenient and is in fact a trap. Shooting through the middle of a ring light puts two perfect glowing circles in your pupils. It made me look like a possessed demon.

I am told the only real fix is to have the light come from a different angle than the camera. Which raises an obvious question: why is there a phone holder in the middle of the ring light?

Anyway, for this first video I found a workaround: I just squinted the whole video. It looks a little ridiculous, but I would rather look like I am concentrating than look like I have demon eyes. Next time I am going to buy a separate phone stand and put the light off to one side.

### Record Loose and Fix It Later

One more thing about filming, and it matters for the next section. I did not record in careful little pieces. I read the entire script start to finish off the teleprompter in one pass, and whenever a line came out wrong I just said it again and again until it sounded right.

The useful observation is that **you always end on a good take.** Whatever the last version of a line is, that is the one you want.

It made filming easier, but the whole time I did it, I was thinking, "This is going to be a nightmare to edit." Thank God I was wrong...

## Editing Is Easy Now, With the Right Tools

Every time I have worked on a video project in the past, editing is the part I dreaded. Scrub through footage, find the moment where you stopped fumbling, cut it, stitch it to the next piece, add a transition, discover the audio is now out of sync, start over. It is tedious work and I am bad at it.

But evidently the editing landscape has drastically improved!

I made this entire video without opening a conventional video editor once. Instead I chained together five steps.

### 1. Speech to text, with word-level timestamps

First, I ran the raw footage through [whisper.cpp](https://github.com/ggerganov/whisper.cpp) running locally on my Mac, using the `large-v3-turbo` model. No uploads, no API bill, no rate limits. The output is a transcript where every word carries a timestamp.

One gotcha if you try this: Whisper's default word timings are not accurate enough to cut video on. You need the `-dtw` flag with `-nfa` to get timings you can actually trust.

### 2. Automatic take selection

Next is the step that genuinely surprised me. I had Claude do the clipping. And it worked amazingly well!

To clarify, I did not ask Claude to read my transcript and pick the good takes. I asked Claude to write me a python script that does it, and that distinction is the whole lesson. An AI reading a transcript is a one-off favor. A hundred lines of Python that I own, understand, and can run again on the next video is infrastructure.

The logic it landed on is simple. Split the transcript into spoken phrases. When a phrase repeats something that was already said, that is a retake, so throw away everything from the earlier version onward. Keep going to the end. What survives is the last clean run of every line.

Worth noting what did *not* work, because it was my first instinct and it was wrong. The obvious approach is to fuzzy-match the written script against the transcript to find each section. This turned out to be far too brittle, because I reword things constantly while filming. Half of what I actually said matched nothing in the script I had written. Comparing the transcript against *itself* to find repeats sidesteps that completely.

The script writes a review report before it cuts anything, so I read what it plans to keep and drop, approve it, and then ffmpeg slices out one clip per section. I never opened a clipping tool. Compared to every previous attempt I have made at this, it is honestly mind-bogglingly simple.

### 3. Removing the background

After that I removed the green screen background.

My first attempt here was ordinary color keying, and it failed badly. ffmpeg's `chromakey` filter ate my navy shirt and chunks of my hair along with the background, and `hsvkey` left halos everywhere there was a shadow. The reason is that my green screen is cheap, wrinkled, and unevenly lit, which is exactly what color-based keying cannot handle.

So I switched to AI segmentation instead, using [RobustVideoMatting](https://github.com/PeterL1n/RobustVideoMatting). It identifies the person rather than the color, so it does not care about wrinkles, shadows, or uneven lighting at all. It worked on the first try.

It was computationally expensive, though. Matting ran at roughly two to three frames per second on my M1, which worked out to about 95 minutes to process all nine clips. I also processed at full resolution, which was a waste, because my face ends up inside a small circle in the corner of the frame.

**The takeaway: do not spend money on a nice green screen. Spend it on light.** Segmentation has made backdrop quality almost irrelevant. This is also becoming a common consensus on Reddit. The top advice I see for YouTube creators is to put your budget into lighting first.

### 4. Assembling the video in code

To actually put the video together I used [Remotion](https://www.remotion.dev/), a code-first video editor. You build videos the same way you build a web app, by writing components. A scene is a file. A transition is a function. The whole video is a project you can read, diff, and version control.

This matters more than it sounds, because Remotion is built on Node, and Node is a stack AI agents are extremely good at. I described what I wanted and Claude built it, and the speed was remarkable. It handled things I would not have attempted by hand, like masking my face into a floating bubble in the corner and cross-fading between every section.

From the point where my clips were cut and keyed to a watchable first draft was a couple of hours. From there I iterated in small adjustments: move the bubble, lengthen the pauses, tweak the on-screen text, crop the menu bar out of the screen recordings. Each change was a few characters in a file rather than an afternoon of dragging things around a timeline.

### 5. Recording the screen captures last

The final step was the screen recordings of my phone and my computer. I saved these for the very end, after the rest of the video was already assembled and rendered with a placeholder sitting in every spot a recording belonged.

Doing it in that order meant I could record against my own narration. I played the rendered video back and used [OBS](https://obsproject.com/) to capture my screen and my computer's audio at the same time, so the take contained my voiceover right alongside the footage.

That let me work the same way I did when filming: one continuous take, start to finish, redoing anything I fumbled. And because the narration was baked into the recording, I could run it straight back through the same transcript cutting script from step two. It found where each section's narration appeared and sliced out that stretch automatically. Five of my six screen recordings came out of a single pass.

**The takeaway: record your screen captures last, not first.** Syncing a screen recording to narration is the most tedious part of making a tutorial video, and recording in this order makes the problem disappear entirely. You are performing to the real timing instead of guessing at it, so by the time the recording exists it is already in sync.

## For My Purposes, Video Editing Is Solved

I am extremely excited about the workflow I discovered here. I mentioned in my initial Project One Video post that the goal wasnt just to make a single video, but to make a sustainable framework for making videos. I think that I can confidently say that this is a solved problem now.

If you want to make your own videos, whether for YouTube, recorded lectures, or course material, I would recommend this setup without hesitation. Buy a ring light and put it off to one side. Write a script and read it off a teleprompter in one pass. Let software find your good takes, let segmentation handle your background, assemble the whole thing in code, and record your screen captures last.

For more tools and ideas like this, you can also [subscribe to my newsletter](/newsletter/).
