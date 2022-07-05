
## Datastructure

docker stop cranky_wing

### List

- Collection of string
- Sorted by insertion order
- Insertion allowed from both ends
- Supported producing, consumer style design, event queue sort of application
- Operations
    - LPUSH -> add element to the head/left
    - RPUSH -> add element to the tail/right
    - LINSERT -> add element to a specific location
    - LRANGE -> Return specific element of the list using zero based offset (negetive indexing allowed)
    - LLEN -> Return list length, 0 for non existing/empty list
    - LPOP -> Remove and return element from the list from left
    - RPOP -> Remove and return element from the list from right


> Pushing new element to an non existing list create the list, again removing last element to an existing list removes the list.

```
127.0.0.1:6379> LPUSH list01 "Ali"
(integer) 1
127.0.0.1:6379> LPUSH list01 "Dab"
(integer) 2
127.0.0.1:6379> LPUSH list01 "Jad"
(integer) 3
127.0.0.1:6379> LPUSH list01 "Jew"
(integer) 4

127.0.0.1:6379> RPUSH list01 "Pre"
(integer) 5

127.0.0.1:6379> LRANGE list01 0 -1
1) "Jew"
2) "Jad"
3) "Dab"
4) "Ali"
5) "Pre"
127.0.0.1:6379> LRANGE list01 2 3
1) "Dab"
2) "Ali"

127.0.0.1:6379> LLEN list01
(integer) 5

127.0.0.1:6379> LPOP list01
"Jew"
127.0.0.1:6379> LRANGE list01 0 -1
1) "Jad"
2) "Dab"
3) "Ali"
4) "Pre"
127.0.0.1:6379> RPOP list01
"Pre"
127.0.0.1:6379> LRANGE list01 0 -1
1) "Jad"
2) "Dab"
3) "Ali"

127.0.0.1:6379> LINSERT list01 BEFORE "Dab" "Aab"
(integer) 4
127.0.0.1:6379> LRANGE list01 0 -1
1) "Jad"
2) "Aab"
3) "Dab"
4) "Ali"
```

### Set

- Unordered collection of unique strings
- Other than uniqueness its more or less like List
- Have server side option to create set from existing set
- Operations
    - SADD -> add element to the set, in case value already exist it will be ignored
    - SREM -> removed element from set
    - SISMEMBER -> Test to check element exist in Set, 1 if exist else 0
    - SCARD -> Count of set, 0 if empty/not exist
    - SMOVE -> Move element from one set to another
    - SUNION -> Combine two sets
    - SDIFF -> Return elements which is different between two sets
    - SRANDMEMBER -> Return random member from set, if you put additional number as an argument it will return that many random elements
    - SPOP -> Removed and return random element from a set, you can add additional argument to delete more than one elements
    


```
127.0.0.1:6379> SADD set01 "01"
(integer) 1
127.0.0.1:6379> SADD set01 "01"
(integer) 0
127.0.0.1:6379> SADD set01 "02"
(integer) 1
127.0.0.1:6379> SADD set01 "03"
(integer) 1

127.0.0.1:6379> SMEMBERS set01
1) "02"
2) "01"

127.0.0.1:6379> SISMEMBER set01 "02"
(integer) 1
127.0.0.1:6379> SISMEMBER set01 "022"
(integer) 0

127.0.0.1:6379> SMOVE set01 set02 "01"
(integer) 1
127.0.0.1:6379> SMEMBERS set02
1) "01"

127.0.0.1:6379> SADD set02 "09"
(integer) 1
127.0.0.1:6379> SUNION set01 set02
1) "01"
2) "09"
3) "02"
4) "03"

127.0.0.1:6379> SRANDMEMBER set01
"03"
127.0.0.1:6379> SRANDMEMBER set01 2
1) "02"
2) "03"

127.0.0.1:6379> SPOP set02
"01"
127.0.0.1:6379> SMEMBERS set02
1) "09"

```

### Sorted Set

- Every member will have a score which allow us to sort elements
- Other than the score it is eaxctly a set
- Property of score
    - Score is required
    - Score doesnot need to be unique
    - Score are float (if you give number it will convert to float)
- Operations
    - ZADD -> Adds element
    - ZREM -> Remove element
    - ZRANGE -> Fetch value of specific range, from high to lowest score
    - ZREVRANGE -> Fetch value of specific range, from lowest to highest score
    - ZRANGEBYSCORE -> Fetch value of specific range by score, from high to lowest score
    - ZRANK -> Returns ranks value of specific range, from high to lowest score. Rank are 0 based
    - ZREVRANK -> Returns ranks value of specific range, from lowest to highest score 
    - ZCARD -> Number of element in sorted set
    - ZCOUNT -> Number of element in sorted set within specific range of score
    - ZINCRBY -> Increment the score of a member, if member doesnot exist it will add it, score increment and decrement (with negetive number) should be float
    - ZSCORE -> Return score of a number

```
127.0.0.1:6379> ZADD age 1984 "dab"
(integer) 1
127.0.0.1:6379> ZADD age 1985 "ali"
(integer) 1
127.0.0.1:6379> ZADD age 1982 "jad"
(integer) 1
127.0.0.1:6379> ZRANGE age 0 -1
1) "jad"
2) "dab"
3) "ali"
127.0.0.1:6379> ZRANGEBYSCORE age 1980 1983
1) "jad"

127.0.0.1:6379> ZRANK age "dab"
(integer) 1
127.0.0.1:6379> ZRANK age "ali"
(integer) 2
127.0.0.1:6379> ZRANK age "jad"
(integer) 0
127.0.0.1:6379> ZREVRANK age "jad"
(integer) 2

127.0.0.1:6379> ZCARD age
(integer) 3

127.0.0.1:6379> ZINCRBY age 1 "ali"
"1986"
127.0.0.1:6379> ZSCORE age "ali"
"1986"
```


### Hash

- Map between string field and string value
- Operations
    - HSET -> Set field in Hash, if it doesnot exist a new key is created if already exist it will be overwritten
    - HMSET -> Set multiple fields, overwrite if already exist
    - HGET -> Returns value associated with Hash, if not exist retrun NIL
    - HMGET -> Return value for multiple fields
    - HGETALL -> Returns all fields in an hash
    - HDEL -> Remove specific fields
    - HEXISTS -> Check if feilds exist in hash, 0 for not 1 for exist
    - HINCRBY -> Increment number in value of a key in hash, if key doesnot exist it creates it
    - HKEYS -> Returns all key names
    - HLEN -> Number of key in hash
    - HVALS -> Return all the values
    - HSTRLEN -> Return string length of value associated with a key in hash

```
127.0.0.1:6379> HMSET emp:alif name "Alif" age 36 city "belmundi"
OK
127.0.0.1:6379> HSET emp:dabli name "Kaoushk"
(integer) 1
127.0.0.1:6379> HSET emp:dabli city "belghoria"
(integer) 1

127.0.0.1:6379> HGET emp:alif name
"Alif"
127.0.0.1:6379> HGET emp:dabli city
"belghoria"
127.0.0.1:6379> HGET emp:dabli name
"Kaoushk"
127.0.0.1:6379> HMGET emp:alif name city age
1) "Alif"
2) "belmundi"
3) "36"

127.0.0.1:6379> HGETALL emp:alif
1) "name"
2) "Alif"
3) "age"
4) "36"
5) "city"
6) "belmundi"

127.0.0.1:6379> HKEYS emp:alif
1) "name"
2) "age"
3) "city"
127.0.0.1:6379> HVALS emp:alif
1) "Alif"
2) "36"
3) "belmundi"

127.0.0.1:6379> HINCRBY emp:alif age 1
(integer) 37
127.0.0.1:6379> HGET emp:alif age
"37"

127.0.0.1:6379> HDEL emp:alif age
(integer) 1
127.0.0.1:6379> HKEYS emp:alif
1) "name"
2) "city"

127.0.0.1:6379> HLEN emp:alif
(integer) 2

```