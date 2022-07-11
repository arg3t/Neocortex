---
title:  Diagonalization
date: 2022-03-20T08:26:44+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
Diagonalization is a more specific form of [[notes/Similar Matrices|Similar Matrices]], basically, diagonalization is the process of finding a [[notes/Matrixes|matrix]] $D$ that is similar to $A$ and is a diagonal matrix. As well as finding the matrix $P$. This makes it easier to calculate the $k^{th}$ time the matrix $A$ is applied to a vector $v$.

In diagonalization, the matrices $P$ and $D$ are calculated using the [[notes/Eigenvalues|Eigenvalues]]($\lambda_n$) and their coressponding [[notes/Eigenvectors|Eigenvectors]]($w_n$). 

$$
D = \begin{bmatrix}
\lambda_{0} & 0 & 0 & 0 & ... \\
0 & \lambda_{1} & 0 & 0 & ... \\
0 & 0 & \lambda_{2} & 0 & ... \\
0 & 0 & 0 & \lambda_{3} & ... \\
\end{bmatrix} 
$$

$$
P = \begin{bmatrix}
w_0 & w_{2} & w_{3} & w_{4} & ...\\
\end{bmatrix}
$$

Since one of the conditions for diagonability is that there are $n$ [[notes/Linear Indepence and Dependence|linearly independent]] eigenvectors, $P$ **must** be invertible.