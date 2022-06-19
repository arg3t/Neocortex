---
title:  Merging in Merge Sort
date: 2021-12-21T07:59:57+03:00
description: 
tags: ['cs/sorting', 'cs/algorithms']
aliases: ['']
---
After the recursive calls return two sorted lists, you need to merge them. Since they are both sorted, merging them into a new sorted list can be done in $O(n)$ complexity. Here is a subsequent java code that would achieve this:

```java
public static int[] merge(int[] l1, int[] l2){
	int[] merged = new int[l1.length + l2.length];
	int i = 0;
	int j = 0;
	while(i + j < merged.length){
		if(i < l1.length && (l2.length <= j || l1[i] > l2[j]))
			merged[i+j] = l1[i++];
		else
			merged[i+j] = l2[j++];
	}
	return merged;
}
```