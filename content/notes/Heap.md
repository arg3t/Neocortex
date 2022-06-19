---
title: Heap
date: 2021-12-14T20:32:21+01:00
tags: ['cs/data-structures', 'cs/trees']
---
A heap is basically a [[/notes/Binary Tree|Binary Tree]] which is complete([[/notes/Full & Complete Trees|Full vs Complete Binary Trees]]) and every child of a parent node ([[/notes/Tree Terminology|Important Tree Terminology]]) has a value greater than or equal to the parent's value. 

## Analysis of a min-heap
|operation|[[/notes/Big-Oh Notation|Big-Oh Notation]]|
|----------|------------------|
|size|$O(1)$|
|min|$O(1)$|
|insert|$O(log(n))$|
|removeMin|$O(log(n))$|