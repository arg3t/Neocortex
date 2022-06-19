---
title:  Depth-First Search
date: 2022-01-24T02:15:36+01:00
description: 
tags: ['cs/algorithms']
aliases: ['']
---
Depth first search is a traversal algorithm for [[/notes/Graphs|Graphs]]. In DFS, edges are explored until we hit a dead-end where we can go to an unvisited vertice and we backtrack until the last decision point after that. Here is pseudocode for DSF:

```
DFS(G, v):
	v.color()
	for(u in G.getNeighbours(v))
		if(!u.isColored)
			record edge (v,u) as u's discovery edge
			DFS(G,u)
```


DFS runs in $O(n_s+m_s)$ time where $n_s$ and $m_s$ are the number of vertices and edges reachable from the start vertice $s$, respectively. However, for this to hold, two conditions must be satisfied:

* We must be able to access the outgoing edges of a vertice in at least $O(deg(v))$ time.
* We must be able to mark a vertice as visited in $O(1)$ time.

> IMPORTANT: When running DFS, you are not guaranteed to find the shortest path between two nodes, you can only check whether there is a path.