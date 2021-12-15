---
title: Transitive Dependency
date: 2021-12-14T20:32:21+01:00
---
## Transitive Dependency
Let's say in your [[Relational Model]], you have two [[Functional Dependency]]s as such:

```
{A} -> {B}
{B} -> {C}
```
However the dependency `{A}->{C}` is not specified. Because of the transitive property of the functional dependency relation, this dependency can be inferred. This is called a transitive dependency.