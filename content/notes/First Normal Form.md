---
title: 1st Normal Form (1NF)
date: 2021-12-14T20:32:21+01:00
tags: ['cs/databases']
---
1st normal form is the simplest of the [[notes/Normal Forms|Normal Forms]], it has no requirements for different types of functional dependencies. It only has two requirements:
* That the relations in the schema must be flat.
* That each attribute needs to be atomic, meaning it cannot be made up from multiple attributes. If you have a component with a cardinality more than one for instance, you can solve this by either replicating the tuple for each value of the attribute or by introducing a new relation instead of the attribute.