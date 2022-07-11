---
title: Tree Traversal
date: 2021-12-14T20:32:21+01:00
---
[[notes/Tree|Tree]] Traversal is the process of visiting/processing every node in a tree using a consistent method. Every traversal algorithm, has a time complexity in [[notes/Big-Oh Notation|Big-Oh Notation]] $O(n)$ where n is the number of nodes in the tree. There are two types of three traversal methods:

* **Depth First:** In this method, we go down each subtree of a node before visiting other nodes, so the nodes at lower heights aren't necessarily prioritized. There are two algorithms for this:
	* [[notes/Pre-Order Traversal|Pre-Order Tree Traversal]]
	* [[notes/Post-Order Traversal|Post-Order Tree Traversal]]
* [[notes/Breadth-First Traversal|Breadth First Traversal]].