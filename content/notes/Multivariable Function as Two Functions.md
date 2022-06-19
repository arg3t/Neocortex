---
title:  Multivariable Function as Product of Two Functions
date: 2022-03-06T08:35:04+01:00
description: 
tags: ['math/calculus']
aliases: ['']
---
If you can write a [[/notes/Multivariable Functions|multivariable function]] as the product of two functions, one of which is defined by $x$ and the other $y$, [[/notes/Double Integrals Over Rectangles|integrating]] it becomes much easier. You can simply rewrite the function $f(x,y) = g(x)h(y)$ and so you can simply do the following operation:

$$
\int_a^b\int_c^df(x,y)dydx=\int_a^bg(x)dx\int_c^dh(y)dy
$$