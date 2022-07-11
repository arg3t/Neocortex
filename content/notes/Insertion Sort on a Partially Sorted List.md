---
title:  Insertion Sort on a Partially Sorted List
date: 2021-12-21T02:14:06+01:00
description: 
tags: [ 'cs/algorithms', 'cs/sorting']
aliases: ['']
---
When you have a partially sorted list, you can change the definition of the [[notes/Priority Queue|Priority Queue]] you use in [[notes/Insertion Sort|Insertion Sort]] so that the new elements are first added to the end of the queue. This way, the algorithm's time complexity changes to $O(n+I)$ where $I$ is the number of inversions[^1] in a list.

[^1]: A pair of elements in the list that start out in the wong relative order.