---
title:  Merge Sort
date: 2021-12-21T04:05:02+01:00
description: A recursive sorting algorithm based on a divide and conquer approach.
tags: [ 'cs/sorting', 'cs/algorithms']
aliases: ['']
---
Merge sort is a sorting algorithm based on a divide and conquer approach. Basically in merge-sort, a list is halved and sorted and then the sorted parts are then [[notes/Merging in Merge Sort|merged]]. The halving operation is repeated until the halved list is of size 1 at this point, the recursion stops. In the end, drawing a graph of all the recursive calls gives us a complete binary tree [[notes/Full & Complete Trees|Full vs Complete Binary Trees]]. 

## An example merge-sort implementation
```java
public static int[] mergeSort(int[] list){
	if(list == null || list.length <= 1)
		return list;
	int[] l1 = Arrays.copyOfRange(0, l1.length / 2, list);
	int[] l2 = Arrays.copyOfRange(l1.length / 2, l1.length, list);
	l1 = mergeSort(l1);
	l2 mergeSort(l2);
	return merge(l1, l2);
}
```
