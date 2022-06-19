---
title:  In-Place Merge-Sort
date: 2021-12-30T11:41:59+03:00
description: 
tags: ['cs/sorting', 'cs/java']
aliases: ['']
---
It is sometimes more efficient to implement [[/notes/Merge Sort|Merge Sort]] in-place. Here is an implementation that sorts an two-dimensional array of strings according to a column, the explanations are made as comments:

```java
public static void merge(String[][] in, String[][] out, int start, int inc, int col){
	int end1 = Math.min(inc + start, in.length);
	int end2 = Math.min(start + inc * 2, in.length);

	int x = start;
	int y = start + inc;
	int z = start;

	while(x < end1 && y < end2){
		if(in[x][col].compareTo(in[y][col]) <= 0) /* the <= here is crucial since it allows for stable sorting */
			out[z++] = in[x++];
		else
			out[z++] = in[y++];
	}

	if(x < end1) /* If right side of the array is consumed first, fill the rest up with the left side */
		for(int i = 0; i < end1 - x; i++)
			out[z+i] = in[x+i];
	else if(y < end2) /* Do the opposite otherwise */
		for(int i = 0; i < end2 - y; i++)
			out[z+i] = in[y+i];
}

public static void stableSort(String[][] intable, int column) {
	int s = 1;
	String[][] table = intable;

	if(table == null || table.length <= 1 || 0 > column || column >= table[0].length)
		return;

	String[][] table2 = new String[table.length][table[0].length];
	for(int i = 0; i < table.length; i++)
		for(int j = 0; j < table[i].length; j++)
			table2[i][j] = table[i][j];

	String[][] temp;
	int n = table.length;

	for(int i = 1; i < n; i*=2){
		for(int j = 0; j < n; j += 2*i)
			merge(table, table2, j, i, column);
		temp = table; table = table2; table2 = temp;
	}

	if(intable != table)
		for(int i = 0; i < table.length; i++)
			intable[i] = table[i];
	}
}
```