---
title: krypton4
date: 2021-11-16T21:07:41+01:00
tags: ['cs/security', 'cs/cryptography']
---


This time a [[/notes/Vigenere|vigenere cipher]] is used to encrypt the text. We know the key is 6 characters long. There are two files. We can just use a simple vigenere [solver](https:f00l.de/hacking/vigenere.php>). Or we can use the script I wrote:

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