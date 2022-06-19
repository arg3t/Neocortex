---
title:  Dijkstra's Algorithm
date: 2022-01-24T03:37:49+01:00
description: 
tags: ['cs/data-structures']
aliases: ['']
---

Dijkstra's algorithm uses a [[/notes/Greedy Method|Greedy Method]] design pattern to find the shortest path from a start vertice $s$ to an end vertice $e$ in a directed and weigthed [[/notes/Graphs|graph]]. If the graph weren't weighted, we could simply use [[/notes/Breadth First Search|Breadth First Search]].

In Dijkstra' algorithm, a Cluster of vertices, $C$, a [[/notes/Priority Queue|Priority Queue]] (pq) and a [[/notes/Maps|map]] of $V \to distance$ (D) is used. In the start, each vertice is assigned a distance of $\infty$ except the start node, which is given a distance of $0$. The nodes are saved to pq using their distances as keys. Afterwards, the following algorithm is ran:

```
while(!pq.isEmpty())
	v = pq.removeMin()
	if D[v] == infty
		break
	for u in v.getOutgoing():
		if D[u] > D[v] + weight(v,u):
			D[u] = D[v] + weight(v,u)
			pq.update(u, D[u]) // This part requires an Adaptable Priority queue, i.e. the keys can be updated
```

Dijkstra runs in $O((n+m)logn)$ time or $O(n^2logn)$ time. Where n is the number of nodes and m is the number of edges.