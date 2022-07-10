---
title:  Packet Fragmentation
date: 2022-07-09T12:07:08+02:00
description: 
tags: ['cs/networking']
aliases: ['Packet Fragmentation', 'MTU']
---

In the [[notes/Network Layer|network layer]], there are often certain limits imposed on the maximum packet size. This limit is called the **MTU (Maximum Transfer Unit)**. When you need to send packets larger than the MTU, these packets need to be split up into smaller ones. This is called *fragmentation*. There are two ways to fragment packets.

- **Non-Transparent Fragmentation:** Router splits up packages and the end-host reassembles
- **Transparent Fragmentation:** Router sends a message to the sending server to split packets up into smaller ones. The process of the router telling the server to split up packets is called *MTU Discovery*.

