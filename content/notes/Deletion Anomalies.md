---
title: Deletion Anomalies
date: 2021-12-14T20:32:21+01:00
tags: [ 'cs/databases']
---
When you have a redundant database and you delete all tuples that contain a certain value for a certain attribute. All data on that attribute is lost, making it impossible to create new tuples with that attribute.

For instance, in the table:

| student_id | student_name | class |
|------------|--------------|-------|
| 1 | yigit | Java|
| 2 | ipek| Web and Database|

When you delete the student yigit, all information on the class Java is lost. In order to prevent such cases, it is a good idea to apply [[notes/Relational Database Normalization|Normalizing a Relational Model]] to your database.