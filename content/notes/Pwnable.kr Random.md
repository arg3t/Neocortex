---
title: Pwnable.kr Random
date: 2022-08-20T10:18:19+02:00
tags: ['cs/security', 'cs/pwn']
aliases: ['random']
---

The source code for the challenge is:
```c
#include <stdio.h>

int main(){
	unsigned int random;
	random = rand();	// random value!

	unsigned int key=0;
	scanf("%d", &key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		system("/bin/cat flag");
		return 0;
	}

	printf("Wrong, maybe you should try 2^32 cases.\n");
	return 0;
}
```

The mistake here is clear, `rand()` is called without calling `srand()`
first. According to the rand manpage:

> If no seed value is provided, the rand() function is automatically seeded with  a value of 1.

So, running the program below gives us the key we should enter:

```c
#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
	unsigned int random = rand();

	printf("%d\n", random ^ 0xdeadbeef);

	return 0;
}
```

