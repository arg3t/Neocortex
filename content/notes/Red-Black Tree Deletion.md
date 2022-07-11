---
title:  Red-Black Tree Deletion
date: 2022-01-05T08:43:21+03:00
description: 
tags: ['cs/trees', 'cs/data-structures', 'cs/algorithms']
aliases: ['']
---
After deleting from the [[notes/Red-Black Trees|Red-Black Trees]] just like a [[notes/Deleting  From A Binary Search Tree|BST]], the promoted node is colored black. However, this might break the black-depth property of the tree. 

## The Sibling of new node's parent(y) is black and has a red child(x)
A [[notes/Binary Tree Restructuring|trinode restructuring]] on x is performed and then a and c is colored black while b is given the color of the original node that were there before.

## The Sibling of new node's parent(y) is black and has two black children
In this case a recoloring is performed so that y is colored red and y's parent is colored black. However, this recoloring might still break the black depth property for y's parent so mode recoloring is necessary traversing up the tree.

## The sibling of node's parent(y) is red
In this case a [[notes/Binary Tree Rotations|rotation]] about y is done. After this rotation, either case 1 or case 2 would apply and this tree can be continued to be fixed from there.

