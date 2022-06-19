---
title:  Check if a matrix is invertible
date: 2022-02-26T07:32:31+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
A [[/notes/Matrixes|matrix]]($A$) of size $n \times n$ is [[/notes/Inverse Matrix|invertable]] if and only if one of the conditions below hold:

1. $A$ is [[/notes/Equivalent Systems|equivalent]] to $I_n$
2. $A$ has $n$ pivot positions
3. The equation $Ax = 0$ only has the [[/notes/Trivial Solution|Trivial Solution]]
4. The columns of $A$ are linearly independent
5. The equation $Ax = b$ has at least one solution for each $b$ in $\mathbb{R}^n$
6. The column of $A$ [[/notes/Vector Span|span]] $R^n$
7. $A^T$ is invertible as well
8. The columns of $A$ form a [[/notes/Basis Vectors|basis]] for $\mathbb{R}^n$
9. $Col A = \mathbb{R}^n$ ([[/notes/Column Space|Column Space]])
10. $Dim(Col A) = n$ ([[/notes/Dimension|Dimension]])
