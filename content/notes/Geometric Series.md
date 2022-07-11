---
title:  Geometric Series
date: 2022-01-17T06:06:44+01:00
description: 
tags: ['math/analysis', 'math/calculus']
aliases: ['']
---
If a [[notes/Sequences|sequence]] a can be written as:

$$
a_n = cr^n
$$ 

Than this is sequence forms the geometric [[notes/Series|Series]]:

$$
S_k = \sum_{n=1}^k cr^n
$$

Doing some algebra and some math magic we can derive a more general formula:

$$
S_k = a\frac{1-r^k}{1-r}
$$

This series [[notes/Convergent Series|converges]] if $|r| \leq 1$. This is fairly obvious when you take the limit of the equation above:

$$
\lim_{k\to\infty} a\frac{1-r^k}{1-r}

a \lim_{k\to\infty} \frac{1-r^k}{1-r}
$$

Since $r^k$ only goes to $0$ when $|r|$ is less than 1 it converges into:

$$
\frac{a}{1-r}
$$

Otherwise, it is $DIV$.
