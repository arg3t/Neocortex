---
title:  Similar Matrices
date: 2022-03-20T08:15:27+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
Two [[/notes/Matrixes|matrices]] $A$ and $B$ are said to be similar if there exists an invertable matrix $P$ such that:

$$
A = PBP^{-1}
$$

When you have such similar matrices and you know that $v$ is an [[/notes/Eigenvectors|eigenvector]] of $B$, $Pv$ must be an eigenvector of $A$ with the same [[/notes/Eigenvalues|eigenvalue]].

$$
A(Pv) = PBP^{-1}Pv = PBv = P\lambda v = \lambda Pv
$$

Building from the definition of the eigenvalues, it is clear that $Pv$ is an eigenvector of $A$ with eigenvalue $\lambda$.