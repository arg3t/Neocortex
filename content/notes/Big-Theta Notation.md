---
title: Big-Theta Notation
date: 2021-11-16T21:07:41+01:00
tags: [ 'cs/math', 'cs/analysis']
---


![Big-Theta notation](images/Pastedimage20211112113644.png)

Big theta notation is a little more complicated, the Big-Theta notation covers both the worst and best-case scenarios that an algorithm might have relative to its input (n). So it essentially is a combination of both [[notes/Big-Oh Notation|Big-Oh Notation]] and [[notes/Big-Omega Notation|Big Omega Notation]]. Since we are trying to cover two cases, the calculation is quite different:

##  Calculating Big Theta

A function $f(n)$ is said to be $\Theta(g(n))$ if there exists constants $c' > 0$, $c'' > 0$  and $n_0 > 1$ such that:

$$\forall n (n > n_0 \implies c'g(n) \leq f(n) \leq c''g(n))$$