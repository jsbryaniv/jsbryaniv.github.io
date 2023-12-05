---
date: 2023-11-30 12:00:01
layout: post
title: Chinese Character Generator
subtitle: A simplified model for generative AI
description: Here we show how to use diffusion based generative models to generate Chinese characters.
image: https://live.staticflickr.com/65535/53334792868_86038b3779_b.jpg
optimized_image: https://live.staticflickr.com/65535/53334792868_86038b3779_b.jpg
category: math
tags:
  - bayesian
  - coding
  - prediction
author: jsbryaniv
paginate: true
math: true
comments: true
---

This article is a companion to the [GitHub project](https://github.com/jsbryaniv/DirichletClustering) of the same name. The project contains all the code necessary to run the model described in this article. The code is written in Python and is designed to be easy to read and understand. If you have any questions, please leave a comment below or message me directly.

## Introduction

Generative AI for image generation is a booming topic right now. The field has rapidly advanced in an incredibly short amount of time, largely due to the discovery of clever ways to frame the image generation problem. In particular, diffusion based models have been shown to be very effective at generating high quality images. In this article, we will show how to use a diffusion based model to generate Chinese characters.

There are many resources online that give great explanations of the diffusion based models. Instead of rehashing those explanations, here we will give a slightly different perspective on how to think about these models from a probabiliy and physics point of view. Also, we will put a large focus on implementation, building up a model from scratch in a way that is (hopefully) easy to understand.

## Diffusion Based Models

Here we explain what a diffusion model is and how it can be used to generate images. We start by rigorously definding the image generation problem as a sampling problem. Then we show how to use diffusion to solve the sampling problem.

### Formulating the problem

Our goal is to generate an image, $y$, that looks similar to the images in the training set, $X$. In our case where $X$ is the set of Chinese characters, we want to generate an image, $y$, that looks like a Chinese character. This is easy to say in words, but we need to be a bit more precise if we want to treat this as a math problem.

We start by treating the training images as random variables. This may be strange to think about Chinese characters as random variables at first because they are taken f

### Diffusion as a sampling problem

## Code

### The data

For our example we use a dataset of Chinese characters printed on a 64x64 grid. For simplicity, instead of having a downloadable dataset, we instead print the characters directly using python. You can learn more about this dataset in the [lab blog](https://labpresse.com/demystifying-pytorch-datasets-building-a-chinese-character-dataset/).

We copy the code from the [original blog post](https://labpresse.com/demystifying-pytorch-datasets-building-a-chinese-character-dataset/) into our project under `data_generator.py`.

### The model

We start by defining the model class. We use a simple class structure that allows us to easily add new models in the future. We define the class in `model.py`.

```python
```

### Training

## Results

## Conclusion
