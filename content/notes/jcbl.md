---
title: Pwnable.kr Input
date: 2022-08-20T11:23:47+02:00
tags: ['cs/security', 'cs/pwn']
aliases: ['']
---

This challenges teaches the solver on controlling environment variables,
arguments and pipes of the process that is executed as well as using sockets.
I won't be going through each line by line, but here is the solution:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>

int main (int argc, char *argv[])
{
	system("ln -s /home/input2/flag /tmp/fr1nge/flag");

	char* args[101];
	char* env[] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe", NULL};

	for(int i = 0; i < 100; i++){
		if(i == 'A'){
			args[i] = "\x00";
		}else if(i == 'B'){
			args[i] = "\x20\x0a\x0d";
		}else if(i == 'C'){
			args[i] = "9192";
		}else{
			args[i] = "A";
		}
	}
	args[100] = NULL;

	chdir("/tmp/fr1nge");

	FILE* fp = fopen("/tmp/fr1nge/\x0a", "w");
	fwrite("\x00\x00\x00\x00", 4, 1, fp);
	fclose(fp);

	int p0[2];
	int p2[2];
	pipe(p0);
	pipe(p2);

	int pid = fork();

	if(pid == 0){
		close(p0[0]);
		close(p2[0]);
		write(p0[1], "\x00\x0a\x00\xff", 4);
		write(p2[1], "\x00\x0a\x02\xff", 4);
		
		int sock = socket(AF_INET, SOCK_STREAM, 0);
		struct sockaddr_in serv_addr;
		serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(9192);
		inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);
		int client_fd;

		while ((client_fd
         = connect(sock, (struct sockaddr*)&serv_addr,
                   sizeof(serv_addr)))
        < 0);
    send(sock, "\xde\xad\xbe\xef", 4, 0);
	}else{
		close(p0[1]);
		close(p2[1]);
		dup2(p0[0], 0);
		dup2(p2[0], 2);
		close(p0[0]);
		close(p2[0]);
		execvpe("/home/input2/input", args, env, 0);
	}

	return 0;
}
```


> [!warning] Attention
>
> Since you are not allowed to write to the home directory, you first need to
> create a directory under /tmp and link the flag file in home to that new dir.



