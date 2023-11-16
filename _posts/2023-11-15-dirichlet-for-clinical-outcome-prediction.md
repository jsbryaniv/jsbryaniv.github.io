---
date: 2023-11-15 12:26:40
layout: post
title: Dirichlet Clustring for Clinical Outcome Prediction
subtitle: A simple example
description: Here we show how to use Dirichlet Clustering to predict clinical outcomes.
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

## Introduction

Clustering is an effective way of making predictions. Clustering works by grouping data points together bases on their features. In the reverse of this, if we know the cluster a data point belongs to, we can make predictions about the data point. In the case of medicine this can be helpful for clinical outcome predicitons since by knowing the cluster a patient belongs to, we can make predictions about their diagnosis.

A clustering tool for diagnosis would work as follows: we take a patient, measure various features about them, find out which cluster they most likely belong to, and then make a prediction about their diagnosis based on the cluster they belong to. This is a simple and effective way of making predictions about a patient's diagnosis.

However, we cannot deploy this model until we have learned the features of each cluster. Since the cluster that a patient belongs to is often not directly measureable, we must infer the cluster assignments from the data. This is where Bayesian inference comes in. Bayesian inference is a method of inferring unknown variables from data.

In this article we show how to build a clustering model using Dirichlet Clustering in a Bayesian framework. We then apply our model to a dataset to predict the diagnosis of patents. We will provide a high level overview of how the math and the code works, but we wont dive deep. If you want to learn more about the math behind Dirichlet Clustering, I encourage you to leave a comment below check out this [textbook](https://books.google.com/books?hl=en&lr=&id=LkPGEAAAQBAJ&oi=fnd&pg=PR11&dq=steve+presse+ioannis+sgouralis+data+modeling&ots=uA42nAUM_f&sig=ll9bYjfOmGnMgeJn5QqR-7IM54Q#v=onepage&q=steve%20presse%20ioannis%20sgouralis%20data%20modeling&f=false).

## Data

For this project we are looking at the [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) from Kaggle. The data tracks the medical history of Pima Indians and whether or not they have diabetes.

For each patient we have 8 measured features (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction, and Age) as well as their diabetes diagnosis in the last column(Outcome). We print the first few lines here:

|   Pregnancies |   Glucose |   BloodPressure |   SkinThickness |   Insulin |   BMI |   DiabetesPedigreeFunction |   Age |   Outcome |
|---------------|-----------|-----------------|-----------------|-----------|-------|----------------------------|-------|-----------|
|             6 |       148 |              72 |              35 |         0 |  33.6 |                      0.627 |    50 |         1 |
|             1 |        85 |              66 |              29 |         0 |  26.6 |                      0.351 |    31 |         0 |
|             8 |       183 |              64 |               0 |         0 |  23.3 |                      0.672 |    32 |         1 |
|             1 |        89 |              66 |              23 |        94 |  28.1 |                      0.167 |    21 |         0 |
|             0 |       137 |              40 |              35 |       168 |  43.1 |                      2.288 |    33 |         1 |

For simplicity we will exclude the Pregnancies column as well as any row that has missing information.

In the `main.py` file of our GitHub project we load the data and split it into a training and testing set as follows:
```pyton
# Load data
data = np.genfromtxt('data/diabetes.csv', delimiter=',', skip_header=True)
data = data[:, 1:]                               # Ignore first column (# pregnancies)
data = data[~np.any(data[:, :-1] == 0, axis=1)]  # Filter our rows with missing values

# Split data into training and test sets
np.random.shuffle(data)
split = int(0.8 * data.shape[0])
data_train = data[:split, :]
data_test = data[split:, :]
```

Now that we have our data we can begin building our model.

## Model

### Equations

The foundation of any Bayesian model is the mathematical model that supports it. In this section we will derive the equations that support our model. There are two main parts to the model: the equations that give rise to the cluster assignments and the equations that give rise to the measurements.

#### Cluster Assignments

First we must choose how many clusters there are. Let $K$ be the number of total clusters, indexed from $k=1,...,K$. Now let $N$ be the number of patients, indexed from $n=1,...,N$. Each patient has a cluster assignment $s_n$ where $s_n$ is the cluster that patient $n$ is assigned to. We can represent this as a vector $\mathbf{s} = (s_1, ..., s_N)$.

If we randomly choose a patient they must be assigned to one of the $K$ clusters. Let's define $\pi_k$ as the probability that a randomly chosen patient is assigned to cluster $k$. In other words, $\pi_k$ represents the portion of the patient population that are in cluster $k$. Since the patient must be assigned to one of the $K$ clusters, we have the constraint that $\sum_{k=1}^{K} \pi_k = 1$. We can represent this as a vector $\boldsymbol{\pi} = (\pi_1, ..., \pi_K)$.

#### Measurements

The next part of our model is to define the feature measurements. Let $F$ be the number of features indexed with $f=1,...,F$. Each feature, $f$, of each class, $k$, will have a mean $\mu_{kf}$ and a variance $\sigma_{kf}^{2}$ . We can define vectors $\boldsymbol{\mu}$ and $\boldsymbol{\sigma}$ that contain all of the means and variances respectively.
We can tell different classes apart based on their differences in features. Each patient, $n$, will have one measurement per feature, $f$, which we will call $x_{nf}$. We can represent all of the measurements as a matrix $\mathbf{X}$ where $\mathbf{X}_{nf} = x_{nf}$. The probability that a patient has a certain measurement is given by the normal distribution:
$$
p(x_{nf} | s_n, \boldsymbol{\mu}, \boldsymbol{\sigma}) = \mathcal{N}(x_{nf} | \mu_{s_nf}, \sigma_{s_nf}^{2})
$$

In additions to measuring the patients features, we also have measure their diagnosis. Let $y_n$ be the diagnosis of patient $n$. The probability that patient $n$ has diabetes is conditioned on their class, $s_n$. Each class has a different probability of having diabetes. Let $\phi_k$ be the probability that a patient in class $k$ has diabetes. We can write this as a vector $\boldsymbol{\phi} = (\phi_1, ..., \phi_K)$. All together the probability that a patient has diabetes given their class is:
$$
p(y_n | s_n, \boldsymbol{\phi}) = \phi_{s_n}^{y_n} (1 - \phi_{s_n})^{1 - y_n}
$$

#### Priors

Since we are working in the Bayesian paradigm we must assign a prior distribution over all variables we wish to infer, $\boldsymbol{\pi}$, $\boldsymbol{\mu}$, $\boldsymbol{\sigma}$, and $\boldsymbol{\phi}$.

Starting with $\boldsymbol{\pi}$, the most suitable choice for this distribution is the Dirichlet distribution. The Dirichlet distribution is a distribution over vectors that are constrained to sum to 1. The Dirichlet distribution is parameterized by a vector $\boldsymbol{\alpha} = (\alpha_1, ..., \alpha_K)$ where $\alpha_k$ is the concentration of cluster $k$. This Dirichlet distribution is why we call this method Dirichlet Clustering.

For the remaining variables we set priors as follows: $\boldsymbol{\mu}$ is given a gaussian prior, $\boldsymbol{\sigma}$ is given an inverse gamma prior, and $\boldsymbol{\phi}$ is given a beta prior.

### Code

Now that we have a mathematical model we can deploying this into code. In `model.py` we create a class called `DirichletClustering` that contains all of the code for our model. The class has two main methods: `train` and `predict`. The `train` method takes in the training data and learns the parameters of the model. The `predict` method takes in the testing data and uses the learned parameters to make predictions.

One of the biggest parts to pay attention to is how we store the variables from our method. We choose to save these as a python dictionary object where each key is the variable name and each value is the assignment.

```python
  VARIABLES = {
      # Constants
      'n_data': None,             # The number of data entries
      'n_features': None,         # The number of features
      'n_classes': 2,             # The maximum number of classes considered
      # Variables
      'P': None,                  # The probability of the variables
      's': None,                  # The class assignments
      'x': None,                  # The class outcome probabilities
      'mu': None,                 # The feature means
      'sigma': None,              # The feature standard deviations
      'pi': None,                 # The class probabilities
      # Priors
      'x_prior_alpha': .1,        # The x prior alpha
      'x_prior_beta': .1,         # The x prior beta
      'mu_prior_mean': None,      # The mu prior mean
      'mu_prior_std': None,       # The mu prior standard deviation
      'sigma_prior_shape': 2,     # The sigma prior shape
      'sigma_prior_scale': None,  # The sigma prior scale
      'pi_prior_conc': None,    # The beta prior concentration
  }
```

We start the variables that can be calibrated with `None` values. For example, `mu_prior_mean` is the mean of the prior distribution for the feature means, which is different for each feature. Our class has a function `initialize_variables` which takes in data and then outputs a variables dictionary with the variables initialized (technically we use a `SimpleNamespace` object which is similar to but different from a dictionary).

#### Training and Prediciton

The `train` method takes in the training data and learns the parameters of the model. Training works by running a gibbs sampler algorithms over the data and learning the most probable value for each parameter.

In `main.py` we start by initializing our model with the desired number of clusters, then running the training method:

```python
n_classes = 3
model = DirichletClustering(n_classes)
variables, samples = model.train(data_train)
```

The model learns all the variables of the model including the state assignments, feature variables, and outcome probability.

The `predict` function then takes in a new dataset and predicts the cluster assignments based on the learned parameters. The model is set up to ignore featues masked with NaN values. In our case we want to predict the diagnosis of the patients, so we mask the last column of the data. We then run the predict function and print the results:

```python
data_test_masked = data_test.copy()
data_test_masked[:, -1] = np.nan
s_pred = model.predict(data_test_masked, variables)
```

## Results

Our method does not directly predict the diagnosis of the patients. Instead it predicts the cluster that the patient belongs to. We can then use the cluster assignments to make predictions about the diagnosis. For example, if we know that a patient belongs to cluster 1, we can predict that they have diabetes with a probability of $\pi_k$.

In order to evaluate the effectiveness of our model is to compare the predicted probability of diabetes of each cluster, $\phi_k$ to the actual proportion of diabetes diagnosises per cluster.
We do that below
<a data-flickr-embed="true" href="https://www.flickr.com/photos/199612465@N08/53336518169/in/dateposted-public/" title="Figure_1"><img src="https://live.staticflickr.com/65535/53336518169_88d3d3ae41_z.jpg" width="640" height="480" alt="Figure_1"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

As you can see our model does a reasonable job of predicting the probability of diabetes for each cluster. This means that our model is effective at predicting the diagnosis of patients.

## Discussion

This model is just for demonstration and would need to be improved in several ways before it could be deployed in a real world setting. For example we would need to include: predicting the number of clusters, covariance between features, non-gaussian distribution over clusters, distributions over learned values rather than point measurements, just to name a few. The goal of this article was just to shed light on the potential that Dirichlet clustering has for clinical outcome prediction.

Please feel free to dive deeper into the code on your own, build upon it, or copy it for your own applications. If you have any questions or comments please leave them below.
