---
title: Sentinel Nodes
date: 2021-11-16T21:07:41+01:00
---
Sometimes, when implementing [[notes/Linked List|Linked List]], especially [[notes/Doubly Linked List|Doubly Linked List]], it makes our job much easier to implement sentinel nodes. Sentinel nodes are basicaly *dummy* nodes that are defined with the list, called **header** and **tailer**. By using these dummy nodes, our job is greatly simplified due to several reasons:
* We don't have to implement seperately the `addFirst()` and `addLast()` method since every add operation is made between two nodes,(even in an empty list, nodes are added between **header** and **tailer**).
* The header and tailer nodes remain constant in the list.