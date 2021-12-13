---
title: The vigenere cipher
date: 2021-11-16
---
## The vigenere cipher

The encrypted message and a key's value is added together and the result\'s modulo 26 is taken to prevent unprintable characters. Here is an example:

    If we use the key(K)  'GOLD', and P = PROCEED MEETING AS AGREED, then "add"
    P to K, we get C.  When adding, if we exceed 25, then we roll to 0 (modulo 26).


    P     P R O C E   E D M E E   T I N G A   S A G R E   E D
    K     G O L D G   O L D G O   L D G O L   D G O L D   G O

    becomes:

    P     15 17 14 2  4  4  3 12  4 4  19  8 13 6  0  18 0  6 17 4 4   3
    K     6  14 11 3  6 14 11  3  6 14 11  3  6 14 11  3 6 14 11 3 6  14
    C     21 5  25 5 10 18 14 15 10 18  4 11 19 20 11 21 6 20  2 8 10 17