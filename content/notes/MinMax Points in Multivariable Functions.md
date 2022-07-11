---
title:  MinMax Points in Multivariable Functions
date: 2022-01-19T05:04:58+01:00
description: 
tags: ['math/multivar', 'math/calculus']
aliases: ['']
---
[[notes/Multivariable Functions|Multivariable Functions]] have minima and maxima points, which can be found using [[notes/Critical Points Multivariable Functions|critical points]]. After finding them,  in order to check whether they are minima, maxima or saddle points, we can either apply the second [[notes/Partial Derivatives|partial derivate]] test which goes like:

$$
D = f_{xx}(a,b)f_yy(a,b) - f_{xy}(a,b)^2
$$

* if $D > 0$ and $f_xx(a,b) > 0$, then $(a,b)$ is a maxima
* if $D > 0$ and $f_xx(a,b) < 0$, then $(a,b)$ is a minima
* if $D < 0$ then $(a,b)$ is a saddle point.
* Otherwise, the test is inconclusive

You can also look at the [[notes/Level Lines|Level Lines]] of the function and infer from there:

> In a level map, if two lines intersect, that point is a saddle point
