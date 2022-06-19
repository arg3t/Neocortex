---
title:  Important Properties of a Graph
date: 2022-01-23T09:42:20+01:00
description: 
tags: ['cs/data-structures']
aliases: ['']
---

Let $G$ be a [[/notes/Graphs|graph]] with $m$ edges in its edge set $E$ and $n$ vertices in its vertex set $V$:

$$
\sum_{v in V}deg(v) = 2m
$$

If G is directed:

$$
\sum_{v in V}outdeg(v) = \sum_{v in V}indeg(v) = m
$$

* If G is [[/notes/Graph Terminology#^42fbff|connected]],  $m \geq n-1$
* If G is [[/notes/Graph Terminology#^78100b|a tree]],  $m = n-1$
* If G is [[/notes/Graph Terminology#^d6fb26|a forest]],  $m \leq n-1$

If G is a simple graph with $n$ vertices, the number of edges is $O(n^2)$.
