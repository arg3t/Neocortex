---
author: Yigit Colakoglu
date: 2021-06-19 Sat
email: yigit\@yigitcolakoglu.com
lang: en
title: Krypton Solutions
---

```{=org}
#+roam_tags: security cryptology ctf wargame overthewire
```
# Krypton

-   krypton0: `echo S1JZUFRPTklTR1JFQVQ= | base64 -d` (KRYPTONISGREAT)
-   krypton1: `cat krypton2 | tr A-Z N-ZA-M` (ROTTEN)

## krypton2

create a file that contains all the letters in the alphabet, and run the encrypt binary on the file. Now you have a one-to-one map of all the letters and their correspondants. Using this info you can easily decode the string:

    abcdefghijklmnopqrstuvwxyz
    MNOPQRSTUVWXYZABCDEFGHIJKL

    OMQEMDUEQMEK
    caeseriseasy (CAESARISEASY)

## krypton3

We have 3 files, translated from english text that were encrypted from the same key. Since they are originally english, we can have a general idea of the key by counting the frequency of each character `cat found* | grep -o . | sort | uniq -c`. [Letter Frequencies](./static/Krypton/2021-06-12T17:16:32_Letter_Frequencies.png) [Website for more details](https:www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html)

  letter   count   frequency      equals
  P        2       2.8409091e-3   Z
  H        4       5.6818182e-3   Q
  R        4       5.6818182e-3   X
  O        12      0.017045455    J
  I        19      0.026988636    K
  F        28      0.039772727    V
  A        55      0.078125       B
  L        60      0.085227273    P
  E        64      0.090909091    Y
  K        67      0.095170455    G
  X        71      0.10085227     F
  T        75      0.10653409     W
  Y        84      0.11931818     M
  M        86      0.12215909     U
  W        129     0.18323864     C
  V        130     0.18465909     L
  Z        132     0.1875         D
  D        210     0.29829545     R
  C        227     0.32244318     H
  G        227     0.32244318     S
  N        240     0.34090909     N
  B        246     0.34943182     I
  U        257     0.36505682     O
  J        301     0.42755682     A
  Q        340     0.48295455     T
  S        456     0.64772727     E
  TOTAL    704     1              

  : Single Letter Counts and Frequencies

```{=org}
#+TBLFM: $3=$2/@30$2
```
```{=org}
#+STARTUP: align
```
``` {.python results="output"}
ciphertext = "<<concatanted>>"
password = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS"
order = ['E','Q','T','S','O','R','I','N','H','C','L','D','U','P','M','F','W','G','Y','B','K','V','X','Q','J','Z']

def letter_order(string):
    counts = [0]*26
    order = ""
    for i in string:
        c = ord(i.upper()) - 65
        if -1 < c < 26:
            counts[c] += 1
    for i in range(26):
        m = (0,0)
        for j in range(26):
            if counts[j] > m[1]:
                m = (j,counts[j])
        counts[m[0]] = 0
        order += chr(65+m[0])
    return order

def genkeys(order):
    if len(order) == 0:
        return [""]
    keys = []
    for i in range(len(order[0])):
        if len(order[0]) > 1:
            neworder = [order[0][0:i] + order[0][i+1:]] + order[1:]
        else:
            neworder = order[1:]
        for j in genkeys(neworder):
            keys.append(order[0][i]+j)
    return keys

def solve(s,orig,ceasar):
    solved = ""
    for i in s:
        if 64 < ord(i.upper()) < 91:
            solved += orig[ceasar.find(i.upper())]
    return solved

cipherorder = letter_order(ciphertext)
for i in genkeys(order):
    print(i)
    print(cipherorder)
    print(solve(password, i, cipherorder))
```

```{=org}
#+RESULTS:
```
``` example
EQTSORINHCLDUPMFWGYBKVXQJZ
SQJUBNCGDZVWMYTXKELAFIOHRP
WELLDONETHELEVELFOURPQSSWORDISBRUTE
```

The password is *BRUTE*

## krypton4

This time a[ Vigenere Cipher](vigenere.org) is used to encrypt the text. We know the key is 6 characters long. There are two files. We can just use a simple vigenere [https:f00l.de/hacking/vigenere.php>](solver). Or we can use the script I wrote:

```python
def letter_freq(string):
    counts = [0]*26
    freqs = {}
    for i in string:
        c = ord(i.upper()) - 65
        if -1 < c < 26:
            counts[c] += 1
    for i in range(26):
        freqs[chr(i+65)] = counts[i]/len(string)
    return freqs

def shiftback(s,c):
    f = ""
    for i in s:
        foo = ord(i) - ord(c)
        if foo < 0:
            f += chr(foo + 26 + 65)
        else:
            f += chr(foo + 65)
    return f

def calcoffset(s):
    freqs={'E': 0.12,'T': 0.091,'A': 0.0812,'O': 0.0768,'I': 0.0731,'N': 0.0695,'S': 0.0628,'R': 0.0602,'H': 0.0592,'D': 0.0432,'L': 0.0398,'U': 0.0288,'C': 0.0271,'M': 0.0261,'F': 0.023,'Y': 0.0211,'W': 0.0209,'G': 0.0203,'P': 0.0182,'B': 0.0149,'V': 0.0111,'K': 0.0069,'X': 0.0017,'Q': 0.0011,'J': 0.001,'Z': 0.0007}
    probs = {}
    for i in range(26):
        p = 0
        foo = shiftback(s,chr(i+65))
        f = letter_freq(foo)
        for j in f:
            p += abs(f[j] - freqs[j])/2
        probs[chr(65+i)] = p
    best = (0,1)
    for i in probs:
        if probs[i] < best[1]:
            best = (i,probs[i])
    return best

def slice(s,l):
    slices = []
    for i in range(l):
        substr = ""
        for c in range(i, len(s), l):
            substr += s[c]
        slices.append(substr)
    return slices

def findkey(s,keylen):
    key = ""
    chances = 1
    slices = slice(s,keylen)
    for i in slices:
        (c,prob) = calcoffset(i)
        chances -= prob/keylen
        key += c
    return key,chances

def decrypt(s,key):
    d = ""
    for i in range(len(s)):
        d+=shiftback(s[i],key[i%len(key)])
    return d

def solve(s,cipher,mkl=20,keylen=None):
    s = s.replace(" ","").upper()
    cipher = cipher.replace(" ","").upper()
    if keylen:
        best = findkey(cipher,keylen)
        return [(decrypt(s,best[0]),best[0],best[1])]
    else:
        keys = []
        for i in range(1,mkl+1):
            res = findkey(cipher,i)
            keys.append((decrypt(s,res[0]),res[0],res[1]))
        return sorted(keys, key=lambda tup: tup[2],reverse=True)

ciphertext = "<<concatanated>>" # Too long, enter the contents of found1 or found2
solution = solve('HCIKV RJOX', ciphertext, keylen=6)[0]
print("Key Found: " + solution[1])
print("Decrypted Text Is: " + solution[0])
print("Confidence: {0:.0f}%".format(solution[2]*100))
```

Password is *CLEARTEXT*

## krypton5

same method as [*krypton4*]{.spurious-link target="krypton4"}

```python
def letter_freq(string):
    counts = [0]*26
    freqs = {}
    for i in string:
        c = ord(i.upper()) - 65
        if -1 < c < 26:
            counts[c] += 1
    for i in range(26):
        freqs[chr(i+65)] = counts[i]/len(string)
    return freqs

def shiftback(s,c):
    f = ""
    for i in s:
        foo = ord(i) - ord(c)
        if foo < 0:
            f += chr(foo + 26 + 65)
        else:
            f += chr(foo + 65)
    return f

def calcoffset(s):
    freqs={'E': 0.12,'T': 0.091,'A': 0.0812,'O': 0.0768,'I': 0.0731,'N': 0.0695,'S': 0.0628,'R': 0.0602,'H': 0.0592,'D': 0.0432,'L': 0.0398,'U': 0.0288,'C': 0.0271,'M': 0.0261,'F': 0.023,'Y': 0.0211,'W': 0.0209,'G': 0.0203,'P': 0.0182,'B': 0.0149,'V': 0.0111,'K': 0.0069,'X': 0.0017,'Q': 0.0011,'J': 0.001,'Z': 0.0007}
    probs = {}
    for i in range(26):
        p = 0
        foo = shiftback(s,chr(i+65))
        f = letter_freq(foo)
        for j in f:
            p += abs(f[j] - freqs[j])/2
        probs[chr(65+i)] = p
    best = (0,1)
    for i in probs:
        if probs[i] < best[1]:
            best = (i,probs[i])
    return best

def slice(s,l):
    slices = []
    for i in range(l):
        substr = ""
        for c in range(i, len(s), l):
            substr += s[c]
        slices.append(substr)
    return slices

def findkey(s,keylen):
    key = ""
    chances = 1
    slices = slice(s,keylen)
    for i in slices:
        (c,prob) = calcoffset(i)
        chances -= prob/keylen
        key += c
    return key,chances

def decrypt(s,key):
    d = ""
    for i in range(len(s)):
        d+=shiftback(s[i],key[i%len(key)])
    return d

def solve(s,cipher,mkl=20,keylen=None):
    s = s.replace(" ","").upper()
    cipher = cipher.replace(" ","").upper()
    if keylen:
        best = findkey(cipher,keylen)
        return [(decrypt(s,best[0]),best[0],best[1])]
    else:
        keys = []
        for i in range(1,mkl+1):
            res = findkey(cipher,i)
            keys.append((decrypt(s,res[0]),res[0],res[1]))
        return sorted(keys, key=lambda tup: tup[2],reverse=True)

ciphertext = "<<concatanated>>" # Too long, enter the contents of found1 or found2
solutions = solve('BELOS Z', ciphertext)
for i in range(3): # print the top 5
    print("Key Found: " + solutions[i][1])
    print("Decrypted Text Is: " + solutions[i][0])
    print("Confidence: {0:.0f}%".format(solutions[i][2]*100))
```

Password is *RANDOM*

## krypton6

When we pass a bunch of \"A\"s into to the encryption binary, we get a repeating pattern `EICTDGYIYZKTHNSIRFXYCPFUEOCKRN`{.verbatim}. We can then simply use this to calculate the original text:

``` python
ciphertext="EICTDGYIYZKTHNSIRFXYCPFUEOCKR"
string="PNUKLYLWRQKGKBE"
decrypted = ""
for i in range(len(string)):
    k =  ord(string[i]) - ord(ciphertext[i]) + 65
    if k < 65:
        k += 26
    decrypted += chr(k)
return decrypted
```
