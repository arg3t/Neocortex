---
title:  Double Integrals Over General Functions
date: 2022-03-06T08:40:25+01:00
description: 
tags: ['math/calculus']
aliases: ['']
---
Calculating [[notes/Double Integrals Over Rectangles|Double Integrals Over Rectangles]] is nice, but do you know what is nicer? Calculating double integrals over any area. All the cool kids do it these days. Am I too high on caffeine while writing this note? Irrelevant. What is relevant is how you calculate the integral of a [[notes/Multivariable Functions|multivariable function]] over any area $A$. What you do is you split the area into two functions, and the functions you pick actually define how you calculate the integral. There are two possible cases depending on the regions you want to calculate:

## Type 1 Regions
A graph is said to be type 1 if it lies between the graph of two functions of $x$. For a type 1 graph, you write down two functions $g_1(x)$ and $g_2(x)$ which form the region $A$ between the lines $y=a$ and $y=b$. Once you have got these functions, it is simple:

$$
\int_a^b\int_{g_1(x)}^{g_{2(x)}}f(x,y)dxdy
$$

## Type 2 Regions
Type 2 regions are the same as type 1 regions except the functions are of $y$ this time. I won't be explaining this any longer since it is the same idea with type 1 regions so you should be reason and understand it yourself. After all, you are not stupid right? Right?..