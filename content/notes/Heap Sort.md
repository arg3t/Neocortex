---
title:  Heap Sort
date: 2021-12-21T02:54:31+01:00
description: 
tags: [ 'cs/sorting', 'cs/algorithms']
aliases: ['']
---
Heap sort is a faster version of [[notes/Insertion Sort|Insertion Sort]], optimised by implementing a [[notes/Heap|Heap]] into the [[notes/Priority Queue|Priority Queue]] so that the insertion and removal stages take $O(nlog(n))$ time. The insertion stage can be altered to have an $O(n)$ complexity by using [[notes/Bottom-Up Heap Construction|Bottom-Up Heap Construction]]. The $O(nlog(n))$ time complexity is much more efficient than the $O(n^2)$ for insertion and selection sort ([[notes/7 Important Functions|7 Important Functions]]).