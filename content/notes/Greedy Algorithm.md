---
title:  Greedy Algorithm
date: 2023-01-25T01:03:11+01:00
description: 
tags: ['cs/algorithms']
aliases: ['Greedy Algorithm']
---

A greedy algorithm([[notes/Greedy Method|Greedy Method]]) is an algorithmic approach that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. It iteratively makes one greedy choice after another, reducing each given problem into a smaller one. At each step, it makes a decision that seems to be the best at that moment, without considering the consequences for the future steps.

Usually, a greedy algorithm consists of 2 steps

1. Sorting the provided data according to a chosen heuristic, this heuristic is differnt for each problem.
2. Create a solution using the sorted array and some extra heuristics.

Even though in some cases they do not result in optimal solutions, it can be proven that they always find the optimal solution  To prove the optimality of greedy algorithms, there are two methods:

- [[notes/Greedy Stays Ahead|Greedy Stays Ahead]]
- [[notes/Exchange Argument|Exchange Argument]]



