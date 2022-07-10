---
title:  IP Version 6
date: 2022-07-10T09:30:50+03:00
description: 
tags: ['cs/networking']
aliases: ['IP Version 6', 'IPv6']
---

The main difference between [[notes/IP Version 4|IPv4]] and [[notes/IP Version 6|IPv6]] is that IPv6 addresses are 128 bits and the headers are different. 
![[images/Andrew S. Tanenbaum_Computer Networks 2.png]]

- **Flow Label:** Mark a packet for a certain type of treatment
- **Next Header:** This is a pointer to the next header, the next header can contain information regarding fragmentation or other stuff. Each header has a next header field and headers form a [[notes/Linked List|linked list]].