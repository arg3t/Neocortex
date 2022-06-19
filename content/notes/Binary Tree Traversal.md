---
title:  Binary Tree Traversal
date: 2022-01-02T09:44:41+03:00
description: 
tags: ['cs/data-structures', 'cs/trees', 'cs/algorithms']
aliases: ['']
---
## With recursion
With recursion, it pretty straightforward, here is an example java code:
```java
public static void traverse(BinaryTree t, List<Integer> l){
	if(t == null)
		return;
	traverse(t.getLeft(), l);
	l.add(t.getKey());
	traverse(t.getRight(), l)
}
```

## Without recursion
```java
public static void traverse(BinaryTree t, List<Integer> l){
	Stack<BinaryTree> s = new Stack<>();
	BinaryTree cur = t;
	while(cur != null || !t.isEmpty()){
		if(cur == null){
			cur = s.pop();
			l.add(cur.getKey());
			cur = s.getRight();
		}else{
			s.push(cur);
			cur = cur.getLeft();
		}
	}
}
```