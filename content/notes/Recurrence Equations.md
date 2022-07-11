---
title:  Recurrence Equations
date: 2021-12-21T08:19:31+03:00
description: 
tags: ['math/recursion']
aliases: ['']
---
A recursive function is a function that uses itself in its definition. An example of such a function is:

$$
f(x) : \mathbb{Z^+} + \{0\} \implies \mathbb{Q}
$$
$$
f(x) = \begin{cases}
x = 0, & 1\\
x > 0, & \frac{f(x-1)}{2}
\end{cases}
$$

This function constantly makes a recursive call to itself until the value x becomes less than 0, then it hits the **base case** and returns 2. Creating a [[notes/Closed Form Equation|Closed Form Equation]] from recurrence equations is a trivial task, Basically, you need to write out the function for several steps. For instance:
- [ ] Closed form equation link

$$
f(x) = \frac{f(x-1)}{2}
= \frac{f(x-2)}{4}
= \frac{f(x-3)}{8}
= \frac{f(x-n)}{2^n}
$$

Since this recursion will continue until x is less than or equal to 0, we can write this function as:

$$
f(x) = \frac{1}{2^x}
$$
