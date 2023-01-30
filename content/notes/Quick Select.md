---
title:  Quick Select
date: 2021-12-27T01:17:19+03:00
description: 
tags: ['cs/algorithms']
aliases: ['']
---
Quick Select is an algorithm similar to [[notes/Quick Sort|Quick Sort]], except it does not sort a given but finds the nth smallest element in an array in $O(n)$ time. However, this algorithm has a [[notes/Big-Theta Notation|worst case time complexity]] of $O(n^2)$ since the recursion tree can be imbalanced. Here is the pseudocode for a function that finds the kth smallest element in an array A:

```java
QuickSelect(n, k):
	Populate L, E, G arrays according to a randomly chosen pivot
	if len(L) >= k:
		return QuickSelect(L,k)
	else if len(L) + len(E) >= k:
		return E[0]
	else:
		return QuickSelect(G,k - (len(L)+len(E))
```