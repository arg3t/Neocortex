---
title: Heap Bubbling
date: 2021-12-14T20:32:21+01:00
---
After inserting an element to a [[notes/Heap|Heap]], sometimes, the heap's **heap-order property** might be broken. In order to fix this, we apply bubbling to that newly inserted element. This operation has three steps:
1. Compare the value of the element with parent's if parent's value is greater (for min-heaps), switch those two nodes.
2. Repeat step 1 until the heap-order proprty is not broken.