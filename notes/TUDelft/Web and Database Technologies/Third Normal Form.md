---
title: 3rd Normal Form (3NF)
date: 2021-12-13
---
## 3rd Normal Form (3NF)
Any 3NF schema must also be in [[Second Normal Form]]. The only extra requirement is that there is no [[Transitive Dependency]] between the [[Primary Key]] of the relation and another attribute.

In order to convert a [[Relational Model]] in 2NF to 3NF, we apply [[Projection]] on the functional dependency that is causing the dependency.