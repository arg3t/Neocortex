---
title: Projection $\pi$
date: 2021-12-14T20:32:21+01:00
---
## Projection $\pi$
When normalizing a database that has a redundancy problem, it is often a good idea to split up a single table into multiple tables. In order to this we use the technique called projection. When projecting a database, we *decompose* a relation into multiple relations. If you let $\alpha_1, \alpha_2,..., \alpha_n \subseteq \{A_1, ..., A_3\}$ be n subsets of a relation $R$'s attributes, we can define a new $R_i$ for any $\alpha_i$ such that:

$$R_i = \pi_{\alpha_i}R$$

In this case, $\alpha_1, \alpha_2,..., \alpha_n$ is a decomposition of the relation R. For this decomposition to be good, it needs to be lossless, meaning that the joining of all those projections ($R_1 \bowtie R_2 ... \bowtie R_n$) must be equal to R.