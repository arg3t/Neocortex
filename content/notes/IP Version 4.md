---
title:  IP Version 4
date: 2022-07-10T09:06:04+03:00
description: 
tags: ['cs/networking']
aliases: ['IP Version 4', 'IPv4']
---

The IP Protocol for is the protocol that is used between [[notes/Network Layer|network layers]].
It has two versions, version 4 and [[notes/IP Version 6|IPv6]]. Every IP packet has a payload and headers. Its headers are as given below:

![[images/Andrew S. Tanenbaum_Computer Networks.png]]

## Packet Fragmentation

[[notes/Packet Fragmentation|Packet fragmentation]] is achieved via the *Fragment Offset*, *Identification* and the *MF*/*DF* flags. When the *DF* bit is set, the router returns an error message instead of applying *Non-Transparent Fragmentation*. This way, the host can figure out the MTU split packets into smaller fragments. When a packet is fragmented the *MF* bit is set meaning it has more fragments to come. Moreover, the *Identification* field is used to indicate which packet it belongs to. Finally, the order of the fragments is communicated using the *Fragment Offset* header. Which includes the number of previous bytes in that packet.