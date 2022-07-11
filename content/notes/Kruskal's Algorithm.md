---
title:  Kruskal's Algorithm
date: 2022-01-24T04:28:32+01:00
description: 
tags: ['cs/algorithms']
aliases: ['']
---
In order to create the minimum spanning tree of a [[notes/Graphs|graph]], the kruskal's algorithm takes the following approach:

- Save each of the edges into a priority queue
- Create $n$ clusters, each containing one of the vertices.
- Remove the minimum entry from the priority queue.
- If the nodes connected by the edge do not belong to the same cluster, we merge the two clusters. Add the removed edge to the tree.
- repeat

Kruskal's algoritm runs in $O(mlogn)$ time. Where $m$ is the number of edges while $n$ is the number of vertices.
