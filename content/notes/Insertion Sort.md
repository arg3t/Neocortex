---
title:  Insertion Sort
date: 2021-12-21T01:51:28+01:00
description: 
tags: [ 'cs/sorting', 'cs/algorithms']
aliases: ['']
---
Insertion sort, is an algorithm based on [[notes/Priority Queue|Priority Queue]]s. In insertion sort, you insert the elements that you want to sort into the priority queue in a **sorted** order. This operation takes $O(n)$ time for each insertsion(unless a [[notes/Heap|Heap]] is used), and removing elements takes $O(1)$ time(again, unless the queue is implemented with a heap). In total, the big-oh complexity of this algorithm is $O(n^2)$

![Image](images/DA3CF7B7-6332-41BA-86A5-34817A00DA6C.png)