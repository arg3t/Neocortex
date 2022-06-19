---
title:  Solution of Non-Homogenous Systems
date: 2022-02-23T12:47:43+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
A [[/notes/Consistent and Inconsistent Systems|consistent]] non-homogenous system $Ax=b$'s solution is $x=x_p + x_h$. In which 

* $x_p$ is a special solution for the homogenous system $Ax=b$
* $x_h$ is the solution for homogenous system $Ax=0$

![[images/9EF24D23-2E2B-468D-8299-3D780C3DE157.jpeg]]

## Proof

Let $Ax = b$ be a non-homogenous system. And let $x_p$ be a solution for $Ax = b$. This means that:

$$
Ax = b
$$
$$
Ax - Ax_p = b - Ax_p
$$
$$
A(x-x_p) = 0
$$