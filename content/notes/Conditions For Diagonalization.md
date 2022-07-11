---
title:  Conditions For Diagonalization
date: 2022-03-20T08:31:52+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
To check if a [[notes/Matrixes|matrix]] is [[notes/Diagonalization|diagonalizable]], there are two conditions:

- For an $n \times n$ matrix, the matrix must have $n$ [[notes/Linear Indepence and Dependence|linearly independent]] [[notes/Eigenvectors|Eigenvectors]]
	- This is always true if $A$ has $n$ distinct [[notes/Eigenvalues|Eigenvalues]]
	
- More generally, $a.m.(\lambda) = g.m.(\lambda)$ for all eigenvalues of $A$.
	- As a proof, think about this, $g.m(\lambda)$ tells us how many linearly independent eigenvectors exist for an eigenvalue $\lambda$ (due to the definition of [[notes/Dimension|Dimension]]). Moreover, since the sum of all the algebraic multiplicities must equal $n$, it is clear that when the algebraic multiplicity is equal to geometric multiplicity for all eigenvalues, we have $n$ linearly independent eigenvectors.
