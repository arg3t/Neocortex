---
title:  Radix Sort
date: 2021-12-24T04:28:25+01:00
description: 
tags: ['cs/sorting', 'cs/algorithms']
aliases: ['']
---
Radix sort is a non-comparison based sorting algorithm, it allows us to do stable sorting in a fast manner for elements that are more complicated than integers. In radix sort, when sorting a list of tuples with two elements, [[/notes/Bucket Sort|Bucket Sort]] is applied two times, once for the second element, and once for the first one.This way, the elements with the same first elements are consecutive and ordered according to their second elements. This algorithm allows for a **lexicographic** sorting of a list with $n$ tuples, each element of the tuples being in the range $[0,N-1]$ in $O(n+N)$ time.