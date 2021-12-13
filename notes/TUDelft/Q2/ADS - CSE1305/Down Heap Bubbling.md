---
title: Down-Heap Bubbling
date: 2021-12-13
---
## Down-Heap Bubbling
Down-Heap bubbling is basically the reverse of [[Up-Heap Bubbling]],  when the **heap-order property** of a heap is broken due to a node that is not a leaf, you need to apply down-heap bubbling. It has two steps:
1. Compare the node with both its children, if it is greater than either of its children(for a min heap),switch it with the smallest of its children.
2. Repeat step 1 until the property is restored.