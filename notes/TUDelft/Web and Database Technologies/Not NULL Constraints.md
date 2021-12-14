---
title: Not NULL Constraints
date: 2021-12-01
---
## Not NULL Constraints
Because of the fact that a relation is defined as $R \subseteq D_1 \times D_2 ... \times D_n$, and a tuple(which represents a relation) cannot have empty elements, We assume that a special NULL value is part of every domain. When we don't want an element to be NULL, we give it the NOT NULL constraint. Keep in mind that [[Primary Key Constraints]] also automatically have NOT NULL constraints.