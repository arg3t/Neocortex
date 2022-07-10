---
title:  Time To Live
date: 2022-07-10T09:10:58+03:00
description: 
tags: ['cs/networking']
aliases: ['Time To Live', 'TTL']
---

When you send a packet accross a [[notes/Network Layer|network]], it bounces around routers until it reaches its destination. However, sometimes, it might get stuck and keep between routers, say, because of a loop in the network. In order to make sure the packet "dies" after a while, each IP packet has a Time To Live value which gets decremented after each jump and the packet is deleted once TTL is 0. Once a packet dies, this is notified to the sender via [[notes/ICMP|ICMP]].

