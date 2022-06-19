---
title: File Path Traversal
date: 2021-11-16T21:07:41+01:00
tags: ['cs/security', 'cs/web']
---

File path traversal vulnerabilities allow an attacker to read/write arbitrary files in a web server. This ability can be used to leak sensitive information or, in case of writing, can be used to escalate to OS Command injection.

## Basic Path Traversal

When the web application does not properly sanitise the parameters where a filename is expected, it could be possible to inject `../` s on the path which could allow an attacker to access files higher in the directory hierarchy.

## Bypassing Protections

### Absolute Paths

Even when a web app does not respond to request like `?file=../../../../.././../etc/passwd` as the attacker wants, it could still be possible to access files using absolute filenames like `?file=/etc/passwd`.

### Sanitisation of Path Traversal Payloads

When a web applications sanitises payloads like `../`, if it doesn\'t remove them recursively it could be possible to still access files in the higher directories using payloads like `....//` since when sanitised it would still be valid(`....//` -\> `.[../]` -\> `../`)

### URL Encoding

In the cases where we try to bypass a middleware that blocks/sanitises our input, we can play around with the encoding of our inputs which can allow us to bypass the middleware\'s protection. In order to bypass, we can use [Overlong Unicode Encoding](web_bypasses.org::*Overlong Unicode Encoding) and [Double URL Encoding](web_bypasses.org::*Double URL Encoding).

### Start of Path Checks

Some web applications that allow users to access the files using an absolute path, check whether the path provided by the user starts with a certain path. This can easily be bypasses using the `../` method by sending a request like `?path=/tmp/access/../../../../etc/passwd`. This can be combined with previous techniques to bypass any other protections of they exist.

### Validation of File Extension

This is a tough one, however sometimes, when an application checks the end of string, without controlling for null bytes, we can add a `%00` right before the file extension in order to trick the web application into thinking we are sending a valid request while the operating systems accesses the file without the extension since a null byte is used as a string t