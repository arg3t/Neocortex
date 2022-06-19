---
title:  Power Series
date: 2022-01-18T10:23:44+01:00
description: 
tags: ['math/analysis', 'math/calculus']
aliases: ['']
---
Power series are a special kind of [[/notes/Series|Series]] that can be written in the form:

$$
\sum_{n=0}^\infty = c_n(x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 ...
$$

The example is called a power series in $(x-a)$

The special part of power series is that the [[/notes/Convergent Series|convergence]] of the series depends on the value of $x$.  To determine for which values of $x$ the series converges, we simply apply a [[/notes/Ratio Test|Ratio Test]] to the series and calculate $x$ for

$$
\frac{|x-a|}{R} < 1
$$

In this case, $a$ is the series' center of convergence while $R$ is its radius of convergence. 

![[images/Pasted image 20220118222816.png]]

> In power series, after solving for $x$ we get a range for $x$. Even though the series converges in this range, we need to check manually if the series also converges at the ends of those ranges.

