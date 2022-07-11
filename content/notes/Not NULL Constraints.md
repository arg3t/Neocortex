---
title: Not NULL Constraints
date: 2021-12-14T20:32:21+01:00
tags: ['cs/databases', 'cs/theory']
---
Because of the fact that a relation is defined as $R \subseteq D_1 \times D_2 ... \times D_n$, and a tuple(which represents a relation) cannot have empty elements, We assume that a special NULL value is part of every domain. When we don't want an element to be NULL, we give it the NOT NULL constraint. Keep in mind that [[notes/Primary Key Constraints|Primary Key Constraints]] also automatically have NOT NULL constraints.