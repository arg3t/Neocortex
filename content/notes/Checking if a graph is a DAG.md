---
title:  Checking if a graph is a DAG
date: 2022-01-24T03:34:06+01:00
description: 
tags: ['cs/algorithms']
aliases: ['']
---
Checking whether a [[notes/Graphs|graph]] is a [[notes/Directed Acyclic Graphs|Directed Acyclic Graphs]] is a trivial problem. First off, we need to know that for a graph to be a DAG, there must exit at least one vertice with $0$ incoming edges, otherwise, it cannot be a DAG(go figure out why yourself, you nitwit). After accepting the proposition, it is easy to find the topological ordering of the graph using the following algorithm:

```
pick a vertice with 0 incoming edges
if none exists:
	not a DAG
append the vertice to the topological order of the graph
remove the vertice from the graph
repeat until graph is empty
```

