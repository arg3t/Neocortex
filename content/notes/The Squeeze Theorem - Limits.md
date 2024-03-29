---
title: The Squeeze Theorem
date: 2021-11-24T18:41:59+01:00
tags: ['cs/calculus']
---
When you take three funtions $f(x)$, $g(x)$ and $h(x)$ such that $f(x) \le g(x) \le h(x)$, but you can't calculate the limit of the function $g(x)$ at a value
$c$, you can simply calculate $\lim_{x\to c} f(x)$ and $\lim_{x\to c} h(x)$.
The value of $\lim_{x\to c} g(x)$ must be between those values and if they are
equal, then it must equal to that value as well. This method is particularly
useful when dealing with the limits of periodical functions such as
[[notes/Trigonometric Functions|Trigonometric Functions]], for instance, when calculating $\lim_{x\to 1}$ for
$g(x) = x^2sin(\frac{\pi}{x})$ . Since the range of the sine function is $-1
\le sin(x) \le 1$, we can take $f(x) = -x^2$ and $g(x) = x^2$. Now, calculating
the limit of both these we functions as x approaches 0, we find that they both
equal 0, therefore the answer is 0.
