---
title:  Bucket Sort
date: 2021-12-24T04:18:32+01:00
description: 
tags: ['cs/sorting', 'cs/algorithms']
aliases: ['']
---
Bucket sort is a non-comparison based sorting algorithm. It has the restriction that the integers in a list are in the range $[0, N]$. In order to sort the list, a list of $N+1$ elements are generated and each elements' value is used as an index into the array and the value of that index in the array is incremented. Once each element in the original array is visited, the counter array is then used to create a new, sorted array. This approach has the [[/notes/Big-Oh Notation|time complexity]] of $O(n)$ and space complexity of $O(n)$ as well.