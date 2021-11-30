## Foreign Key Constraints
Sometimes, a relation might need to me make a reference to another relation. In those cases, we use the following notation:
Hero(<ins>id</ins>, first_name, last_name)
Aliases(<ins>alias</ins>, heroid -> Hero)
in order to protect the **referential integrity** of the database, we set the constraint that a referencing attribute must be the key of a tuple that is in the database.
When you have a composite key, the notation becomes:
Hero(<ins>id</ins>, <ins>first_name</ins>, last_name)
Aliases(<ins>alias</ins>, hero_id, hero_name, (hero_id, hero_name) -> Hero)
