---
title:  Matrix Multiplication
date: 2022-02-26T03:43:30+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
For a [[notes/Matrixes|matrix]] multiplication to be valid, you need two vectors $A$ and $B$ such that $A$ is of size $m \times n$ and $B$ of size $n \times p$ and the multiplication must occur in the order $AB$, and results in a matrix of size $m \times p$. In order to apply the multiplication you use the formula below:

$$
AB = \begin{bmatrix}
Ab_1 & Ab_2 & Ab_3 & ... & Ab_p
\end{bmatrix}

$$

> Matrix multiplication is equivalent to applying two [[notes/Linear Transformations|Linear Transformations]] one after another, this is why the order of multiplication matters
