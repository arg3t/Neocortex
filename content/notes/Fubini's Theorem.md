---
title:  Fubini's Theorem
date: 2022-03-06T08:14:52+01:00
description: 
tags: ['math/calculus']
aliases: ['']
---
Fubini's theorem for [[notes/Double Integrals Over Rectangles|Double Integrals Over Rectangles]] is that for a rectangle $D = [a,b] \times [c,d]$ the integral can be written as:

$$
\iint_D f(x,y)dA = \int_a^b\int_c^df(x,y)dydx = \int_c^d\int_a^bf(x,y)dxdy
$$

> Note that the order of the integrals as well as the order of the $dx$ and $dy$ are important in this case