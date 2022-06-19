---
title:  Deleting  From A Binary Search Tree
date: 2022-01-01T03:08:29+01:00
description: 
tags: ['cs/algorithms', 'cs/data-structures', 'cs/trees']
aliases: ['']
---
Deleting from a [[/notes/Binary Search Trees|binary search tree]] can be a tricky process since we want to sustain the BST property of the tree upon deletion. We can split the deletion of a node into three cases depending on how many children that node has.

##  No Children
Just remove the node.

## One Child
Replace the node with its child.

## Two children
In this case, you have two choices:

- Replace the node we want to delete with the maximum node in the left subtree
- Replace it with the minimum node in the right subtree.

All these operations can be done in $O(log(n))$ time.