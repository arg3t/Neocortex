---
title: Copying Lists
date: 2021-11-16T21:07:41+01:00
---
## Copying Lists
When copying lists, you need to create a new [[Array]]/[[Linked List]] and copy over each element from the original list into the new one. This approach works, however, when you are copying objects, since objects are reference based, you need to call `.clone()` method of each instance.