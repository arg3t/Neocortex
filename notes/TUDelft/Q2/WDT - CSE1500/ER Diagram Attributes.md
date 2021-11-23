## ER Diagram Attributes
Attributes can be represented in [[ER Diagrams]] using an ellipse connecting to an attribute. However, there other ways to do that as well.

![[20211123104136.png]]

In this example, attributes are represented using circles. An empty circle has a cardinality of (1,1) which means that every entity must have that attribute and it can only have one of them. You can also specify the cardinality in the attribute, which is what was done in the Job attribute. Also, you can give an attribute with the cardinality of (N,1) using a circle in a circle.

It is also possible to create **composite attributes**, attributes that are made of smaller parts. One example to that is Date, which is made of day, month and year.

![[20211123104817.png]]

In this notation, it is possible to also represent **derived attributes**, attributes which are made of/calculated from other attributes.

![[20211123105108.png]]