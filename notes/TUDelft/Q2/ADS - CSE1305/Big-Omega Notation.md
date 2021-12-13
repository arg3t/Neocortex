---
title: Big Omega Notation
date: 2021-11-16
---
## Big Omega Notation
The big omega notation $\Omega(n)$ is basically the opposite of [[Big-Oh Notation]], what it does is that it shows the time an algorithm in the best-case relative to its input size, n. Here is how you calculate it:

### Calculating Big-Omega
Since big omega basically does what Big-Oh does, the definition is just slightly different, we still need two integers $c$ and $n_0$, but this time $f(n)$ must be greater than or equal to $c\times g(n)$ for all $n > n_0$ in order for $f(n)$ to be $\Omega(g(n))$. Here is the definition in predicate logic:

  $$\exists c,n_0(\forall x(x \geq n_0 g \implies f(x) \geq cg(x))) \implies f(n) \in \Omega(g(n))$$