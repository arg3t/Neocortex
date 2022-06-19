---
title:  Edge List
date: 2022-01-23T02:59:28+01:00
description: 
tags: ['cs/data-structures']
aliases: ['']
---

The edge list structure basically holds a list of all the edges in a [[/notes/Graphs|graph]] as well as a list of all the vertices. It is a simple yet effective way to store a graph. Since we store vertices and edges, it takes $O(n+m)$ space.^[1]:

| **Method** | **Running Time** |
|---------------|-------------------|
| numVertices(), numEdges() | $O(1)$ |
| vertices() | $O(n)$ |
| edges() | $O(m)$ |
| getEdge(u,v), outDegree(v), inDegree(v) | $O(m)$ |
| insertVertex(x), insertEdge(u, v, x), removeEdge(e)| $O(1)$ |
| removeVertex(v)| $O(m)$ |



[1]: n is the number of vertices, m is the number of edges