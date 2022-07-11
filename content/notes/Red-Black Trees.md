---
title:  Red-Black Trees
date: 2022-01-04T01:37:37+03:00
description: 
tags: ['cs/data-structures', 'cs/trees']
aliases: ['']
---
Red-Black trees are a type of [[notes/Binary Search Trees|Binary Search Trees]] which aim to keep the tree balanced by adding an extra property into each node, whether it is red or black and enforcing a set of properties:

- **Root Property:**  The root of red-black tree is black
- **External Property:** Every external node is black
- **Red Property:** The children of a red node are black
- **Depth Property:** The black depth(i.e. The number of proper ancestors that are black) of each external node is the same.
