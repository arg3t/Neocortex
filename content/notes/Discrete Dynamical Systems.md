---
title:  Discrete Dynamical Systems
date: 2022-03-21T09:41:18+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
If you are dealing with a system whose state can be described by a list of numbers, you can describe the state using a [[/notes/Vectors|vector]], and the different states of the system can be shown using a [[/notes/Linear Transformations|linear transformation]]. These types of systems are called **discrete dynamical systems** and each state is calculated using the formula:

$$
x_{n+1} = Ax_{n} = A^nx_0
$$

Where $A$ is the state matrix and $x_0$ is the initial state of the system. When [[Solving Discrete Dynamical Systems|solving discrete dynamical systems]], [[/notes/Diagonalization|Diagonalization]] proves to be a very useful technique.