
## NoSQL DB Concepts

### Strength

- Scalable
- Flexible
- Fast
- No strict structure imposition, data record can vary from one another
- Fields may vary from one record to another
- 

While RDBMS provide:

- Reliable
- Consistent
- Excellent Integrity (implemented by constrains like Primary Key, Foreign Keys)
- Follow strict structure
- Excellent support to map transactional systems
- All data record has every data field (even if it is NULL)

### CAP Theorem

Name is an abbreviation for Consistency, Availability and Partition Tolerance
It's a Computing concept, directed to Data Storage systems. The theorem claims in case of distributed data storage (***P***artitioned) system Network failure it is possible to provide either ***C***onsistency or ***A***vailability.

> Note RDBMS is generally not distributed this it's not scoped and targets mostly Consistency.

Different Non-Relational DB systems:

- 1 - Consistency & Availability - Neo4j
- 2 - Consistency & Partition Tolerance - MongoDB, HBase, Redis
- 3 - Partition Tolerance & Availability - CouchDB, Cassandra and DynamoDB

> Since without Consistency there is usability of data storage systems the one above which does not support Consistency, provide something called ***Eventual Consistency***.

Now let's explain implementation difference in 2 & 3:

- In Type 2 Availability os provided by Replication but to provide Consistency READ & WRITE allowed from one system (Active). But if Active is unavailable there is lag in transforming Non-Active to Active.
- In Type 3 only WRITE allowed from one system (Active) while READ allowed from Non-Active also. But since READ allowed from Non-Active leading to inconsistent READ.

