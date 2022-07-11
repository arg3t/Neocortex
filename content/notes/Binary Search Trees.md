---
title:  Binary Search Trees
date: 2022-01-01T02:37:16+01:00
description: 
tags: ['cs/data-structures', 'cs/trees']
aliases: ['']
---
Binary search trees are an extension of the [[notes/Binary Tree|Binary Tree]] data structure, except it has two extra constraint:

- A node can have two children, the children with the value less than the node's is placed to the left of it, and the one with a higher value is placed to the right.
- There cannot be two nodes with the same value.

Thanks to these properties, binary search trees allow searching for a node in $O(log(n))$ time. 