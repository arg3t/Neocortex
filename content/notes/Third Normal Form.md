---
title: 3rd Normal Form (3NF)
date: 2021-12-14T20:32:21+01:00
---
Any 3NF schema must also be in [[notes/Second Normal Form|2nd Normal Form (2NF)]]. The only extra requirement is that there is no [[notes/Transitive Dependency|Transitive Dependency]] between the [[notes/Primary Key|Primary Key]] of the relation and another attribute.

In order to convert a [[notes/Relational Model|Relational Model]] in 2NF to 3NF, we apply [[notes/Projection|Projection $\pi$]] on the functional dependency that is causing the dependency.