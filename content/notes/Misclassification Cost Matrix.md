---
title:  Misclassification Cost Matrix
date: 2022-09-25T05:20:41+02:00
description: 
tags: ['cs/ml']
aliases: ['Misclassification Cost Matrix']
---

The [[notes/Misclassification Cost|Misclassification Cost]] for each class can be placed into a matrix of size $C \times C$ where $C$ is the number of classes. In this matrix, a point $(a,b)$ has the value of $\lambda_{a,b}$. This means that the diagonal values in the matrix are always $0$.

$$
\begin{bmatrix}
\lambda_{1,1} & \lambda_{1,2} \\\
\lambda_{2,1} & \lambda_{2,2}
\end{bmatrix}
$$