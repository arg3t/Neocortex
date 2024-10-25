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



```functionplot
---
title: Standard Normal Dist
xLabel: 
yLabel: 
bounds: [-3,3,0,0.5]
disableZoom: false
grid: true
---
f(x) = (1/(1*sqrt(2*PI)))*pow(E, -(x-0)^2/(2*1^2))
```
