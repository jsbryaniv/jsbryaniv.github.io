---
date: 2025-07-18 12:00:01
layout: post
title: Building Train Hats
subtitle: Integrating new tools into old frameworks.
description: Sometimes to make a train, you need to make a hat. 
image: https://jsbryaniv.github.io/assets/img/blog/blog_train_hats.png
optimized_image: https://jsbryaniv.github.io/assets/img/blog/blog_train_hats.png
category: essay
tags:
  - essay
  - AI
author: jsbryaniv
paginate: true
math: true
comments: true
---


## Building Train Hats

In AI research, we're trained to focus on improving the state-of-the-art. Many projects are designed to make incremental improvements with the hope that over long time spans, the small improvements add up. There's value in that. But recently, I've discovered that the research projects that make the most immediate, tangible impact, aren't the ones that incrementally improve models, but rather the ones that make existing models more usable. This was echoed frequently at the Mayo Clinic AI Summit I attended last week.

Getting models into the real world is hard. And not in the ways we were taught. AI classes usually teach how to build a model and make a basic app. But real-world deployment often means working with clunky legacy software, vendor-locked systems, and layers of organizational inertia. In these environments, nobody cares about your extra 1% performance boost if they can’t use it.

Integrating new tools into old frameworks is challenging. At the AI Summit, I talked to a lot of people facing the same thing. It was nice to hear that I wasn't alone in this. But what was really cool was that I met a few who had managed to break through. When I asked how they managed to get their tools deployed they all said the same thing:

“You just gotta kind of... hack it.”

That might sound obvious to some. But for me, it was an epiphany. As I started to think about this idea, I remembered an old story I heard about video game developers, which was funny at the time I read it, but now holds a whole new meaning: making a train a hat.

## When you can’t build a train, build a hat

The story is about the developers of Fallout 3, which was actually one of my favorite video games of all time. Anyway, Fallout 3 was a massive success, so they continued to develop the game after it was released by creating DLC (downloadable content) expansion packs that give you additional quests and things. In one of these DLC packages, they wanted the player to ride on a train. But the problem is that in the game physics engine, there was no way to make movable objects that players ride on. Since the game was already released, the developers were not able to go back and update the physics engine to allow for moving ridable objects. So they were stuck: they had to either give up on the train or find a work around. They must have really wanted that train, because they found a strange way to make it work!

They found a loophole: while characters in the game could not stand on moving objects, they could for some reason stand on other characters as they moved. So the train would have to be classified as a character, rather than an object. But evidently creating new character classes in the game engine was difficult as well, so they came up with a clever solution: they defined the train as a wearable hat. To put the train into the game, they created an invisible character that was rendered underground, and had them wear the train hat.

In the game you would never notice the difference. You just step onto the train and it takes you to the next station, but behind the scenes, there was actually an invisible man under you the whole time, running you from station to station... man that guy's legs must be tired!

Here is the article that describes the story in more detail: [Fallout 3's Train Hat](https://www.pcgamer.com/heres-whats-happening-inside-fallout-3s-metro-train/).

## Reflection

I loved this story when I first read it because I thought that an invisible man wearing a train as a hat was a funny image. I love it now because it highlights that if you want to integrate a tool into an existing platform, sometimes you need to think outside of the box. I find that very relevant and inspiring.

Going back to the big picture, if the goal is to make AI tools usable, then we have to integrate them into frameworks that people are using. If these frameworks are hard to work with, we need to be clever and find work around. If the work around seems odd, that isn't necessarily a bad thing, maybe it just means you're clever!

Sometimes if you want a train you need to make a hat.



