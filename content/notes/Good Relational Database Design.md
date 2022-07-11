---
title: What makes a Relational Database Design Good?
date: 2021-12-14T20:32:21+01:00
tags: ['cs/databases']
---
* **Minimal Redundancy:** The less a database repeats the data in it, the better. Redundancy can cause issues such as [[notes/Deletion Anomalies|Deletion Anomalies]]
* **Prevents Modification Anomalies by Design:** This means anomalous modifications are prevented by using keys, not by enforcing an excessive amount of contraints. Otherwise, [[notes/Update Anomalies|Update Anomalies]] may occur.
* **Matching the used RDBMS:** This provides faster query processing, but for this, redundancy can be necessary.