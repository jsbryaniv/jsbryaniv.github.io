---
date: 2025-7-25 12:00:01
layout: post
title: Introducing CuentoGo
subtitle: We vibe coded a Spanish app.
description: CuentoGo lets you read Spanish stories. 
image: https://jsbryaniv.github.io/assets/img/blog/blog_introducing_cuentogo.png
optimized_image: https://jsbryaniv.github.io/assets/img/blog/blog_introducing_cuentogo.png
category: project
tags:
  - project
  - AI
  - language
author: jsbryaniv
paginate: true
math: true
comments: true
---


## Vibe Coding a Spanish App

A couple weeks back, my friend [Julian Jacobs](https://github.com/j8jacobs) and I built CuentoGo, a Spanish learning app. Its a project I've been wanting to do for a while, but never had the time. That is until Julian introduced me to "Vibe Coding". The idea in vibe coding is you just plan high level concepts and lean very heavily on AI to do all the grunt work. We decided to test it out and honestly, the results are pretty cool!

![CuentoGo Screenshot](https://jsbryaniv.github.io/assets/img/blog/blog_introducing_cuentogo_screenshot.jpeg)

The problem with vibe coding, or at least what people complain about on LinkedIn, is that if you don't know how to code, then you run a risk that the AI will build something that breaks or exposes privacy issues. But in our case, Julian and I both know how to build this, we just wanted to get results fast and lazy.

And actually speaking of fast and lazy, we made a few design decisions that really emphasize this, beyond just vibe coding the source code. Our demo app is a static site, meaning it has no server or backend. We just host it on GitHub Pages. This means that we can build a fully functional app without worrying about servers, databases, or any of the usual backend headaches. It’s all client-side, which makes it super fast and easy to deploy.

Check out our prototype here: [CuentoGo](https://j8jacobs.github.io/spanish-app/public/index.html).

Now that I've introduced the app, let me tell you a bit more about how we built it and why. And in the spirit of vibe coding, I'll be transparent and tell you I also leaned heavily on AI to write the rest of this blog post!

Vibes away!

## Why We Built It

I’ve been into learning languages for a long time. Growing up in Arizona I was naturally exposed to a lot of Spanish, then I studied Latin in high school, and later Arabic and Chinese just for fun. And as someone with a physics and AI background, I’ve always thought of language as a kind of compression algorithm: a highly efficient way of turning abstract thoughts into something another brain can decode.

My main priority in language learning is to communicate. For this reason, I care about two things:

* Can I understand what someone’s saying?
* Can I make myself understood?

I don’t worry too much about perfect grammar or fancy vocab. Personally, I would rather be able to express myself like a first grader than know how to translate 100 textbook-perfect sentences. Grammar you can always pick up later.

That’s it. And the best way to get better at those two things is to practice with real humans... but if you don’t have a fluent speaker on call, the next best thing is to immerse yourself in content.

When I was learning Chinese, I tried every app under the sun. The best app I found, by far, was [DuChinese](https://duchinese.net/). It’s brilliant in its simplicity: just short stories written in Chinese, sorted by difficulty. You read along while a native speaker narrates, and if you don’t recognize a word, you click it for the translation. That’s it. No gamified streaks or cartoon owls. Just content.

The only problem? It only works for Chinese and Japanese.

So we made a Spanish version.

## Building the Content with GPT

The real magic of this project was how we built the content because I didn’t write a single story by hand. I used ChatGPT for the entire thing.

It started with me brainstorming a bunch of story prompts with GPT: short slice-of-life situations, history lessons, and some language lessons, each designed to use common vocabulary and grammar. Once I had a list, I wrote a Python script to loop through the ideas and generate stories on demand.

Then I went back through each story and translated them sentence by sentence, again using GPT. That let me keep the Spanish and English perfectly aligned for display in the app.

But the fun didn’t stop there.

I also used GPT to tokenize each sentence, apply part-of-speech tagging, and extract morphological features—tense, number, gender, person, etc. Normally you’d do this with something like spaCy, but GPT gives you two big advantages:
It works out-of-the-box across many languages.
It avoids licensing issues.

The irony is that we are using a state of the art LLM to do rather simple NLP tasks. It might seem like swatting a fly with a bazooka, but it lets me write a single function that works for any language so it's totally worth it.

All the annotated content is stored in tidy JSON files like this:

```json
{
  "sentence": "Luis quiere comprar un sombrero rojo.",
  "translation": "Luis wants to buy a red hat.",
  "words": [
    {
      "word": "Luis",
      "pos": "PROPN",
      "features": {"Gender": "Masc", "Number": "Sing"}
    },
    {
      "word": "quiere",
      "pos": "VERB",
      "features": {"Tense": "Pres", "Person": 3, "Number": "Sing"}
    },
    ...
  ]
}
```

Clean, structured, and ready for any frontend to display beautifully. You can see the full JSON structure in our [CuentoGo](https://j8jacobs.github.io/spanish-app/public/index.html) repository if you are curious.

## No Backend, No Problem

While I was pumping out stories, my friend, Julian, built the app. The best part is it's entirely built without a single backend call.

We hosted everything on GitHub Pages, which meant it had to be a static site. So instead of spinning up a real API, he made a “pseudo-API” by presaving API calls as json files. For example instead of having an endpoint to get the list of stories, we have a json file that has the list of stories. It's a really nifty way to apply backend logic in a static site. The browser just fetches the right JSON and renders the story.

That’s it.

All the logic lives client-side. It works offline. It costs zero dollars to host. And it feels snappy and clean because it’s not making round trips to a server for every click.

Lastly, to make it feel more like a real app, I just added a shortcut to the webpage on my phone’s home screen. Now it launches full-screen, just like a native app. No installs, no updates—just stories in your pocket.

## Why This Works

We didn’t try to build the most advanced AI tutor in the world. We just wanted to make something we’d actually use: real Spanish stories, built-in grammar help, and smooth navigation.

This app doesn’t “test” you (yet). It doesn’t correct your grammar. It just shows you what the language looks like in context—then gets out of the way.

It’s [DuChinese](https://duchinese.net/), but for Spanish.

## Want to Try It?

We’re still polishing it, but it’s already fun to use. Check it out here: [CuentoGo](https://j8jacobs.github.io/spanish-app/public/index.html). And let me know if you find it useful. I’m starting to use this daily, and I can already see my Spanish improving.

This process is wierdly addicting. We originally set out to just have the minimum functionality to make this work, but in classic fashion of getting highly invested in the project, we ended up thinking of a million ways to improve it. Not to mention that the GPT content creation framework means we could easily expand it into other languages!

We might turn this into a real app. Having a static site has a lot of advantages, but some things we are thinking of will require a more robust backend. Even if it doesn't take off, I know I will use it!

In the meantime, the takeaway here isn’t just the app—it’s the process. Between GPT’s flexibility and some clever static-site engineering, we were able to go from idea to working prototype in a weekend. No infrastructure. No translation team. No funding.

Just a vibe.
