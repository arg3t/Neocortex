---
title:  Breadth First Search
date: 2022-01-24T02:33:01+01:00
description: 
tags: ['cs/algorithms']
aliases: ['']
---
Breadth first search, or [[/notes/Breadth-First Traversal|Breadth First Traversal]], similar to [[/notes/Depth-First Search|Depth-First Search]] is a traversal algorithm for [[/notes/Graphs|Graphs]]. I works in rounds, by splitting the graph into **levels** strarting from the start node $s$. A visual should be more than enough to explain it:

![[images/Pasted image 20220124151203.png]]

Breadth first search runs in $O(n+m)$ for a graph with $n$ vertices and $m$ edges.