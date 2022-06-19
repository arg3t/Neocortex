---
title:  Power Series As Functions
date: 2022-01-19T09:06:32+01:00
description: 
tags: ['math/analysis', 'math/calculus']
aliases: ['']
---
Since power series are defined relevant to a value $x$. We can define some properties for two series $f(x) = \sum a_nx^n$ for $|x|<R_1$ and $g(x) = \sum b_nx^n$ for $|x|< R_2$:

* $cx^k\sum f(x) = \sum ca_n x^{n+k}$ $|x| < R_1$
* $f(cx^k) = \sum a_n c^n x^{nk}$ $|cx^k| < R_1$
* $f(x - c) = \sum a_n (x-c)^n$ $|x-c| < R_1$
* $f(x) + g(x) = \sum (a_n+b_n)x^n$ $|x| < min(R_1, R_2)$

It is also possible to differentiate power series 
$$
f(x) = \sum c_n(x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 ...
$$

$$
f'(x) = c_1 + 2c_2(x-a) + 3c_3(x-a)^2 = \sum nc_n(x-a)^{n-1}
$$

$$
\int f(x)dx = c + c_0(x-a) + \frac{c_1(x-a)^2}{2} = \sum \frac{c_n(x-a)^{n+1}}{n+1}
$$

> The radius of convergence remains the same for both integration and differentiation

