---
title:  Selection Sort
date: 2021-12-21T01:45:34+01:00
description: A sorting algorithm based on priority queues
tags: [ 'cs/sorting', 'cs/algorithms']
aliases: ['']
---
Selection sort is a sorting algorithm based on [[/notes/Priority Queue|Priority Queue]]s. In order to sort using selection sort, the items are inserted into a priority queue with their values as keys in the order they are currently at (i.e. not altering the order, meaning each insertion takes $O(1)$ time and $O(n)$ time in total). Afterwards, items are removed from the priority queue, since the order hasn't changed, this operation takes $O(n^2)$.