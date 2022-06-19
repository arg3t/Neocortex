---
title: Copying Lists
date: 2021-11-16T21:07:41+01:00
tags: [ 'cs/java', 'cs/doc', 'cs/lists']
---
When copying lists, you need to create a new [[/notes/Array|Array]]/[[/notes/Linked List|Linked List]] and copy over each element from the original list into the new one. This approach works, however, when you are copying objects, since objects are reference based, you need to call `.clone()` method of each instance.