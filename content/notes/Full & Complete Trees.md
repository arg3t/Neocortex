---
title: Full vs Complete Binary Trees
date: 2021-12-14T20:32:21+01:00
tags: [ 'cs/trees', 'cs/data-structures']
---
* In a *full*/*complete* [[/notes/Binary Tree|Binary Tree]], every node has two children, except the leaf nodes.
* In a *complete* binary tree however, every level has the maximum number of nodes it can have. The last layer is exempted from this condition. If there are missing leaf nodes, they all have to be on the right.

### A Full Binary Tree
```mermaid
graph TD;
	A(( ))-->B(( )) & C(( ));
	B(( ))-->D(( )) & E(( ));
	C(( ))-->F(( )) & G(( ));
```

### A Complete Binary Tree
```mermaid
graph TD;
	A(( ))-->B(( )) & C(( ));
	B(( ))-->D(( ));
```

#### This is not a valid complete binary tree:
```mermaid
graph TD;
	A(( ))-->B(( )) & C(( ));
	B(( ))-->D(( ));
	C-->E(( ));
```