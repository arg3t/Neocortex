---
title:  Inverse Matrix
date: 2022-02-26T07:24:28+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
Inverse [[notes/Matrixes|Matrixes]] are basically [[notes/Linear Transformations|Linear Transformations]] that can reverse the effects of a matrix. Finding the inverse of a matrix is done through this method:

1. An augmented matrix of type $\begin{bmatrix} A & | & I_n \end{bmatrix}$, where $I_n$ is an [[notes/Special Matrices#^81da11|identity matrix]] of size $n \times n$.
2. If $A$ is invertible, than you can use [[notes/Elementary Row Operations|Elementary Row Operations]] in order to reduce the augmented matrix so that it is in the form $\begin{bmatrix} I_n & | & A^{-1} \end{bmatrix}$ 
