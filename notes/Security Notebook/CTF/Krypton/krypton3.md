
## krypton3

We have 3 files, translated from english text that were encrypted from the same key. Since they are originally english, we can have a general idea of the key by counting the frequency of each character `cat found* | grep -o . | sort | uniq -c`. [Letter Frequencies](./static/Krypton/2021-06-12T17:16:32_Letter_Frequencies.png) [Website for more details](https:www3.nd.edu/~busiforc/handouts/cryptography/cryptography%20hints.html)

**letter**|** count**|** frequency**|** equals**
:-----:|:-----:|:-----:|:-----:
P| 2| 2.8409091e-3| Z
H| 4| 5.6818182e-3| Q
R| 4| 5.6818182e-3| X
O| 12| 0.017045455| J
I| 19| 0.026988636| K
F| 28| 0.039772727| V
A| 55| 0.078125| B
L| 60| 0.085227273| P
E| 64| 0.090909091| Y
K| 67| 0.095170455| G
X| 71| 0.10085227| F
T| 75| 0.10653409| W
Y| 84| 0.11931818| M
M| 86| 0.12215909| U
W| 129| 0.18323864| C
V| 130| 0.18465909| L
Z| 132| 0.1875| D
D| 210| 0.29829545| R
C| 227| 0.32244318| H
G| 227| 0.32244318| S
N| 240| 0.34090909| N
B| 246| 0.34943182| I
U| 257| 0.36505682| O
J| 301| 0.42755682| A
Q| 340| 0.48295455| T
S| 456| 0.64772727| E
TOTAL| 704| 1| 

**Single Letter Counts and Frequencies:**

```python
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

```
EQTSORINHCLDUPMFWGYBKVXQJZ
SQJUBNCGDZVWMYTXKELAFIOHRP
WELLDONETHELEVELFOURPQSSWORDISBRUTE
```

The password is *BRUTE*