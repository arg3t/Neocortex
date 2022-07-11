---
title: 2nd Normal Form (2NF)
date: 2021-12-14T20:32:21+01:00
---
Any 2NF schema must also be 1NF, however, there are some extra requirements for a [[notes/Relational Model|Relational Model]] to be 2NF. It must not contain any [[notes/Partial Dependency|Partial Dependency]]s.

In order to apply [[notes/Relational Database Normalization|Normalizing a Relational Model]] to a relation that has a [[notes/Partial Dependency|Partial Dependency]], we apply a [[notes/Projection|Projection $\pi$]] over the relation with two sets of attributes, one of which being the attributes that *define* the dependency and the attributes that depend on the dependency, and the other one being the original relation with the dependants of the dependency removed.