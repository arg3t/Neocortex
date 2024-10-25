---
title:  Using Bayes Rule
date: 2024-10-22T12:24:05+02:00
description: 
tags: ["cs/ml"]
aliases: ['Using Bayes Rule']
---

In order to use [[Bayes' Theorem]] to guess the class of each data point in a given dataset, we need to estimate

1. **The class priors:** $p(y) = \frac{N_y}{N}$ where $N$ is the size of our dataset.
2. **Unconditional Class Probabilities:** $p(\mathbf{x}) = \sum_{i=1}^Cp(\mathbf{x}|y_i)p(y_i)$. This too is easy to calculate, since it does not require any assumptions.
3. **The class conditional probability:** $p(\mathbf{x}|y)$. In order to calculate this one, we need to make an assumption for the distribution of each class $y_i$.

Usually, for the class conditional, [[Gaussian Distribution|Gaussian Distribution]] is used. The dimensionality of the distribution depends on the dimensions of each data point $\mathbf{x}$.