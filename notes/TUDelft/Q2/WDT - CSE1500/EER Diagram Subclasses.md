---
title: ER Diagram Subclasses and Superclasses
date: 2021-11-23
---
## ER Diagram Subclasses and Superclasses
Sometimes when drawing[[ER Diagrams]], sometimes you need to represent a subclass and superclass relationship between entities when they share attributes and relations. In order to represent this, we have disjoint and overlapping subclass relationships. If a subclass entity is overlapping, an entity can belong to multiple entity types of those subclasses. In disjoint relationships, an entity can belong to only one entity type. More importantly, when defining subclass relationships, the connection between the disjoint/overlapping and the superclass entity should be total participation ([[ER Diagram Total Participation]]) so that every entity belonging to the superclass must be a subclass.

![[20211123145942.png]]