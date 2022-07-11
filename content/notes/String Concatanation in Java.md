---
title: String Concatantion in Java
date: 2021-11-16T21:07:41+01:00
---
>  ...strings in Java are immutable objects. Once created, an instance cannot be modified. The command, answer += c, is shorthand for answer = (answer + c). This command does not cause a new character to be added to the existing String instance; instead it produces a new String with the desired sequence of characters, and then it reassigns the variable, answer, to refer to that new string.
>  In terms of efficiency, the problem with this interpretation is that the creation of a new string as a result of a concatenation, requires time that is proportional to the length of the resulting string...
>  
>  (Data Structures and Algorithms, Michael Goodrich (Page 172))

So, this means that any operation involving string concatanation run in O(n) time (see [[notes/Big-Oh Notation|Big-Oh Notation]]), n being the length of the string.