---
date: 2024-10-15 12:00:01
layout: post
title: Physics, AI, and the Nobel Prize
subtitle: Reflections on current enthusiasm for physics and AI.
description: Here I write some thoughts reflecting on the recent Nobel Prize in physics.
image: https://jsbryaniv.github.io/assets/img/blog/blog_physics_ai_nobel_prize.png
optimized_image: https://jsbryaniv.github.io/assets/img/blog/blog_physics_ai_nobel_prize.png
category: essay
tags:
  - essay
  - physics
  - ai
author: jsbryaniv
paginate: true
math: true
comments: true
---

A while back, I gave a presentation to my lab about the overlap between physics and recent advances in artificial intelligence. During the presentation, I made a speculative comment to add emphasis of the importance of the field: “Future Nobel Prizes in physics are going to be awarded to people who can advance the field of Artificial Intelligence.” When I said it, I had no idea how quickly that this prediction would come true.

I want to be clear that I’m not trying to say I predicted the Nobel Prize or that I’m some futurist people should look up to. But lately, I've been seeing some controversy about why AI researchers should be awarded a prize in physics. I understand why from the outside looking in it might appear like the Nobel Committee is caving into the AI hype, but what people don’t seem to realize is just how strong the overlap between physics and AI is. I wanted to give my two cents about this, focussing on the history of physics, the current state of physics in AI, and some philosophical points.

## Historical point of view

A typical physics curriculum is divided into four main sections: Kinematics, Electrodynamics, Thermodynamics, and Quantum. I think it's interesting to note that historically, each of these fields launched as its own stand-alone discipline of physics in response to major technological breakthroughs of the day. For example, an original use case for kinematics was to help aim cannonballs at enemy soldiers, electrodynamics was formed to explain how electricity works, and thermodynamics was originally studied to make steam engines more efficient. Starting with a major technological first, the physicists came in afterward to help explain things mathematically and in turn build improved, more efficient versions.  

Clearly, I’m oversimplifying things a bit, but I want to drive a point that fields of physics that help explain important technology are generally higher impact. There is an obvious explanation for this: things that are useful get used more. It's not to say that other types of physics aren’t interesting, for example the physics of swarm behavior in bird flocks is incredibly interesting, but it is just generally harder to get funding for things that don’t have clear benefits to society.

Moreover, the best time to study a field is right after a major technology has been created. This is when there is the most low hanging fruit for young researchers to study. As a field matures, it becomes harder to find new things, and improvements become more incremental. Thus, the researchers who get into the field first will tend to be most successful.

I think it is safe to say that the most important technological breakthrough of our time is AI. Using the logic outlined above, it becomes clear that if physicists can find ways to better explain and improve AI technologies, then “Physics of AI” could very well become its own branch of physics, complete with it's own journals and funding opportunities. This is what I meant when I said that “Future Nobel Prizes in physics will be awarded to AI researchers.”

But the importance of a field is different from whether or not it is actually physics. For example, gene editing is important, but that's biology, not physics. Building spaceships are important, but that's aeronautical engineering, not physics. So what makes me think that AI deserves to be categorized as physics instead of something else?

## Physics and AI

When people mention “Physics” and “AI” in the same sentence, they typically mean one of two things: 1) using AI algorithms to solve problems in physics; or 2) using physics intuition and modeling to help understand and improve AI. When I talk about “Physics of AI” I am referring to this second category. Also, for clarity when I talk about AI, I am referring to the general process of creating a model to predict future measurements based on past measurements, and not something specific like chatbots or image generators.

I don't think most people realize how much physics intuition and modeling goes into the fundamentals of AI. To name a few: 

Image generation models like DALL-E create images using a diffusion process based on Brownian motion principles that come straight out of thermodynamics.
During training, parameters of a deep learning model are assigned momenta and are treated exactly as kinematic particles moving subject to external forces.
The Hopfield Model (named after this year’s Nobel Prize winner), shows that training deep learning models can be equivalent to minimizing energy in a quantum spin glass system.

While these examples make it clear that physics is useful in AI, critics might point out that it doesn't make it automatically a part of AI. For example, some AI models are trained using evolution, but nobody would consider AI a subset of biology. The difference here is that the physics concepts in AI are seemingly fundamental to the core of how AI algorithms work.

At the heart of AI is the goal of minimizing the entropy of a distribution. Entropy and information are fundamentally physics concepts. In fact, physics topics such as Landauer's principle and Maxwell’s Demon indicate show that there is a physical connection between information and energy. Landauer’s principle, states that even at perfect efficiency, a computer must give off heat to record information. Similarly, Maxwell’s Demon is a thought experiment that shows that information about a system is a form of stored energy, that must be dissipated as heat when it is erased.

I agree that much of the physics principles used in modern AI are somewhat of hacks that just seem to work, but it doesn't mean that it will always be this way. I like to relate the current state of AI to the state of steam engines before thermodynamics became popular. People built steam engines that worked, but they didn't quite understand why they worked. In the same way these people were able to build a steam engine without knowing the Carnot cycle, modern AI algorithms use physics techniques without knowing exactly why they work. 

Our goal as physicists is to create mathematical models for this. Ultimately, this will allow AI models to become smarter and more efficient in the same way thermodynamics made engines more efficient. This is exactly what this year's Physics Nobel Prize winners, Hopfield and Hinton, did for AI. By deriving equations describing the learning process mathematically, they opened doors for more efficient algorithms.

## Philosophical discussion

I want to end this essay with a brief philosophical discussion, starting with a question. What is the unifying principle between Kinematics, Electrodynamics, Thermodynamics, and Quantum that makes us all confident to label them all as physics?

For me, physics can be understood as predictive power. Kinematics lets you predict motion of objects, electrodynamics lets you predict motions of charges, thermodynamics lets you predict heat flow, and quantum mechanics lets you predict measurements of small particles. Physics is the process of solidifying our prediction mechanism into equations and models that are easy to solve. And because AI is the general study of making predictions, to me, it is physics.

Now I will end this discussion with an idea that is totally conjecture and should be taken with a grain of salt. It's been said that we, as humans, are prediction machines, taking in continuous measurements from our environment, then predicting what will happen next. Our entire understanding of the world exists entirely in our brains as part of the information processing in our brains, which can be completely described by the mathematics of behind AI and information theory. In this paradigm, the only concrete things that truly exist are statistical relationships, yet we see a world rich with complex yet consistent phenomena around us. Could it be that the laws of physics we see are emergent behavior based in statistical prediction? This is not entirely unheard of, for example temperature is fundamentally a statistical based property, and mass in quantum field theory is defined as a variance. As we explore the connection between physics and prediction models in the future, it will be interesting to see if more physical laws can be cast this way.

## Conclusion

I am excited about the recent enthusiasm about the connection between physics and AI. Big picture, I think that this will be most helpful for the advancement of AI technologies. Increasing compute can only take us so far, I think that a stronger emphasis on the physics of the problem will do wonders.
