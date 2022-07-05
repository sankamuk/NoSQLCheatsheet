
## Key Value Pair

- Commands already discussed
    - SET -> Set string value for a Key
    - GET -> Get value for a Key
    - DEL -> Delete a Key
    - EXISTS -> Check if Key exists
    - INCR -> Increament value of Key by 1
    - INCRBY -> Increament value of Key by a number
    - DECR -> Decreament value of Key by 1
    - DECRBY -> Decreament value of Key by a number

- MSET 

    - Allow setting multiple key values
    - Replace existing value with new one


```
127.0.0.1:6379> MSET k1 100 k2 200
OK
127.0.0.1:6379> GET k1
"100"
127.0.0.1:6379> GET k2
"200"
```

- MSETNX 

    - Allow setting multiple key values, ***only*** if they do not exist
    - None will work even if one Key exists

```
127.0.0.1:6379> GET k2
"200"
127.0.0.1:6379> MSETNX k2 30 k4 50
(integer) 0
127.0.0.1:6379> GET k2
"200"
127.0.0.1:6379> GET k3
(nil)
```

- MGET 

    - Allow getting multiple key values
    - Returns nil if Key doesnot exist


```
127.0.0.1:6379> MGET k1 k5 k2
1) "100"
2) (nil)
3) "200"
```

- APPEND 

    - Allow appending value to an already existing key's value
    - In case Key doesnot exist APPEND behave like SET


```
127.0.0.1:6379> APPEND k1 10
(integer) 5
127.0.0.1:6379> GET k1
"10010"
127.0.0.1:6379> APPEND k3 10
(integer) 2
127.0.0.1:6379> GET k3
"10"
```

- GETRANGE 

    - Substring of a string value, ofset start and end value need to be provided
    - Negetive offset are allowed

```
127.0.0.1:6379> GET k1
"10010"
127.0.0.1:6379> GETRANGE k1 1 2`
"00"
127.0.0.1:6379> GETRANGE k1 -2 -1
"10"
```

> To get the complete string a range of 0 to -1 could be used.

- RENAME

    - Rename a Key
    - Error if key doesnot exist

```
127.0.0.1:6379> SET k1 100
OK
127.0.0.1:6379> GET k1
"100"
127.0.0.1:6379> GET k2
(nil)
127.0.0.1:6379> RENAME k1 k2
OK
127.0.0.1:6379> GET k1
(nil)
127.0.0.1:6379> GET k2
"100"
127.0.0.1:6379> RENAME k1 k2
(error) ERR no such key

```

- GETSET

    - Works like SET, but it retruns old value

```
127.0.0.1:6379> GET k1
(nil)
127.0.0.1:6379> GET k2
"100"
127.0.0.1:6379> GETSET k2 200
"100"
127.0.0.1:6379> GET k2
"200"
127.0.0.1:6379> GETSET k1 200
(nil)
127.0.0.1:6379> GET k1
"200"
```

- SETEX 

    - SET value to Key with timeout
    - Almost like SET and EXPIRE in one command

```
127.0.0.1:6379> SETEX k5 10 100
OK
127.0.0.1:6379> GET k5
"100"
127.0.0.1:6379> GET k5
(nil)
```

- PSETEX 

    - Same as SETEX except the timeout is in milliseconds

- PTTL 

    - Same as TTL except it shows time in milliseconds for a Key to exist


- PERSIST 

    - Removes timeout of an Key
    - Its opposite of EXPIRE

```
127.0.0.1:6379> SETEX k5 15 100
OK
127.0.0.1:6379> TTL k5
(integer) 11
127.0.0.1:6379> PERSIST k5
(integer) 1
127.0.0.1:6379> TTL k5
(integer) -1
127.0.0.1:6379> GET k5
"100"
127.0.0.1:6379> TTL k5
(integer) -1
127.0.0.1:6379> EXPIRE k5 10
(integer) 1
127.0.0.1:6379> TTL k5
(integer) 8

```

- SETNX 

    - Same as SET if key doesnot exist
    - If Key exist it doesnot reset value

```
127.0.0.1:6379> GET k1
"200"
127.0.0.1:6379> GET k3
(nil)
127.0.0.1:6379> SETNX k1 100
(integer) 0
127.0.0.1:6379> SETNX k3 100
(integer) 1
127.0.0.1:6379> GET k1
"200"
127.0.0.1:6379> GET k3
"100"
```

- MSETNX

    - Same as SETNX but for multiple key value pair
    - Note of one Key exist then no keys will be set

```
127.0.0.1:6379> GET k3
"100"
127.0.0.1:6379> GET k4
(nil)
127.0.0.1:6379> MSETNX k3 200 k4 100
(integer) 0
127.0.0.1:6379> GET k4
(nil)
127.0.0.1:6379> GET k3
"100"
```

- RENAMENX

    - Same as RENAME except the target should be new one
    - In case target exist the RENAME fails

```
127.0.0.1:6379> GET k1
"100"
127.0.0.1:6379> GET k3
"100"
127.0.0.1:6379> GET k4
(nil)
127.0.0.1:6379> RENAMENX k1 k3
(integer) 0
127.0.0.1:6379> GET k1
"100"
127.0.0.1:6379> RENAMENX k1 k4
(integer) 1
127.0.0.1:6379> GET k1
(nil)
127.0.0.1:6379> GET k4
"100"
```

