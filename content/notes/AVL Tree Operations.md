---
title:  AVL Tree Operations
date: 2022-01-02T10:46:07+03:00
description: 
tags: ['cs/data-structures', 'cs/algorithms', 'cs/trees']
aliases: ['']
---
## Insertion
After inserting into an AVL Tree, which works just like a [[notes/Binary Tree|Binary Tree]], we insert the node into the tree, we traverse upwards from the inserted node, checking if the AVL property is broken at any point in the tree. If that is the case, we apply [[notes/Binary Tree Restructuring|trinode restructuring]] and that is enough to fix the AVL property for this subtree and all the ancestors of that node.

## Deletion
Again, deletion works just like [[notes/Deleting  From A Binary Search Tree|deletion from a BST]],  once it is done, we again move upwards from the node checking if AVL property is broken, and fix any nodes that break it. In this case, one restructuring is not enough, we need to traverse until the root of the tree.