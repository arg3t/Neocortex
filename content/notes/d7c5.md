---
title: Reversing Hero Level 4
date: 2022-08-20T09:30:34+02:00
tags: ['cs/security', 'cs/reversing']
aliases: ['']
---

## Initial opinions

Opening up the file, we are greeted with the start function. It calls a function
and checks if it returns an exit code 0 and gives us the flag if that is the
case:

```asm
; Opens a file and uses it for taking input
mov     rax, 2
mov     rdi, offset filename ; filename = "d.d"
mov     rsi, 0
syscall

; Omitted some useless assembly here...

mov     rdi, r12
mov     rsi, 0DEADFACEDEADBEEFh
mov     rdx, 123456701234567h
mov     rcx, 80h
mov     r8, offset var_flagbuf
call    f_maincheck
```

## f_maincheck

This function has a bunch of calls.
```c
  v10 = a2;
  v11 = 64;
  while ( 1 )
  {
    v8 = f_getfirst_char(fd);
    result = -1LL;
    if ( v8 == -1 )
      break;
    f_some_weirdshit(a5, v8);
    result = f_bit_manipulator(&v10, v8);
    if ( result )
      break;
    result = 0LL;
    if ( v10 == a3 )
      break;
    if ( !--a4 )
      return -1LL;
  }
  return result;
```

Now, the `f_some_weirdshit` function is important, and I have spent a bunch of
time trying to reverse it. However, it is as complicated as it is useful. And
after solving the challenge, I still don't know what it does. The function that
matters here is `f_bit_manipulator`, since if it alters `a2` so that is equal to
`a3`, then the function returns 0 and we get the flag. In our case:

```
a2 = 0xDEADFACEDEADBEEF
a3 = 0x0123456701234567
```

## f_bit_manipulator
Looking at the IDA decompilation, we see the following. 

```c
__int64 __fastcall f_bit_manipulator(_QWORD *a1, __int64 a2)
{
  __int64 v2; // rsi
  __int64 v3; // rsi
  int v4; // ecx
  unsigned int v5; // ecx
  unsigned int v6; // ecx
  unsigned int v7; // ecx
  unsigned int v8; // ecx

  v2 = a2 - 0x30;
  if ( !v2 )
  {
    v4 = *((_DWORD *)a1 + 2);
    if ( !v4 )
      return -1LL;
    *a1 = __ROR8__(2LL * (__ROL8__(*a1, v4) >> 1), v4);
    --*((_DWORD *)a1 + 2);
    return 0LL;
  }
  v3 = v2 - 1;
  if ( !v3 )
  {
    v5 = *((_DWORD *)a1 + 2);
    if ( v5 >= 0x40 )
      return -1LL;
    v6 = v5 + 1;
    *a1 = __ROR8__(2LL * (__ROL8__(*a1, v6) >> 1), v6);
    *((_DWORD *)a1 + 2) = v6;
    return 0LL;
  }
  if ( v3 == 1 )
  {
    v7 = *((_DWORD *)a1 + 2);
    if ( v7 < 0x40 )
    {
      v8 = v7 + 1;
      *a1 = __ROR8__((2LL * (__ROL8__(*a1, v8) >> 1)) | 1, v8);
      *((_DWORD *)a1 + 2) = v8;
      return 0LL;
    }
  }
  return -1LL;
}
```

I don't know about you, but that hurts my eyes. Instead, let's take a look at
the disassembly:

```asm
f_bit_manipulator proc near
                sub     rsi, 30h ; '0'
                jz      short myloc_0x30
                dec     rsi
                jz      short myloc_0x31
                dec     rsi
                jz      short myloc_0x32
                jmp     short myloc_invalid

myloc_0x30:    
                mov     ecx, [rdi+8]
                jecxz   myloc_invalid
                mov     rax, [rdi]
                rol     rax, cl
                shr     rax, 1
                shl     rax, 1
                ror     rax, cl
                mov     [rdi], rax
                dec     dword ptr [rdi+8]
                jmp     short myloc_ret0

myloc_0x31:  
                mov     ecx, [rdi+8]
                cmp     ecx, 40h ; '@'
                jnb     short myloc_invalid
                mov     rax, [rdi]
                inc     ecx
                rol     rax, cl
                shr     rax, 1
                shl     rax, 1
                ror     rax, cl
                mov     [rdi], rax
                mov     [rdi+8], ecx
                jmp     short myloc_ret0

myloc_0x32:                     
                mov     ecx, [rdi+8]
                cmp     ecx, 64
                jnb     short myloc_invalid
                mov     rax, [rdi]
                inc     ecx
                rol     rax, cl
                shr     rax, 1
                shl     rax, 1
                or      rax, 1
                ror     rax, cl
                mov     [rdi], rax
                mov     [rdi+8], ecx

myloc_ret0:                      
                xor     eax, eax
                jmp     short locret_4003E3

myloc_invalid: 
                or      rax, 0FFFFFFFFFFFFFFFFh

locret_4003E3:  
                retn
f_bit_manipulator endp
```

After a quick examination, we can make the following inferences:

* The function only accepts `0`, `1` or `2` characters as the input. As you can see from
    the initial cmp and jmp statements which correspond to a switch.
* When the character is 0, the counter at [rdi+8], which is set to 64 by
`f_maincheck` in line `v11 = 64` (Reference to the assembly to understand how
that variable is accessed in another function) is moved to rcx. Afterwards,
`a2`'s RCX'th most significant bit is set to 0.
* When the char is 1, the counter is incremented.
* When the char is 2, the counter is incremented and the reverse of 0 occurs,
i.e. RCXth bit is set to 1.

### How is the RCXth bit set to 0.
If you look the assembly below:

```asm
rol     rax, cl
shr     rax, 1
shl     rax, 1
ror     rax, cl
```

Rotating left by RCX means that RCXth most
significant bit is at the leftmost point in the register. Then, shifting right
and left means that bit is set to 0. That is equivalent to anding with
`0xFFFFFFFFFFFFFFFE`


## The python program
It is easier to first set the contents of `a2` to `0` and then setting each
necessary bit to `1`:

```py
target = 0x0123456701234567

payload = "" # Null out the register first

reps = 0
while target > 0:
    if target % 2 == 1:
        payload += "2"
    else:
        payload += "1"

    target = target >> 1
    reps += 1

print("0" * 64 + "1"*(64-reps) + payload[::-1])
```
