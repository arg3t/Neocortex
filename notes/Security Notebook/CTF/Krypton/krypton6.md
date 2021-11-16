## krypton6

When we pass a bunch of "A"s into to the encryption binary, we get a repeating pattern `EICTDGYIYZKTHNSIRFXYCPFUEOCKRN`. We can then simply use this to calculate the original text:

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