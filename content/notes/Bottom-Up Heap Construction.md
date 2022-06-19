---
title:  Bottom-Up Heap Construction
date: 2021-12-21T02:25:16+01:00
description: 
tags: [ 'cs/algorithms', 'cs/trees']
aliases: ['']
---
Constructing a heap from scratch by inserting each element into the heap takes $O(nlog(n))$ time. However, when you have a list with $2^n-1$ elements, you can construct a heap with those elements in $O(n)$ time using the following steps.

> The diagrams are for the list `[1,9,10,8,7,2,5,6,3,11,13,4,12,15,16]`

1. Construct $\frac{n+1}{2}$ heaps each with one element 
```mermaid
graph TD
	A((6)) & B((3)) & C((11)) & D((13)) & E((4)) & F((12)) & G((15)) & H((16))
```

2. Construct $\frac{n+1}{4}$ heaps each with three elements
```mermaid
graph TD
	I((8)) --- A((6)) & B((3))
	J((7)) --- C((11)) & D((13))
	K((2)) --- E((4)) & F((12))
	L((5)) --- G((15)) & H((16))
```

3. Apply [[/notes/Down Heap Bubbling|Down-Heap Bubbling]] on each heap.

```mermaid
graph TD
	I((8)) --- A((6)) & B((3))
	J((13)) --- C((11)) & D((7))
	K((12)) --- E((4)) & F((2))
	L((16)) --- G((15)) & H((5))
```
2. Construct $\frac{n+1}{8}$ heaps each with seven elements
```mermaid
graph TD
	M((9)) --- I & J
	N((10)) --- K & L
	I((8)) --- A((6)) & B((3))
	J((13)) --- C((11)) & D((7))
	K((12)) --- E((4)) & F((2))
	L((16)) --- G((15)) & H((5))
```

3. Apply [[/notes/Down Heap Bubbling|Down-Heap Bubbling]] on each heap.

```mermaid
graph TD
	M((13)) --- I & J
	N((16)) --- K & L
	I((8)) --- A((6)) & B((3))
	J((11)) --- C((9)) & D((7))
	K((12)) --- E((4)) & F((2))
	L((15)) --- G((10)) & H((5))
```
4. Finally, add the last element in the list and apply [[/notes/Down Heap Bubbling|Down-Heap Bubbling]] one final time.
```mermaid
graph TD
	O((16)) --- M & N
	M((13)) --- I & J
	N((15)) --- K & L
	I((8)) --- A((6)) & B((3))
	J((11)) --- C((9)) & D((7))
	K((12)) --- E((4)) & F((2))
	L((10)) --- G((1)) & H((5))
```