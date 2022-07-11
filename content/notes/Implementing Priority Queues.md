---
title: Implementing Priority Queues
date: 2021-12-14T20:32:21+01:00
---
There are two ways to implement [[notes/Priority Queue|Priority Queue]]s:

### Unsorted List
In this method, you insert the elements into the queue in the order that they have been added in. So, insertions take $O(1)$ time. However, removing the element with the highest priority takes $O(n)$ time.

### Sorted List
When adding elements into the queue, you add the element in a way so that the queue remains sorted. This makes the insert operation take more time($O(log_2n)$), but removing the element with the highest priority takes $O(1)$.