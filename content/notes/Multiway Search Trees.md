---
title:  Multiway Search Trees
date: 2022-01-03T12:44:50+03:00
description: 
tags: ['cs/data-structures', 'cs/trees']
aliases: ['']
---
Multiway search trees are basically search trees, just like [[/notes/Binary Search Trees|Binary Search Trees]] except that they don't have to be binary trees and each node can have more than one entries. Basically, a multiway tree node can have $n$ entries, which are stored in the node in an ordered manner. A node with $n$ entries can have $n+1$ children. The rule is that, the entries in the kth child needs to be between the values of $k-1$th and $kth$ entriesin the parent. Assuming ofcourse that $k_0=-\infty$ and $k_{n+1}=\infty$
![[images/2C46C726-E7C4-4EED-AF0D-54D754C4D74C.gif]]