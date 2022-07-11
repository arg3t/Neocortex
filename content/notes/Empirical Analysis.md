---
title: Empirical Analysis
date: 2021-11-16T21:07:41+01:00
tags: ['cs/algorithms', 'cs/analysis'] 
---
Empirical analysis is the process of running an algorithm with different input sizes and plotting/analyzin the change in input times overtime.

## Drawbacks of empirical analysis
- Runtime differs between different hardware, not just between different hardware but between different runs.
- Does not cover all inputs, thus the inputs not tested are not covered by the empirical analysis.
- An algorithm must be fully implemented in order to test it, but we only want to implement the fastest algorithm.

Instead of doing empirical analysis, it is a good idea to first calculate the [[notes/Big-Oh Notation|Big-Oh Complexity]]