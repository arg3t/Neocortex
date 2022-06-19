---
title:  Hash Collision Handling
date: 2021-12-31T01:21:45+03:00
description: 
tags: ['cs/algorithms']
aliases: ['']
---
Since we apply [[/notes/Hash Compression|Hash Compression]] in [[/notes/Hash Tables|Hash Tables]], hash collisions may occur often, so handling the collisions becomes critical in order to sustain an efficient [[/notes/Big-Oh Notation|time complexity]].

## Seperate Chaining
In this method, each entry in an array points to a linked list. This method works, but it makes this implementation susceptible to running in $O(n)$ time if every element added to the map has the same hash value. In order to prevent this, the $\lambda$ of this map, ($\lambda = n/N$) where $n$ is the number of elements in an array, and $N$ is the size of the map. In order to sustain an efficient hash map, the **load factor** must be kept under 1.

## Open Addressing
In order to avoid using buckets, we can instead use the array itself to store the colliding elements. Even though it is not as easy as seperate chaining, it uses less space.