---
title: ER Diagram Subclasses and Superclasses
date: 2021-11-23T14:10:26+01:00
tags: [ 'cs/databases']
---
Sometimes when drawing[[/notes/ER Diagrams|ER Diagrams]], sometimes you need to represent a subclass and superclass relationship between entities when they share attributes and relations. In order to represent this, we have disjoint and overlapping subclass relationships. If a subclass entity is overlapping, an entity can belong to multiple entity types of those subclasses. In disjoint relationships, an entity can belong to only one entity type. More importantly, when defining subclass relationships, the connection between the disjoint/overlapping and the superclass entity should be total participation ([[/notes/ER Diagram Total Participation|Total Participation in ER Diagrams]]) so that every entity belonging to the superclass must be a subclass.

![[images/20211123145942.png]]