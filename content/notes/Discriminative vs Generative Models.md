---
title:  Discriminative vs Generative Models
date: 2022-09-25T05:34:41+02:00
description: 
tags: ['cs/ml']
aliases: ['Discriminative vs Generative Models']
---

There are two approaches to [[notes/Classification|classification]], *discriminative* and *generative* models. 

## Discriminative Models
Discrimintive models aim to classify objects by just knowing the [[notes/Posterior Probability]]. The hard problem that needs to be solved is how we can calculate those probabilities, and to solve it, we need to make **strong** assumptions.

## Generative Models
Generative models aim to calculate the posterior probability by knowing the [[notes/Classification|Class Prior]] and the conditional density($p(x|\omega)$). Using the principle:
$$
p(\omega|x) \propto p(\omega)p(x|\omega)
$$
It requires the class prior and the conditional density to be estimated.