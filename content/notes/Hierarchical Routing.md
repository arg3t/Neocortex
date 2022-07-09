---
title:  Hierarchical Routing
date: 2022-07-07T01:40:17+02:00
description: 
tags: ['cs/networking']
aliases: ['']
---

When networks get very big, you can start inserting [[notes/IP Ranges|ip ranges]] into routing tables. When routing a fragment, if the destination ip is in one of the IP ranges in the table, the packet gets routed to that router.

```ad-caution
When two or more ip ranges contain the destination ip, the router with the smallest range is selected.
```