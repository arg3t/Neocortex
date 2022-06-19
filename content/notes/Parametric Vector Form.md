---
title:  Parametric Vector Form
date: 2022-02-27T11:11:01+01:00
description: 
tags: ['math/linear']
aliases: ['']
---
In order to convert a linear system into parametric vector form, first the matrix must be converted to reduced echeleon form. Afterwards, the free variables (the columns that do not have any pivot points) and the basic variables are determined. And then, the equations for each row in the matrix are written down so that the basic variables are represented by the free variables. And then the equations are converted into a summation of vectors and the solutions can simply be generated using that form. Here is a sample solution:

$$
\begin{bmatrix}
-2 & 1 & -4 & 1 \\
-1 & 1 & -1 & 0 \\
0 & 1 & 2 & -1
\end{bmatrix}x = 
\begin{bmatrix}
4 \\
1 \\
-2
\end{bmatrix}
$$

$$
\begin{bmatrix}
1 & 0 & 3 & -1 \\
0 & 1 & 2 & -1 \\
0 & 0 & 0 & 0
\end{bmatrix}x = 
\begin{bmatrix}
-3 \\
-2 \\
0
\end{bmatrix}
$$

$$ 
\begin{cases}  
-3 = x_1 + 3x_3 - x_4 \\
-2 = x_2 + 2x_3 - x_4 \\
x_3 = s \\
x_4 = t
\end{cases} 
$$

$$ 
\begin{cases}  
x_1 = x_4 - 3x_3 - 3 \\
x_2 = x_4 - 2x_3 - 2 \\
x_3 = s \\
x_4 = t
\end{cases} 
$$

$$
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4
\end{bmatrix} = 
s\begin{bmatrix}
-3 \\
-2 \\
1 \\
0
\end{bmatrix} + 
t\begin{bmatrix}
1 \\
1 \\
0 \\
1
\end{bmatrix} +
\begin{bmatrix}
-3 \\
-2 \\
0 \\
0
\end{bmatrix}
$$