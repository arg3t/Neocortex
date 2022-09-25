---
title:  Empirical Risk
date: 2022-09-25T04:13:33+02:00
description: 
tags: ['cs/ml']
aliases: ['Empirical Risk']
---

When you [[notes/Classification|classify]] the points in the dataset as $D = \{(x_i, \omega_i)\}_{i=1}^N$ and you assign each of the points to a class $\hat{\omega_i}$. Then the total empirical risk on the dataset, given the [[notes/Misclassification Cost|misclassification cost]] of each class is:

$$
R = \frac{1}{N}\sum_{i=1}^N \lambda_{\omega_i, \hat{\omega_i}}
$$