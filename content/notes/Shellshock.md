---
title: Shellshock
date: 2022-08-20T14:19:34+02:00
tags: ['cs/security']
aliases: ['']
---

Shellshock is a vulnerability with code
[CVE-2014-6271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271).
The bug occurs because bash processes trailing strings after function
definitions in the values of environment variables. This allows an attacker to
overwrite a binary that the bash script is calling with a function and run
arbitrary code.

## Checking for shellcode
```
env x='() { :;}; echo vulnerable' bash -c 'echo hello'
```
