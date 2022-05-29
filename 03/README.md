
## Compare RDBMS and NoSQL

- RDBMS works with ACID, i.e. Atomic, Consistency, Isolation and Durability
- NoSQL work with BASE, i.e. Basic Availability, Soft State, Eventual Consistency

## Choice of NoSQL


|CAP Support|NoSQL Data Type|Database|
|---|---|---|
|AP|Key Value|DynamoDB|
|AP|Document|CouchDB|
|AP|Wide Column|Cassandra|
|CA|Graph|Neo4j|
|CP|Key Value|Redis|
|CP|Document|MongoDB|
|CP|Wide Column|HBase|

> Also do look into your developer comfort and maximum Usage (Open Source) and quality support (Commercial) should govern your design choice.


