---
title: Pwnable.kr Coin1
date: 2022-08-20T14:51:42+02:00
tags: ['cs/security', 'cs/pwntools']
aliases: ['']
---

When we connect with `nc pwnable.kr 9007`, we get the following text to greet
us:

```
        ---------------------------------------------------
        -              Shall we play a game?              -
        ---------------------------------------------------

        You have given some gold coins in your hand
        however, there is one counterfeit coin among them
        counterfeit coin looks exactly same as real coin
        however, its weight is different from real one
        real coin weighs 10, counterfeit coin weighes 9
        help me to find the counterfeit coin with a scale
        if you find 100 counterfeit coins, you will get reward :)
        FYI, you have 60 seconds.

        - How to play -
        1. you get a number of coins (N) and number of chances (C)
        2. then you specify a set of index numbers of coins to be weighed
        3. you get the weight information
        4. 2~3 repeats C time, then you give the answer

        - Example -
        [Server] N=4 C=2        # find counterfeit among 4 coins with 2 trial
        [Client] 0 1            # weigh first and second coin
        [Server] 20                     # scale result : 20
        [Client] 3                      # weigh fourth coin
        [Server] 10                     # scale result : 10
        [Client] 2                      # counterfeit coin is third!
        [Server] Correct!

        - Ready? starting in 3 sec... -

N=757 C=10
```

We can write a script using pwntools to solve it.

> [!info] Important
>
> Script should be executed inside pwnable.kr server via SSH

```py
from pwn import *

context.log_level = 'error'

def solve(r):
    r.recvuntil("N=")

    upper = int(r.recvuntil("C=")[:-2])
    c = int(r.recvuntil("\n")[:-1])

    lower = 0

    mid = 0

    while(c != 0):
        mid = (lower + upper) // 2
        r.sendline(" ".join([str(x) for x in range(lower, mid)]))
        s = r.recvline()
        w = int(s)
        if w % 10 == 0:
            lower = mid
        else:
            upper = mid
        c -= 1


    mid = (lower + upper) // 2

    r.sendline(str(mid))

r = remote("127.0.0.1", 9007)

r.recvuntil("Ready?")
for i in range(100):
    solve(r)
    r.recvuntil("Correct!")
    print(str(i))

print(r.clean())
print(r.recvline())
print(r.recvall())
```

