---
title: Converting to a [[Relational Model]]
date: 2021-12-13
---
## Converting to a [[Relational Model]]
Even though [[ER Diagrams]] contain more semantic information, they are harder to turn into actual databases because some of the constraints are impossible to represent.

### Simple Entities
When you have an entitity without any relations connected to it, all you need to do is to create an entry in the schema with the given attributes.

### N:M Relation Type
With an N:M relationship, you need to create a new entry in the schema to represent that relation. Here is a more visual example:
![[2F8F54F0-8071-4BA7-9A5D-00D35EC80228.jpeg]]

### 1:M Relationship
In this case you just push the relationship information to the side with the * cardinality.
![[367FF726-2F89-4733-A3B2-EFF81FB72BB7.jpeg]]

### 1:1 Cardinality
Same as the 1:M one, just need to pick a side to put the relation.

### Attributes Attached to Relation
When attributes are attached to a relation, you simply add another attribute to the relation.

### [[ER Diagrams Weak Entity and Identifying Relationship]]
Since weak entities are defined using the identifying relationship, you put the relationship in the weak entity.

### Composite Attributes
You just flatten them

### Multi-Attribute
Treat the attribute as a relation and create a new relation with a cardinality of 1:N.

### Inherited Attributes and Relations
Create a single entity that contains all the attributes and relations from all types and add an extra attribute type.