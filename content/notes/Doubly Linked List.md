---
title: Doubly Linked List
date: 2021-11-16T21:07:41+01:00
tags: [ 'cs/data-structures', 'cs/lists']
---
Doubly linked list are very similar to [[/notes/Linked List|Linked List]] except that instead of having one pointer at each node, which points to the next node, each node has two pointers: one pointing to the next node and the other pointing to the previous node. The big-Oh notations for each operation remains the same. Except the operation of removing the tail node, since you can update the reference to the tail node, removing the tail takes $O(1)$ time.