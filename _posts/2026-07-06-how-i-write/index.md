---
date: 2026-07-06 12:00:01
layout: post
title: "How I Write"
subtitle: "A Peek Behind the Curtain of My Writing Process"
description: "I share how I write, from ideation to publication, and the tools I use to make it happen, especially with regard to AI tools."
image: assets/coverart_how_i_write.png
category: essay
tags:
  - essay
---

I thought it would be fun to share a bit about my writing process, from ideation to publication, and some of the tools I use along the way.

I especially want to discuss how I use AI tools to help me write, since there is a lot of debate right now about how AI should be used in writing. As an AI professional, I personally lean heavily into these tools, but I also feel that despite using AI throughout my workflow, the end result is still my own work. I want to be transparent about how I use AI so that people don't think I'm "cheating."

## Why I Write

Before I can discuss my writing process, I think it's important to explain why I write and what I'm ultimately trying to accomplish.

Big picture, I have a long list of projects and products that I want to build. I use my website and social media to share those ideas, get feedback from the community, and eventually sell some of the things I create. To get there, I first need to build an audience and a community of people who are interested in my work and ideas. And to build an audience, I need to consistently publish content that people can read and engage with. That's where my writing comes in.

My writing generally comes in two flavors. The first flavor is what I consider my **primary content**: project updates and technical deep dives that directly showcase the work I'm doing. These align closely with my long-term goals, but they're also time consuming to produce. The second flavor is what I think of as **supplemental content**: essays, tutorials, book reviews, and other shorter articles. These are much easier to write and allow me to maintain a consistent publishing schedule between larger projects. Ironically, the supplemental content is often more popular than the primary content. It's generally easier to read, more relatable, and doesn't require as much technical background as the deep dives.

With that in mind, one of the biggest constraints on my writing is time and efficiency. I want to get my ideas out as clearly as possible and as quickly as possible so that I can spend the rest of my time building.

## How I Think of Ideas

Ideas just randomly pop into my head all the time. Whenever that happens, I immediately write them down in my phone so I can come back to them later and organize them into lists based on topic.

The challenge isn't coming up with ideas—it's filtering them. I try to make sure the ideas stay reasonably on brand, where my brand currently sits somewhere between physics, AI, coding, and entrepreneurship. Of course, that brand is constantly evolving. If you go back far enough on my website, you'll find a period where I wrote much more about biotech and healthcare.

Anyway, once I've narrowed my list down to a handful of ideas that I think would make interesting articles, I usually just pick one and start writing!

## How I Write

Once I have an idea to write about, I start with a walk, or clean the house, or do some random activity where I can mindlessly get my body moving while my mind is free to think about the idea. I basically write an outline of what I want to say in my head. This usually takes about an hour, although more complicated ideas might take a few days for things to come together.

The next challenge is converting that outline into a finished article as efficiently as possible. This is where I lean heavily on AI tools. Remember, my main goal is to work on projects, so I don't mind using AI to help me write, so long as the end result is still my own work and my own ideas.

The first step is to convert my outline-in-head to an outline-in-text, which I do by writing a bullet point list of everything I want to say directly into VSCode in the markdown file that will eventually be the final article. Here, I basically write out the entire article in bullet points. I don't worry much about grammar, sentence structure, or whether every sentence starts with the same word. My only goal is to get every idea onto the page.

This is also the first place where AI starts helping me. It turns out that GitHub Copilot is surprisingly good at completing rough bullet points. Often I'll type just a few words, and Copilot correctly predicts the rest of the sentence. It's a surprisingly effective time saver! I'll put a code block on the end of this article with an example of what this particular article looks like as a bullet point rough draft.


Once the outline is finished, I need to write the first draft. For this I honestly just feed the bullet point list directly into an AI and have it convert my outline into a full article. The main advantage of using an AI to convert an outline into a rough draft is that it automatically does things like make sure each sentence starts with a different word, and it sometimes it acts like a thesaurus and will replace words with synonyms if I use the same word too many times in a row. This is the most helpful part of AI for me, because historically, I would spend far too much time rewriting paragraphs simply to improve the flow. I'd notice that several sentences all started with the same word, or that I had used the same phrase too many times in a row. Then I'd rewrite one sentence, which meant changing the next sentence, which meant changing the one after that, and before long I had spent half an hour rewriting a single paragraph. AI handles that kind of editing remarkably well. It naturally varies sentence structure, replaces repeated words with synonyms, and generally produces a much cleaner first draft much faster than I would have written on my own.

The next step is refinement. I read through the article, delete the em dashes and other strange formatting that AI sometimes likes to add, replace some periods with exclamation marks, and rewrite sentences until they sound like something I would naturally say.

Finally, and probably most importantly, I stop iterating as soon as the article is good enough! I've already said this a few times, but my writing is a tool that supports my projects. It isn't the end goal. I could spend several more hours polishing every article, but those hours are usually better spent building something new. Once I'm happy with the article, I do one final pass through AI to catch any remaining typos (VSCode doesn't have a good spell checker, so AI ends up filling that role as well). Then I publish it!

## Conclusion

I hope this gives you a better idea of how I write and how I use AI tools throughout the process. Maybe you'll find some of these ideas useful in your own writing. Or maybe you'll think I'm cheating! Either way, I'd love to hear what you think.

As promised, here's the original bullet-point outline that I fed into an AI to generate the first rough draft of this article.

````text
---
date: 2026-07-06 12:00:01
layout: post
title: "How I Write"
subtitle: "A peek behind the curtain of my writing process"
description: "I share how I write, from ideation to publication, and the tools I use to make it happen, especially with regard to AI tools."
image: assets/coverart_how_i_write.png
category: essay
tags:
  - essay
---


- I want to share a bit about my writing process, from ideation to publication, and tools I use along the way.

- I especially want to discuss how I use AI tools to help me write, since there is a lot of debate on how AI should be used in writing.
- As an AI professional I personally lean heavily into using AI tools, but I also feel that despite that the end result is still my own work.
- I just want to be transparent about my use of AI, so that people don't think I'm "cheating". 

## Why I write

- Before I can discuss my writing process, I think its important to discuss why I write and what I am trying to accomplish with my writing.

- Big picture, I have a bunch of ideas for projects and products that I want to build, and I want to use social media and my website as a way to share these ideas, get feedback from the community, and sell some of the end products.
- In order to get there, I need to build an audience and a community of people who are interested in my work and ideas
- And in order to get an audience, I need to have consistent content that people can read and engage with, which is where my writing comes in.

- My writing comes in two flavors: the primary content, like the project updates and technical deep dive articles and the secondary content, like essays and tutorials.
- The primary content aligns with my long-term goals of showcasing my work, but it is time consuming to write.
- In order to maintain a consistent publishing schedule I rely on secondary content, which is easier to write and can be published more frequently.
- Ironically, the secondary content is often more popular than the primary content, since it is easier to read and is more relatable than the technical deep dives.

- With this in mind, you can see that one of the biggest constraints on my writing is time and efficiency. I want to get my ideas out as clearly as possible and as quickly as possible so that I can focus on building.

## How I Think of Ideas

- Ideas just randomly pop into my head constantly.
- As these ideas pop into my head I write them down in my phone to come back to them later organizing them by topic in lists.

- I get so many ideas that my main job is to filter through them.
- I try to make sure the ideas are "on brand", where my brand is somewhere between physics, AI, and entrepreneurship.
- And by the way, the brand is constantly evolving, if you go back far enough youll see when a lot of my focus was on biotech and healthcare.
- Anyway, once I narrow down the list to a few ideas that I think would be interesting to discuss I just randomly pick one to write about.

## How I write

- Once I have an idea to write about, I start with a walk, or clean the house, or do some random activity where I can mindlessly get my body moving while my mind is free to think about the idea.
- This usually will take an hour or so, but for more complex ideas I might come back to it over a few days.
- I basically write an outline of what I want to say in my head.

- Next the goal is to convert from outline-in-head to finished article as efficiently as possible.
- I lean heavily on AI tools to help me with this.
- Remember, my main goal is to work on projets, so I dont mind using AI to help me write, so long as the end result is still my own work and my own ideas.

- The first step is to convert my outline-in-head to an outline-in-text, which I do by writing a bullet point list of everything I want to say directly into VSCode in the markdown file that will eventually be the final article.
- I more or less write out a full rough draft in bullet points, but I dont worry too much about grammar or whether every sentence starts with the same word or anything like that.
- This is the first place where I get help from AI, because it turns out that my copilot AI code completion tools is also pretty good at finishing bullet point rough drafts. For a lot of the points i can just write a few words and the AI will finish the sentence for me, which is a huge time saver.
- I'll put a code block on the end of this article with an example of what this particular article looks like as a bullet point rough draft.

- Next I honestly just feed the bullet point list directly into an AI and have it convert my outline into a full article. 
- The main advantage of using an AI to convert an outline into a rough draft is that it automatically does things like make sure each sentence starts with a different word, and it sometimes it acts like a thesaurus and will replace words with synonyms if I use the same word too many times in a row.
- This is the most helpful part of AI for me, because historically I would spend far too much time rewriting paragraphs making sure that I don't use the same word too many times in a row, and things like that. Then if you change one sentence, you have to go back and change the other sentences around it so that the surrounding sentences don't use any words from that sentence, then on and on, until it becomes a huge time sink.
- The fact that AI does that now is a life saver.

- Next I refine the article.
- Mainly I read through the article and delete the em dashes and strange formatting that AI sometimes adds
- I also will rewrite sentences so that they sound more like me.

- Finally and most importantly, I stop itterating as soon as the article is good enough.
- I've said this multiple times already, but my writing is a tool to help my projects, not the end goal, so I don't want to spend too much time on any one essay or article.
- Once I feel like the article is good enough, I will do one last pass through an AI to catch typos (VSCode doesn't have a good spell checker so I rely on AI for that) and then I publish it.


## Conclusion

- I hope this gives you a better idea of how I write and how I use AI tools to help me write.
- Maybe you might find this useful for your own writing, or maybe you think I'm cheating!
- Either way, feel free to let me know what you think!

- As promised here is the bullet point outline draft of this article which I fed into an AI to generate the first rough draft of this article:

```
<AI Dont actually generate this, just put in a blank code block with this message!>
```
````