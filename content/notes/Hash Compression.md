---
title:  Hash Compression
date: 2021-12-31T01:03:33+03:00
description: 
tags: ['cs/algorithms', 'cs/theory', 'cs/math']
aliases: ['']
---
It can be very useful to compress a hash value so that it becomes smaller, there are some methods to achieve this:

## The division method
In order to compress a hash i in the range $[0, N-1]$ you can simply calculate:

$$
i mod N
$$

## The MAD method
MAD is more sophisticated then the division method since it eliminates repreated patters in a set of integers.

$$
[(ai+b) mod p] mod N
$$

Where $p$ is a prime number greater than $N$ and $a$ and $b$ are randomly selected integers.