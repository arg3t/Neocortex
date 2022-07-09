---
title:  IP Ranges
date: 2022-07-09T09:28:50+02:00
description: 
tags: ['cs/networking']
aliases: ['Subnet Masks']
---

When you want to represent several IPs, we use a combination of IP addresses and subnet masks. The subnet mask essentially acts as a **bitmask** that ensures the IP addresses in the range has certain bits same as the IP range's address. Here is an example:

---

- **IP Address:** 192.168.1.0
- **Subnet Mask:** 255.255.255.0
- **IP Range:** 192.168.1.0/24

In this example, 24 is the number of bits set in the bitmask.
This IP range has $2^8$ possible IPs.

