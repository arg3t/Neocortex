---
title:  Balanced Binary Search Trees
date: 2022-01-01T03:12:26+01:00
description: 
tags: ['cs/data-structures', 'cs/trees']
aliases: ['']
---
How a [[/notes/Binary Search Trees|BST]] performs depends largely on how well balanced it is. If a tree has mostly linear structure, then its worst-case time complexity for searching becomes $O(n)$ instead of $O(log(n))$. In order to balance a tree, [[/notes/Binary Tree Rotations|rotations]] are crucial.