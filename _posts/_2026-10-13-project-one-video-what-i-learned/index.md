---
date: 2026-10-13 12:00:01
layout: post
title: "TODO — e.g. What I Learned Making My First YouTube Video"
subtitle: TODO
description: TODO
image: assets/coverart.png
category: project
tags:
  - project
  - youtube
  - video-production
  - AI
---

<!-- ============================================================
     OUTLINE v2 — from Shep's dictated structure, reorganized.
     Not prose. Raw material: scratchpad/post-raw-material.md
     Video: https://youtu.be/cw7BeaIxu9c (temp link, swap after publish)

     AUDIENCE: programmers. The video is for a no-code audience; this
     post is for people who build things. That split is the site's
     theme — products for regular people, writing for technical people.
     Say it once in the intro so nobody is confused, then move on.

     THROUGHLINE: the money went into hardware, not software. The
     hard part was physical. The editing — the part everyone dreads —
     turned out to be the easy part, because it's now just tools in
     a chain.
     ============================================================ -->


<!-- ============ 1. INTRO ============
     - This closes out Project One Video.
     - The video is live. Embed it.
     - One line on what it teaches (AI trainer that writes your
       workouts, no code required).
     - The turn: that video is for everyone. This post is for the
       people who want to know how it was made.
     - What you'll take away: the whole stack, and the two places
       I wasted time so you don't have to.
     Keep this short. Four or five sentences.
-->

## TODO


<!-- ============ 2. HARDWARE IS THE HARD PART ============
     Thesis: every cliché about filming yourself is true, and the
     bottleneck was physical, not technical.

     - The camera lies in one direction only: any blemish you'd
       ignore in real life is pronounced on video.
     - First plan: just record on the Mac. Quality was atrocious.
     - Wife has minimal filming equipment from her business. Final kit:
         * ring light
         * cheap Amazon green screen
         * phone stand built into the ring light
         * teleprompter app  <- lifesaver, call this out
     - Recorded on the phone FRONT camera, specifically so the
       teleprompter was readable while filming.
     - ~$100 of equipment did more for final quality than anything
       in software. That's the section's one-line takeaway.

     THE PITFALL (keep the humor, it's the best bit in the post):
     - Ring light with the phone holder mounted in its centre puts
       perfect rings in your eyes. Demon eyes.
     - Told the only fix is to have the light come from a different
       angle than the camera.
     - The joke that lands: so why is there a phone holder in the
       middle of the ring light?
     - This video's workaround: squint. Hard. The whole time. Looks
       ridiculous; still better than demon eyes.
     - Moving forward: separate stand for the phone, light offset.

     ADD — this is the bridge to section 3, don't skip it:
     - Filming method was one unbroken pass through the whole script,
       off the teleprompter, redoing lines whenever they came out wrong.
     - Key observation: you always end on a good take.
     - That's only a sane way to record because take selection is
       automated downstream. Recording loose and fixing it in software
       is a deliberate trade, not laziness. -> leads into section 3.
-->

## TODO


<!-- ============ 3. EDITING WITH THE RIGHT TOOLS ============
     Thesis: editing used to be the part I dreaded. In 2026 I made a
     whole video without opening a conventional video editor.

     Open with the old pain for contrast: scrubbing footage, finding
     the right clip, stitching, transitions. Tedious. Dreaded it.

     Then the chain, four links:

     1. SPEECH-TO-TEXT WITH WORD TIMESTAMPS
        - whisper.cpp, large-v3-turbo, running locally. No upload,
          no API bill.
        - Gotcha worth one line: default word timings are unusable,
          needs -dtw with -nfa.

     2. AUTOMATIC TAKE SELECTION  <- be accurate here, see note
        - Claude didn't read the transcript. Claude wrote a script
          that does it deterministically, and I own it and can rerun
          it on the next video. That's the real lesson.
        - How it works: split the transcript into spoken phrases;
          when a phrase repeats something already said, that's a
          retake; drop everything from the earlier version onward.
        - First design was to fuzzy-match the SCRIPT against the
          transcript. Too brittle — I reword constantly while
          recording, so half the spoken lines matched nothing.
          Worth including: it's the one place the obvious approach
          was wrong.
        - It writes a review report before cutting anything. Human
          approves, then ffmpeg cuts one clip per section.
        - Never opened a clipping tool. This is the "mind-boggling
          compared to past attempts" beat.

     3. GETTING RID OF THE BACKGROUND
        - Tried color keying first. It failed: ffmpeg chromakey ate
          the navy shirt and the hair; hsvkey left shadow halos.
          Because the green screen is cheap, wrinkled, unevenly lit.
        - Switched to AI segmentation/matting (RobustVideoMatting).
          Doesn't care about the screen's quality at all.
        - THE TAKEAWAY, and it's a good one: don't spend money on a
          nice green screen. Spend it on light. Segmentation makes
          the screen's quality nearly irrelevant.
        - Honest cost: slow. ~1.7-3 frames/sec on an M1, 95 minutes
          for nine clips. And full resolution was overkill given the
          footage ends up in a small circle.

     4. ASSEMBLY IN CODE — REMOTION
        - Remotion = build video from code, like coding an app.
        - Node-based, which matters: it's a stack AI agents are
          genuinely good at.
        - Asked Claude to assemble it; speed was remarkable.
        - Got real effects out of it: face in a bubble in the corner,
          cross-fades between sections.
        - First draft in a couple of hours.  <- consider specifying
          which stage, since keying alone was 95 min
        - Then iterate in small adjustments to the final video.
-->

## TODO


<!-- ============ 4. THE TRICK I'D TELL ANYONE ============
     (New section — recommend including. Strongest reusable tip in
     the project and it's currently missing from the outline.)

     Problem it solves: syncing screen recordings to narration is the
     most tedious part of a tutorial video.

     The move: don't record your screen first. Record it LAST, against
     the finished video.
     - Render the video with placeholders where the screen captures go.
     - Each placeholder displays the exact filename to save as, the
       script's directions for that section, and a running clock to
       record against.
     - Then play the rendered video while screen-recording with the
       computer's audio (OBS), so the recording contains the narration.
     - sync_screen.py finds where each section's narration appears in
       the take and cuts that stretch out automatically.
     - Five of six recordings came out of a single take.

     Why it works: you're performing to the real timing instead of
     guessing at it, so there's nothing left to sync.

     Could be folded into section 3 as link 5, but it's strong enough
     to stand alone and it's the most quotable idea in the post.
-->

## TODO


<!-- ============ 5. CONCLUSION ============
     - For my purposes, video editing is a solved problem.
       (Consider hedging to "solved for what I need" — a technical
       audience will push back on the absolute version, given the
       failed keying attempt and the brittle first matcher.)
     - Confident I can make this a sustainable part of a monthly
       routine. The pipeline is reusable; video two starts from here,
       not from scratch.
     - Recommendation to the reader: if you want to make your own
       videos — YouTube, recorded lectures, course material — this
       setup is worth copying. ~$100 of hardware and a chain of tools.
     - Forward look: next project.
-->

## TODO
