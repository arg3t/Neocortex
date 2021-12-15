---
title: 2nd Normal Form (2NF)
date: 2021-12-14T20:32:21+01:00
---
## 2nd Normal Form (2NF)
Any 2NF schema must also be 1NF, however, there are some extra requirements for a [[Relational Model]] to be 2NF. It must not contain any [[Partial Dependency]]s.

In order to apply [[Relational Database Normalization]] to a relation that has a [[Partial Dependency]], we apply a [[Projection]] over the relation with two sets of attributes, one of which being the attributes that *define* the dependency and the attributes that depend on the dependency, and the other one being the original relation with the dependants of the dependency removed.