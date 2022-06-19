---
title:  Hash Tables
date: 2021-12-31T12:57:08+03:00
description: 
tags: ['cs/data-structures']
aliases: ['']
---
A hash table is a data structure in which every entry is mapped into an index in an [[/notes/Array|Array]] according to that entry's [[/notes/Hash Functions|hash value]]. Since a hash function might output value of a big-range, creating an array of that size may be undesirable. so the hash values are [[/notes/Hash Compression|compressed]]. This compression might lead to hash collision so [[/notes/Hash Collision Handling|Hash Collision Handling]] must be implemented.