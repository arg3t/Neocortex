---
title:  Classification Error
date: 2022-09-25T04:01:13+02:00
description: 
tags: ['cs/ml']
aliases: ['Classification Error']
---

The [[notes/Classification|classification]] error is the overall error we make with a given model for a given dataset. It is calculated using the formula:

$$
p(error) = \sum_{i=1}^C p(error|\omega_i)p(\omega_i)
$$
This can better be visualized by integrating the area under the distribution of two classes that are to opposing sides of the [[notes/Decision Boundaries|decision boundary]]:

![[images/Pasted image 20220925160454.png]]