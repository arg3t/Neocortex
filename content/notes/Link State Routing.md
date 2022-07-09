---
title:  Link State Routing
date: 2022-07-07T01:33:01+02:00
description: 
tags: ['cs/networking']
aliases: ['']
---
Works by storing the entire network's graph and running a path-finding algorithm such as [[notes/Dijkstra's Algorithm|djikstra]] when a packet needs to be routed. For routers to learn about the state of the entire networ, the following algorithm is used.
1. Routers announce information about their neighours.
2. Other routers who receive the announcement update their graphs and announce what they learned. This allows knowledge to be propagated accross the network.
3. Once all the information is shared, routers learn nothing new so the communication regarding the network stops.
