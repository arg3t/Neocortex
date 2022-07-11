---
title:  Quick Sort Pivot Selection
date: 2021-12-23T01:05:53+03:00
description: 
tags: ['cs/algorithms', 'cs/sorting']
aliases: ['']
---
The most important aspect in a quick sort algorithm is how the pivot is chosen, the pivot decides how well-balanced the recursion tree of the algorithm turns out to be. An ideal pivot selection results in a [[notes/Full & Complete Trees|complete]] binary recursion tree. There are several methods for choosing a pivot:

## Blindly Picking the Last Element
Blindly picking the last element makes the impementation susceptible to having a [[notes/Big-Theta Notation|Big-Theta Notation]] of $\Theta(n^2)$ if the provided array is sorted in an ascending order.

## Random selection
Randomly selecting the pivot point in each iteration will result in a time complexity of $O(nlog(n))$

## Median of three
When picking a pivot, another approach is to just pick the median of the first, last and middle element. This too results in a complexity of $O(nlog(n))$, and in my opinion this is a more robust approach.