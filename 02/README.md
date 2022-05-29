
## Common Property of a NoSQL Database System

- Handles unstructured data
- Handles large amount of data
- Handles large volume of clients simultaneously

## NoSQL Database System Types

- Key Valued
- Document
- Wide Column
- Graph

## Key Valued

- Simple storage, e.g cache
- Basis data type support, e.g. user profile, monitoring, session caching
- Very easily scalable
- Redis is the most common example, also DynamoDB becoming very popular

## Document 

- Key Valued but the value are document
- It can support systems like CMS (content management system), large document storage
- Allow query not only on key but also on attribute of value but not complex query
- MongoDB is most common, also Azure CosmosDB, CouchDB are becoming very popular

## Wide Column 

- Subset of Key Value
- Has concepts of Table, Row & Columns like RDBMS
- Columns (type, number, name) can vary row to row
- Unlike RDBMS one should focus on the Query when designing not the data
- Support large volume of data
- HBase is most common, Cassandra also becoming very popular

## Graph 

- Data stored in nodes and relationship established between nodes
- It can represent multidimensional complex relationship between nodes
- But not good for general purpose and simple relationship
- Neo4j is most common


