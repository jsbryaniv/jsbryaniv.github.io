---
date: 2023-12-07 12:00:01
layout: post
title: Chinese Character Generator
subtitle: A simplified model for generative AI
description: Here we show how to use diffusion based generative models to generate Chinese characters.
image: https://live.staticflickr.com/65535/53380463416_d0653321c7_z.jpg
optimized_image: https://live.staticflickr.com/65535/53380463416_d0653321c7_z.jpg
category: science
tags:
  - deep learning
  - coding
  - generative ai
author: jsbryaniv
paginate: true
math: true
comments: true
---

This article is a companion to the [GitHub project](https://github.com/jsbryaniv/CharacterGenerator). The project contains all the code necessary to run the model described in this article. The code is written in Python and is designed to be easy to read and understand. If you have any questions, please leave a comment below or message me directly.

## Introduction

Generative AI for image generation is a booming topic right now. The field has rapidly advanced in an incredibly short amount of time, largely due to the discovery of clever ways to frame the image generation problem. In particular, diffusion based models have been shown to be very effective at generating high quality images. In this article, we will show how to use a diffusion based model to generate Chinese characters.

There are many resources online that give great explanations of the diffusion based models. Instead of rehashing those explanations, here we will give a slightly different perspective on how to think about these models from a probabiliy and physics point of view. Also, we will put a large focus on implementation, building up a model from scratch in a way that is (hopefully) easy to understand.

## Diffusion Based Models

Here we explain what a diffusion model is and how it can be used to generate images. We start by rigorously definding the image generation problem as a sampling problem. Then we show how to use diffusion to solve the sampling problem.

### Formulating the problem

Our goal is to generate an image, $y$, that looks similar to the images in the training set, $X$. In our case where $X$ is the set of Chinese characters, we want to generate an image, $y$, that looks like a Chinese character. This is easy to say in words, but we need to be a bit more precise if we want to treat this as a math problem.

We start by treating the training images as random variables drawn from some common distribution. In our case, this distribution is the random process of thousands of years of Chinese history that gave rise to the characters we see today. Under this paradigm we say that each image, $x$, in $X$ is drawn from this distribution, $P$. We can write this as
$$
x \sim P.
$$

When we say that we want to generate an image, $y$, that looks similar to the training set, what we mean is that we want to generate an image that looks like it was drawn from the same distribution, $P$. In other words, we want to sample,
$$
y \sim P.
$$

So really, in this paradigm generative AI is just a spicy sampling problem. The trick is to figure out how to sample from $P$, given that we only have access to the training set, $X$.

### Diffusion as a sampling method

Our goal is to sample an image, $y$, from  a distribution $P$, where we do not know the form of $P$, but we do have access to training samples, $X$. Diffusion based models are a way to sample from $P$ using only $X$. There are many types of diffusion models, but here we will focus on one simple type that is easy to understand and implement.

Our diffusion model will consist of two functions: $c$ the "corruptor" and $f$ the "denoiser". The corruptor adds random noise to an image and the denoiser removes the noise. We define the function $c$ as
$$
c(x) = x + \epsilon
$$
where $\epsilon$ is a Gaussian distributed random noise. The denoiser function, $f$, is a neural network that takes in an image and outputs a cleaned image. The denoiser is trained on the training set, $X$, so that it learns to remove the noise added by the corruptor.

The diffusion process works by taking a starting image and iterively applying the corruptor and denoiser repeatedly
$$
y_0 = x \\
y_1 = f(c(y_0)) \\
...\\
y_n = f(c(y_{n-1})).
$$
Each time the corruptor and denoiser are applied, the resulting image is close to, but not exactly the same as the previous image. Over many iterations, the image will become more and more distored. [It has been shown](https://arxiv.org/abs/1305.6663) that after many steps the image will converge to an image that is sampled from the distribution used to train the denoiser.

There are many ways to think about this, but the way that I think is easiest to wrap my head around is to think of this in terms of statistical physics. An image, $y$, is really just a point in a very high dimensional space, where the dimensionality is the number of pixels in the image and the position along each dimension is the intensity of the the corresponding pixel. Each point in image space has a corresponding probability, $P(y)$, that is the probability of sampling that image. The negative log probability, $U(y)=-log(P(y))$, can be thought of as the energy of the image. So every point in space corresponds to an image and each image has an energy associated with it, forming a potential energy landscape in image space.

The denoiser, $f$, acts as a restoritive force that pushes images to lower energy configurations (technically $f(x)=x+F(x)$ where $F$ is restoring force, but for simplicity we will call $f$ the force). Images from the training set should have the highest probability and thus the lowest energy, meaning they correspond to minima of our energy landscape. Thus the force should be zero for at image space locations corresponding to the training set. Images near local minima should feel a restoring force pushing towards the nearest minimum.

Adding noise to an image is like giving it a thermal kick. For small displacements, the restoring force should take it back to the same minimum, but for larger kicks the image will be pushed to a new minimum. This new minima will be a new image. Thus, by iteratively applying the corruptor and denoiser, we are randomly walking around the energy landscape, sampling new images!

I like to imagine the sampling process as a ball getting kicked around the hills and valleys of this potential energy landscape. I created a nice visual for this below.
<a data-flickr-embed="true" href="https://www.flickr.com/photos/199612465@N08/53380463416/in/dateposted-public/" title="CharacterHills"><img src="https://live.staticflickr.com/65535/53380463416_d0653321c7_z.jpg" width="640" height="640" alt="CharacterHills"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

The training procedure is then to just train the denoiser to restore the original image after the corruptor has been applied.

## Code

### The data

For our example we use a dataset of Chinese characters printed on a 64x64 grid. For simplicity, instead of having a downloadable dataset, we instead print the characters directly using python. You can learn more about this dataset in the [lab blog](https://labpresse.com/demystifying-pytorch-datasets-building-a-chinese-character-dataset/).

We copy the code from the [original blog post](https://labpresse.com/demystifying-pytorch-datasets-building-a-chinese-character-dataset/) into our project under `data_generator.py`.

### The model

We start by defining the model class. We use a simple class structure that allows us to easily add new models in the future. We define the class in `model.py`.

```python
class Generator(nn.Module):
    """Generator network."""

    def __init__(self, img_shape=(64, 64), num_channels=1, num_features=8, num_layers=4, num_steps=8, max_kT=1.5):
        super().__init__()

        # Set the parameters
        self.img_shape = img_shape
        self.num_channels = num_channels
        self.num_features = num_features
        self.num_layers = num_layers
        self.num_steps = num_steps
        self.max_kT = max_kT
        
        # Set temperature schedule
        self.kT_schedule = list(torch.linspace(0, max_kT, num_steps))


        # Input block
        self.input = nn.Sequential(
            nn.Conv2d(num_channels, num_features, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features),
            nn.ReLU(),
            nn.Conv2d(num_features, num_features, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features),
            nn.ReLU(),
        )

        # Encoder block
        self.encoder = nn.ModuleList()
        for i in range(num_layers):
            num_in = num_features * 2**i
            num_out = num_features * 2**(i+1)
            self.encoder.append(nn.Sequential(
                nn.Conv2d(num_in, num_out, kernel_size=3, stride=2, padding=1),
                nn.BatchNorm2d(num_out),
                nn.ReLU(),
                nn.Conv2d(num_out, num_out, kernel_size=3, stride=1, padding=1),
                nn.BatchNorm2d(num_out),
                nn.ReLU(),
            ))

        # Decoder block
        self.decoder = nn.ModuleList()
        for i in range(num_layers):
            num_in = num_features * 2**(num_layers-i)
            num_out = num_features * 2**(num_layers-i-1)
            self.decoder.append(nn.Sequential(
                nn.ConvTranspose2d(num_in, num_out, kernel_size=3, stride=2, padding=1, output_padding=1),
                nn.BatchNorm2d(num_out),
                nn.ReLU(),
                nn.Conv2d(num_out, num_out, kernel_size=3, stride=1, padding=1),
                nn.BatchNorm2d(num_out),
                nn.ReLU(),
            ))

        # Output block
        self.output = nn.Sequential(
            nn.Conv2d(num_features, num_features, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(num_features),
            nn.ReLU(),
            nn.Conv2d(num_features, num_channels, kernel_size=3, stride=1, padding=1),
            nn.Sigmoid(),
        )

    def numel(self):
        """Number of parameters."""
        return sum(p.numel() for p in self.parameters())

    def forward(self, x):
        """Forward pass."""

        # Initialze skips
        skips = []

        # Normalize the input
        x = x - x.mean(dim=(2, 3), keepdim=True)
        x = x / x.std(dim=(2, 3), keepdim=True)

        # Input
        x = self.input(x)

        # Encoder
        for i in range(len(self.encoder)):
            x = self.encoder[i](x)
            skips.append(x)
            
        # Decoder
        for i in range(len(self.decoder)):
            x = x + skips[-i-1]
            x = self.decoder[i](x)

        # Output
        x = self.output(x)

        return x
    
    @torch.no_grad()
    def dream(self, num_cycles=10, kT_schedule=None):
        """Dream."""
        
        # Set the temperature schedule
        if kT_schedule is None:
            kT_schedule = self.kT_schedule

        # Initialize image
        device = next(self.parameters()).device
        img_shape = self.img_shape
        x = torch.randn((1, 1, *img_shape), device=device)

        # Loop over cycles
        for _ in range(num_cycles):

            # Increase temperature
            for kT in kT_schedule:
                x = x + torch.randn_like(x, device=x.device) * kT
                x = self(x)

            # Decrease temperature
            for kT in kT_schedule[-1::-1]:
                x = x + torch.randn_like(x, device=x.device) * kT
                x = self(x)

        # Return the result
        return x
```

This model is just a simple convolutional neural network with skip connections. We simply go down an encoding and decoding process, adding skip connections along the way.

Notice that in addition to the standard forward function we also added a function called `dream`. This is the character generation process of adding noise and denoising. We will use this function later to generate characters.

### Training

For training we use a simple training loop. The loss function is the difference between input and output images. We train the model by diffusing the image for a few steps with increasing temperature and then diffusing it back to the original image with decreasing temperature.
  
```python

# Initialize loss with regulator
loss = (
    sum(p.pow(2.0).sum() for p in generator.parameters())
    / sum(p.numel() for p in generator.parameters())
)

# Increase temperature
image = target_image.clone()
for i, kT in enumerate(generator.kT_schedule):

    # Check if end of schedule
    last_step = i == generator.num_steps - 1
    
    # Add noise
    image = image + torch.randn_like(image, device=device) * kT
    input_images.append(image.clone())

    # Forward pass
    image = generator(image)
    output_images.append(image.clone())
    
    # Loop down temperature schedule from i to 0
    for j in range(i-1, -1, -1):
        kT2 = generator.kT_schedule[j]
        
        # Add noise
        image = image + torch.randn_like(image, device=device) * kT2
        if last_step:
            input_images.append(image.clone())
        
        # Forward pass
        image = generator(image)
        if last_step:
            output_images.append(image.clone())

    # Add loss
    loss += F.mse_loss(image, target_image)

```

Notice that we are not just training up to the maximum temperature each time. We make sure to go one step up one step down, two steps up two steps down, etc. This ensures that the model learns to denoise at all temperatures. The highest noise level we add is sufficiently high enough that the image is completely unrecognizable. This is important because it ensures that the model learns to denoise even when the image is completely corrupted.

## Results

I save the inputs and outputs of the last step in the training to see how the model distorts the image as it is diffused. You can see this below.
<a data-flickr-embed="true" href="https://www.flickr.com/photos/199612465@N08/53380705118/in/dateposted-public/" title="FinalEpoch"><img src="https://live.staticflickr.com/65535/53380705118_66905d2482_z.jpg" width="640" height="215" alt="FinalEpoch"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
Notice that the first few iterations are very subtle and the image is well restored, but as the temperature is increased the image becomes more and more distorted. By the end, the image is completely unrecognizable.

We can also see how the model performs by dreaming up new images. Below we show the output of a few iterations of the dreaming process.
<a data-flickr-embed="true" href="https://www.flickr.com/photos/199612465@N08/53380971770/in/dateposted-public/" title="NewCharacters"><img src="https://live.staticflickr.com/65535/53380971770_13ccb6f2e5_z.jpg" width="640" height="521" alt="NewCharacters"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>
These images are crude, but they do capture some elements of the radicals that make up the Chinese writing system such as the the box (口, kǒu), the vertical line (丨, gǔn), and the dot (丶, zhǔ). In fact the top left one looks to me almost like a real character, 近 (jìn), which means "near". 

## Conclusion

This model shows the basics of generative AI. While we are not quite ready to make the next Dall-e, I think that we at least have a better understanding of the math behind it and a minimal model.

This model was designed to be very simple, but I am surprised at how well it performed. I think it would be interesting to try this same training with a more complex arcitecture.

I hope that you enjoyed this project and were able to learn from it. If you would like to see more content like this please let me know. I always welcome feedback, critiques, and suggestions. Thanks for reading!
