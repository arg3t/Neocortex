---
title:  Conditional And Total Risk
date: 2022-09-25T05:09:37+02:00
description: 
tags: ['cs/ml', 'math/stats']
aliases: ['Conditional And Total Risk']
---

The conditional risk of assigning an object $x$ to the class $\omega_i$ is ( given the [[notes/Misclassification Cost|missclassification costs]]):
$$
l^i(x) = \sum_{j=1}^C \lambda_{j,i}p(\omega_j|x)
$$
This means the average risk(expectation) over a region $\Omega_i$ is:
$$
$$
$$
\begin{align*}
r^i &= \int_{\Omega_i} l^i(x)p(x)dx \\
 &= \int_{\Omega_i} \sum_{j=1}^C \lambda_{j,i}p(\omega_j|x)p(x)dx
\end{align*}
$$

And the overall risk  becomes:

$$
\begin{align*}
r &= \sum_{i=1}^C r^i \\
 &= \sum_{i=1}^C\int_{\Omega_i} l^i(x)p(x)dx \\
 &= \sum_{i=1}^C\int_{\Omega_i} \sum_{j=1}^C \lambda_{j,i}p(\omega_j|x)p(x)dx
\end{align*}
$$

> [!note] Classification
> The main purpose of classification algorithms is to choose the regions $\Omega_i$ so that each of those integrals is minimal.
