---
title:  Linear Indepence and Dependence
date: 2022-02-23T01:07:48+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
A set of vectors are linearly dependent if:

$$
\begin{bmatrix}
v_1 & v_2 & v_3 & ... & v_n
\end{bmatrix} x = 0
$$

only has the [[/notes/Trivial Solution|Trivial Solution]] as a solution. 

It can also be said that the set is linearly dependent if a vector in the set is a linear combination of one or more vectors in the set.

Linear dependency is also present if given a set of vectors ${v_1, v_2, ..., v_n}$, the equation $c_1v_1 + c_2v_2 + ... + c_nv_n = 0$ can be satisfied where not all the constants are 0.

> If there are more than $n$ vectors in the set, each of which of size $\mathbb{R}^n$ cannot be linearly independent.

> If the zero vector is in the set, it is linearly dependent