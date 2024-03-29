---
title: Array
date: 2021-11-16T21:07:41+01:00
tags: ['cs/data-structures', 'cs/lists']
---
Arrays are data structures that allow access to its entries using indexes. They are basically an amount of space allocated in memory, and each entry in the array is placed in that space one after another. Since each entry's size is set, their location in memory is constant so accessing an element by index takes $O(1)$ time. However, they are not very flexible so, removing an element to an array, adding an element to an array that is already full, or putting an element on a certain spot, shifting the elements when necessary takes $O(n)$ time.