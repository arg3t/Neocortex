---
title: Pwnable.kr Blackjack
date: 2022-08-20T18:09:52+02:00
tags: ['cs/security']
aliases: ['']
---

A blackjack code published on
[cboard](https://cboard.cprogramming.com/c-programming/114023-simple-blackjack-program.html) is also for this challenge.
A quick glimpse through the code shows that we can enter negative values as
bets, and those values are substracted(hence added) from our current balance
once we lose. So we enter -1000000 as our bet and lose, which gives us the flag.



