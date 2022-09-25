---
title:  Errors in a more general sense
date: 2022-09-25T03:55:16+02:00
description: 
tags: ['cs/ml', 'math/stats']
aliases: ['Errors in a more general sense']
---

For a two-type [[notes/Classification|classification]] problem: There are two different types of errors: $\varepsilon_1$ and $\varepsilon_2$. You can calculate them like so:
- **[[notes/Types of Errors|Type I Error]]**: $\int_{\Omega_2} p(x|\omega_1)dx$
- **[[notes/Types of Errors|Type II Error]]**: $\int_{\Omega_1} p(x|\omega_2)dx$

If you call $\omega_2$ the positive group and $\omega_1$ the negative group. Type I becomes false negative and Type II becomes false positive.