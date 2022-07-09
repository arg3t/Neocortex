---
title:  Structure of the Internet
date: 2022-07-07T12:19:19+02:00
description: 
tags: ['cs/networking']
aliases: ['']
---
![[images/Structure of Internet.png]]
The internet is structured as an interconnected network of routers. The network can also be thought of as a [[notes/Graphs|graph]] where each router is a node and each connection is an edge between those nodes. 

When a packet needs to be moved from one router to another, a process called [[notes/Routing|routing]] takes place.

The internet is split up into several subnetworks([[notes/Graph Terminology#^f18c89|connected components]]). Each connected component is owned by an [[notes/ISP|ISP]]. The communication between those ISPs are done using two options:
* IXPs(Internet Exchange Points) which are huge data centers that manage traffic between ISPs.
* Routers of different ISPs just communicate with each other if there is a link between them.
```ad-info
The policy for each ISP differs according to politics, economics and many other factors
```