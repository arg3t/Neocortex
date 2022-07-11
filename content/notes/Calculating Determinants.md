---
title:  Calculating Determinants
date: 2022-03-06T10:45:50+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
Calculating [[notes/Determinant|determinants]] with the concept of [[notes/Cofactor|cofactor]] is relatively straight forward. Given an $n \times m$ matrix $A$, the determinant is defined by one of the following formulas:

$$
\forall k \leq m : det(A) = \sum_{i=0}^n -1^{i+k}a_{ik}C_{ik}
$$

$$
\forall k \leq n : det(A) = \sum_{i=0}^m -1^{i+k}a_{ki}C_{ki}
$$

> Notice that to calculate the determinant, we can pick any row/column we want, so it is best to pick one with **as many zeros as possible**.

## Properties of Determinants
- $det(A^T) = det(A)$
- $det(AB) = det(A)det(B)$
- $det(A^{-1}) = det(\frac{1}{A})$