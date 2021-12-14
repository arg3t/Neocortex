---
title: Functional Dependencies
date: 2021-12-13
---
## Functional Dependencies
If you have two sets of attributes, call them $X$ and $Y$, id $Y$ functionally depends on $X$, then two tuples which agree on their $X$ values must also agree on their $Y$ values. A functional dependency(denoted using  $X\to Y$) in subsets $X,Y\subseteq{A_1,...,A_n}$  means that for two arbitrary tuples $t_1$ and $t_2$:
$$\pi_Xt_1 = \pi_Xt_2 \iff \pi_Yt_1 = \pi_Yt_2$$
> If you don't understand the notation, review [[Projection]]
> In plain english, this means that if the tuples have the same values for the attributes in X, they must also have the same values for Y.

> X->Y means that: 
> X *functionally determines* Y
> Y *functionally depends on* X
> X is the determinant and Y is the dependant in this relationship

Since functional dependencies are semantic(i.e. they depend on the real world knowledge), they are determined by the engineer of the schema and are manualy defined [[Integrity Constraints]].

> When you have the functional dependency X->Y in the relation R, X is a [[Super Key]] in R.