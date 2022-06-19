---
title:  Real Matrixes with Complex Eigenvalues
date: 2022-03-20T10:23:19+01:00
description: 
tags: ['math/linear']
aliases: ['']
---

Given a $2 \times 2$ [[/notes/Matrixes|matrix]] in the form:

$$
A = \begin{bmatrix}
a & -b \\
b & a
\end{bmatrix}
$$

> This is a [[/notes/Rotational Transformations|rotational transformation]]


Then $A$ has the eigenvalues $\lambda_{\pm}= a \pm bi$ and can be represented by the [[/notes/Euler's Identity|Euler's Identity]] of

$$
a + bi = re^{i\phi}
$$

$$
A = r\begin{bmatrix}
cos \phi & -sin \phi \\
sin \phi & cos \phi
\end{bmatrix}
$$

Diagonalizing the matrix $B$, which has the eigenvalues : $a \pm bi$ is calculated using the method below:

$$
B = P\begin{bmatrix}
a & -b \\
b & a
\end{bmatrix}
P^{-1}
$$

$$
P = \begin{bmatrix}
Re(\mathbf{v}) & Im(\mathbf{v})
\end{bmatrix}
$$

where $\mathbb{v}$ is the eigenvector for $a - bi$