---
title: Weak Entity and Identifying Relationship in ER Diagrams
date: 2021-11-23
---
## Weak Entity and Identifying Relationship in ER Diagrams
A weak entity in [[ER Diagrams]] is an entity type that depends on another entity for its existence and cannot exist without it. En example of a weak entity is a Student and a University, in this example, the Student is a weak entity. Since a student can't exist without a university. Another thing to consider is that the student's number is only identifying inside that university, so, we need a way to specify that inside our diagram. For this, we use an **identifying relationship**. Also, since a weak entity, cannot exist without the class it is identified by, every instance of that entity must relate to at least one of those entities. Again, for this, we use **total participation**([[ER Diagram Total Participation]]).

![[20211123111244.png]]