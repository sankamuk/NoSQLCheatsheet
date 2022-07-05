
## Scan

- Allows in itterating over keys
- Return result in batches (Good to run in Prod scenario)
- Takes position in Key set as a parmeter
- Guarantee
    - Full scan return all elements
    - Never return any element thats was not there in collection from start to finish

- Example 1 - Scan all element (default 10 element at a time)

```
127.0.0.1:6379> MSET 1 "1" 2 "2" 3 "3" 4 "4" 5 "5" 6 "6" 7 "7" 8 "8" 9 "9" 10 "10" 11 "11" 12 "12" 13 "13" 14 "14"
OK
127.0.0.1:6379> SCAN 0
1) "11"
2)  1) "7"
    2) "5"
    3) "11"
    4) "4"
    5) "1"
    6) "6"
    7) "14"
    8) "8"
    9) "13"
   10) "10"
   11) "9"
127.0.0.1:6379> SCAN 11
1) "0"
2) 1) "12"
   2) "3"
   3) "2"
127.0.0.1:6379>
```

- Example 2 - Scan all element 3 element at a time

```
127.0.0.1:6379> SCAN 0 COUNT 3
1) "6"
2) 1) "7"
   2) "5"
   3) "11"
   4) "4"
127.0.0.1:6379> SCAN 6 COUNT 3
1) "13"
2) 1) "1"
   2) "6"
   3) "14"
127.0.0.1:6379> SCAN 13 COUNT 3
1) "11"
2) 1) "8"
   2) "13"
   3) "10"
   4) "9"
127.0.0.1:6379> SCAN 11 COUNT 3
1) "7"
2) 1) "12"
   2) "3"
   3) "2"
127.0.0.1:6379> SCAN 7 COUNT 3
1) "0"
2) (empty list or set)
127.0.0.1:6379>
```

- Example 3 - Scan all element with matching key

```
127.0.0.1:6379> SCAN 0 MATCH 1*
1) "11"
2) 1) "11"
   2) "1"
   3) "14"
   4) "13"
   5) "10"
127.0.0.1:6379> SCAN 11 MATCH 1*
1) "0"
2) 1) "12"
```

## Keys

- Search all mathcing keys (no per batch traversal, thus to be used carefully in Prod)
- Allow pattern based search
    - */?/[]/[-]/ all are supported

- Example 4 - Key based matching

```
127.0.0.1:6379> KEYS 1*
1) "13"
2) "10"
3) "14"
4) "1"
5) "11"
6) "12"
127.0.0.1:6379> KEYS 1[23]
1) "13"
2) "12"
127.0.0.1:6379> KEYS 1[2-5]
1) "13"
2) "14"
3) "12"
127.0.0.1:6379> KEYS ??
1) "13"
2) "10"
3) "14"
4) "11"
5) "12"
```

## Randomkey

- Gives back random key

- Example 5 - Randomkey

```
127.0.0.1:6379> RANDOMKEY
"6"

```

