---
title: Classification
date: 2022-09-21T12:27:00+02:00
tags: ['cs/ml']
aliases: ['Class Prior', 'Class Conditional']
---

Classification is the problem of guessing to which class it belongs(often
represented by the symbol $\omega$) given a data point. For this problem, it is
quite common to calculate the [[notes/Posterior Probability|posterior probability]] of a data
point for each class and classifying that point as the group with the largest
probability.

Given this definition, a classifier can be defined in the following ways:

- $p(\omega_1 | x) > p(\omega_2 | x)$
- $p(\omega_1 | x) - p(\omega_2 | x) > 0$
- $\frac{p(\omega_1 | x)}{p(\omega_2 | x)} > 1$
- $ln(p(\omega_1 | x)) - ln(p(\omega_2 | x)) > 0$

However, since the posterior is hard to estimate in most cases, it is quite
common to use the [[notes/Bayes' Theorem| Bayes' theorem]]. It maps to classification like
so:

$$
p(\omega | x) = \frac{p(x|\omega)p(\omega)}{p(x)}
$$

In this formula the terms are:

- $p(x | \omega)$ : The distribution of the class $\omega$
- $p(\omega|x)$ : Class conditional
- $p(\omega)$ : Class prior
- $p(x)$ : Data distribution


> [!info] How is class distribution calculated
>
> It is guessed using contextual information on the data. More often than not,
> it is a gaussian distribution.
