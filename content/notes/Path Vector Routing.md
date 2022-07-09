---
title:  Path Vector Routing
date: 2022-07-07T01:29:50+02:00
description: 
tags: ['cs/networking']
aliases: ['']
---
Path vector. routing is very similar to [[notes/Distance Vector Routing|distance vector routing]] except that it solves the *count to infinity problem* by storing the path to access the router instead of just storing the neighbour.

```ad-danger
In large networks, since routes may be long, path vector routing tables can get **HUGE**.
```