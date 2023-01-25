---
title:  Exchange Argument
date: 2023-01-25T01:41:10+01:00
description: 
tags: ['cs/algorithms']
aliases: ['Exchange Argument']
---

The exchange argument is a proof method used to prove the optimality of [[notes/Greedy Algorithm|Greedy Algorithms]]. The proof is based on the idea that given an optimal solution with inversions, commpared to the the greedy solution, fixing those inversions brings the optimal solution closer to the greedy solution whilst preserving optimality.

> [!WARNING]
> For two elements in the wrong order compared to the greedy solution to be considered an inversion, they need to be next  to each other.

## A basic skeleton
1. Let the solution produced by our greedy algorithm be $S$ 
2. Let $\mathscr{O}$  be the optimal solution with the least amount of inversions.
3. Assume that greedy does not produce optimal solutions.
4. Define what an inversion is, show that by definition $S$ cannot have any inversions.
5. From here, we have two cases:
	1. $\mathscr{O}$ does not have any inversions, this immediately contradicts with our statement at step 3.
	2. $\mathscr{O}$ has at least one inversion. This impliest that there two points $(o_i, o_{i+1})$ that are inverted. It is best to start this part with *"Consider a solution..."*
		1. Show that swapping the inverted elements preserves the optimality of the solution.
		2. Show that swapping the two points removes the inversion
		3. Show that swapping the two points does not introduce any new inversions.
		4. State that this creates a new solution $\mathscr{O}'$ that is still optimal and yet has less number of inversions than $\mathscr{O}$. 
		5. This means $\mathscr{O}$ is not the optimal solution with the least number of inversions, contradicting step 2.
		6. By reducing the number of inversions we brough $\mathscr{O}'$ closer to $S$ while preserving the optimality. This contradicts with step 3. 
		7. Thus, the solution $S$ is optimal
