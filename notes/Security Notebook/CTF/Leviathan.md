---
title: # Leviathan
date: 2021-11-16
---
# Leviathan

-   leviathan0: `grep leviathan ~/.backup/bookmarks.html` (rioGegei8m)

## leviathan1

The home dir has a single SUID binary **check**, owned by *leviathan2*

    -r-sr-x--- 1 leviathan2 leviathan1 7.3K Aug 26  2019 check

We can use [radare2](radare2.org) to get an idea of what the binary does:

``` {.asm6502 .numberLines startFrom=""}
mov dword [s2], 0x786573    ; 'sex'
mov dword [var_17h], 0x72636573 ; 'secr'
mov word [var_13h], 0x7465  ; 'et'
mov byte [var_11h], 0
mov dword [var_1bh], 0x646f67 ; 'god'
mov dword [var_20h], 0x65766f6c ; 'love'
mov byte [var_1ch], 0
sub esp, 0xc
push str.password:_         ; 0x8048690 ; "password: " ; const char *format
call sym.imp.printf         ; int printf(const char *format)
add esp, 0x10
call sym.imp.getchar        ; int getchar(void)
mov byte [s1], al
call sym.imp.getchar        ; int getchar(void)
mov byte [var_bh], al
call sym.imp.getchar        ; int getchar(void)
mov byte [var_ah], al
mov byte [var_9h], 0
sub esp, 8
lea eax, [s2]
push eax                    ; const char *s2
lea eax, [s1]
push eax                    ; const char *s1
call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
add esp, 0x10
test eax, eax
jne 0x80485e5
```

Ok, so there are multiple strings defined, \'sex\', \'secr\', \'et\', \'god\', \'love\'. The binary than prints the password prompt and saves the user\'s input into `[s1]` as can be seen on the instruction `mov byte [s1] al`. It then pushes `s1` and `s2` on the stack and calls `strcmp` on those two strings. If they match (aka. `text eax, eax` sets the zero flag) than a shell is spawned. And between all the strings in the start, the one pushed to `[s2]` s2 is `sex`, nice. (ougahZi8Ta)

## leviathan2

```assembly
.text
main:
add esp, 0x10
test eax, eax
je 0x80485a8
sub esp, 0xc
push str.You_cant_have_that_file... ; 0x80486b9 ; "You cant have that file..." ; const char *s
call sym.imp.puts           ; int puts(const char *s)
add esp, 0x10
mov eax, 1
jmp 0x80485fa
mov eax, dword [ebx + 4]
add eax, 4
mov eax, dword [eax]
push eax
push str.bin_cat__s         ; 0x80486d4 ; "/bin/cat %s" ; const char *format
push 0x1ff                  ; 511 ; size_t size
lea eax, [string]
pop ebx
pop ebp
lea esp, [ecx - 4]
ret
```

The program asks the user for the input of a filename and then runs `/bin/cat %s` using the `system` function call. We can inject any command we want by separating the filename with *;* . We can simply create a file with the name \'; sh\' and run `printfile`. Bada Bing Bada Boom, we have a shell.(Ahdiemoo1j)

## leviathan3