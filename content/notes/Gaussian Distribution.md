---
title:  Gaussian Distribution
date: 2022-10-16T02:26:16+02:00
description: 
tags: ['cs/ml', 'math/stats']
aliases: ['Gaussian Distribution', 'Normal Distribution', 'normal distribution']
---

The gaussian distribution, also called the normal distribution occurs in many places in life. It is defined like so:

$$
p(x | \mu, \sigma) = \frac{1}{\sqrt{2\pi \sigma^2}}exp(-\frac{(x-\mu)^2}{2\sigma^2})
$$

```plot
 normal(x, mu, sd) = (1/(sd*sqrt(2*pi)))*exp(-(x-mu)**2/(2*sd**2))
 plot [-3:3] normal(x,0,1)
```