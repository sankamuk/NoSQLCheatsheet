
## Redis Storage Design

***Storing***

- Key-Value are the building blocks so no limit to number of the same.
- Every record should be key-ed.
- Spend most time in designing the Key, consider namespacing (with :) and it should be treated as Primary Key.

***Retrieval***

- To search single record, you should be able to create the key.
- For searching a range you should rely on wild card (*).

***Example***

|id|name|Salary|
|---|---|---|
|1|Dab|1500|
|2|Prem|1600|
|3|Ali|1300|

- Storage 

```commandline
127.0.0.1:6379> HMSET EMP:1 name Dab salary 1500
OK
127.0.0.1:6379> HMSET EMP:2 name Prem salary 1600
OK
127.0.0.1:6379> HMSET EMP:3 name Ali salary 1300
OK
```

- Access Single Record

```commandline
127.0.0.1:6379> HGETALL EMP:1
1) "name"
2) "Dab"
3) "salary"
4) "1500"
```

- Access All Employee

```commandline
127.0.0.1:6379> SCAN 0 MATCH EMP:*
1) "0"
2) 1) "EMP:3"
   2) "EMP:2"
   3) "EMP:1"
   
127.0.0.1:6379> KEYS EMP:*
1) "EMP:3"
2) "EMP:2"
3) "EMP:1"
```

> In below example our search pattern and primary key is dependent on both id and name

|id|name|salary|city
|---|---|---|---|
|1|Dab|1500|Kol|
|2|Prem|1600|Bel|
|3|Ali|1300|How|

- Storage 

```commandline
127.0.0.1:6379> HMSET EMP:1:Dab salary 1500 city Kol
OK
127.0.0.1:6379> HMSET EMP:2:Prem salary 1600 city Bel
OK
127.0.0.1:6379> HMSET EMP:3:Ali salary 1300 city How
OK
```

- Access Single Record

```commandline
127.0.0.1:6379> HGETALL EMP:1:Dab
1) "salary"
2) "1500"
3) "city"
4) "Kol"
```

- Access All Employee

```commandline
127.0.0.1:6379> KEYS EMP:*:D*
1) "EMP:1:Dab"
127.0.0.1:6379> KEYS EMP:*:Prem
1) "EMP:2:Prem"

```

