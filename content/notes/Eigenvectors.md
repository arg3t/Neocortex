---
title:  Eigenvectors
date: 2022-03-20T06:03:22+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
Eigenvectors are [[notes/Vectors|Vectors]] which remain in the same span when a [[notes/Linear Transformations|linear transformation]] $A$ is applied to them. However, they can be scaled up or down. An eigenvector is represented algebraically as:

$$
Ax = \lambda I x
$$

where $I$ is the [[notes/Special Matrices#^81da11|identity matrix]]. This can also be rewritten as:

$$
(A - \lambda I)x = 0
$$

This linear system can have $1$ or $\infty$ solutions, since the $0$ vector is always a solution to the system(because of the [[notes/Linear Transformations#^81460d|0 property of linear transformations]]).

The $\lambda$ here is called the [[notes/Eigenvalues|eigenvalue]] of the eigenvector $x$.
