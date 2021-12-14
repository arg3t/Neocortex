---
title: Bypasses
date: 2021-11-16T21:07:41+01:00
---
# Bypasses

## X-Forwarded-For header

By setting this to `127.0.0.1`, forbidden 403 responses. Also, you can occasionally bypass rate limitations by changing the value of the header to another ip every-time you get rate-limited.

## Host Headers

`X-Forwarded-For` this header is sometimes used in applications that utilize a middleware. Using this header, we can alter the URLs sent to a user\'s email, which could allow us to steal password changing tokens.

## Encoding

### Double URL Encoding

This technique is fairly simple, you first encode the parameters you are sending and then re-encode the encoding string so that the `%` signs are encoded into `%25` as well.

### Overlong Unicode Encoding

The way unicode works is that each character might have a different length, and the character\'s length is defined by the value of the most significant bits of the most significant byte. If that byte is 0, than the character is a single byte, if `110` than the character is 2 bytes, if `1110` then the character is 3 bytes and so on. In multi-byte characters, the first two bits of each byte that is not the most significant byte are set to `10` to indicate that they are continuation bytes of the previous byte. These continuation bytes and the length specifying byte are removed when the character is being processed. This can be used to represent the same character in different formats, some of which might not be recognised by the protections in place:

    A (1 byte)  : 01000001 : %41
    A (2 bytes) : (110)00001 (10)000001 -> 0000 1000001: %c1%81
    A (3 bytes) : (1110)0000 (10)000001 (10)000001  -> 000000000 1000001: %c1%81%81

### 16-Bit Unicode Encoding

Just encode the parameters as 16-bit unicode. It is that simple.