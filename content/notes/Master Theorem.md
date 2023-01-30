---
title:  Master Theorem
date: 2023-01-29T10:26:11+01:00
description: 
tags: [cs/algorithms]
aliases: ['Master Theorem']
---

The master theorem is used to calculate the [[notes/Big-Oh Notation|Big-Oh Complexity]] of [[notes/Recurrence Equations|recurrence equations]] of the form:

$$
T(n) = aT(\frac{n}{b}) + f(n)
$$

Where $a \geq 1$ and $b \geq 1$ and  $f(n)$ is an [[notes/Vertical Asymptotes|asymptotically]] positive function.

> [!note] 
> It is important to note that $\frac{n}{b}$ is not always an integer. This is why it is usually in form $\lceil \frac{n}{b} \rceil$ ([[notes/The floor and ceil functions|the ceil function]]). For notational ease, we will be using the notation without brackets in this note.



It can be used on three cases:
1. $f(n)= O(n^{log_b{a-\epsilon}})$  ([[notes/Big-Oh Notation]]), where $\epsilon > 0$. $T(n) = \Theta(n^{log_ba})$
2. $f(n)= \Theta(n^{log_b{a}})$  ([[notes/Big-Theta Notation]]), then  $T(n) = \Theta(n^{log_ba}log n)$
3. $f(n)= \Omega(n^{log_b{a-\epsilon}})$  ([[notes/Big-Omega Notation]]), where $\epsilon > 0$. $T(n) = \Theta(f(n))$