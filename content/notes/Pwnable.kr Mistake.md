---
title: Pwnable.kr Mistake
date: 2022-08-20T13:40:53+02:00
tags: ['cs/security', 'cs/pwn']
aliases: ['']
---
For this one, you need to be especially careful, while inspecting the source
code, pay attention to the line:

```c
if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
```

Here, the programmer meant to to save the return value of `open()` to fd, 
but they forgot to use braces so instead they save the result of the comparison
to fd. So, if the comparison fails, fd is set to 0. That is STDIN. Hence, all we
need to do is input a 10 character string first and after that the string with
each byte XORed with 1.

```
mistake@pwnable:/tmp/fr1nge_mistake$ ~/mistake
do not bruteforce...
0000000000
input password : 1111111111
Password OK
Mommy, the operator priority always confuses me :(
```



