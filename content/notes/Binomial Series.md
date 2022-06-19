---
title:  Binomial Series
date: 2022-01-19T09:35:50+01:00
description: 
tags: ['math/analysis', 'math/calculus']
aliases: ['']
---
Binomial series are a special type of [[/notes/Power Series|Power Series]] which are used to describe functions of the form $(a+x)^r$. Even though a power series can be calculated for every single form of this function, it is often easier to calculate the power series of $(1-x)^r$ which is 

$$
\sum \binom{r}{n} x^n
$$

> Here, we use a [[/notes/Binomial Coefficient|Binomial Coefficient]]. 

After knowing the power series for $(1-x)^r$, we can [[/notes/Power Series As Functions|treat it as a function]] and derive any function in the form $(a+x)^r$.

