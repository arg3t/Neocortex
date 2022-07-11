---
title: Queue
date: 2021-11-23T09:00:33+01:00
tags: ['cs/data-structures']
---
A queue is a first in first out data structure that the added data are lined up just like a queue. The data structure works just like a real queue. As new data is added, it is added to the end-the tail- of the list and as data is removed, it is removed from the head. The user of the data structure only has access to the first entry on the head. Queues are closely related to [[notes/Linked List|linked lists]] and can easily map using the following operations

| **Linked List** | **Queue**|
|-----------------|----------|
|*removeFront()*|*unenqueue()*|
|*addTail()*|*enqueue()*|
|*getFront()*|*poll()*|
