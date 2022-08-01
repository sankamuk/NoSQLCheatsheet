
# Publish Subscribe

Redis can be used as a PUB-SUB broker.

- Step 1: Subscribe a client

```commandline
127.0.0.1:6379> SUBSCRIBE TOPIC01
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "TOPIC01"
3) (integer) 1
```

> Note your cli will not return prompt signifying client waiting for new message

- Step 2: Publish message from different client

```commandline
127.0.0.1:6379> PUBLISH TOPIC01 "hello clients"
(integer) 1
```

- Step 3: First client listing should receive the message

```commandline
1) "message"
2) "TOPIC01"
3) "hello clients"
```

> Note there could be multiple client subscribing to topic
> You can not do 'UNSUBSCRIBE' in cli but if you use telnet you can do it, for CLI you should use CONTROL+D
> You can SUBSCRIBE multiple channels like SUBSCRIBE TOPIC01 TOPIC02

- Step 4: Pattern based subscription

> Publish

```commandline
127.0.0.1:6379> PUBLISH NEWS:SPORTS "India won ICC WC 2022"
(integer) 1
``` 

> Subscribed client

```commandline
127.0.0.1:6379> PSUBSCRIBE NEWS:*
Reading messages... (press Ctrl-C to quit)
1) "psubscribe"
2) "NEWS:*"
3) (integer) 1
1) "pmessage"
2) "NEWS:*"
3) "NEWS:SPORTS"
4) "India won ICC WC 2022"
```

- Check Subscription

> Subscribe client

```commandline
127.0.0.1:6379> SUBSCRIBE NEWS:SPORTS
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "NEWS:SPORTS"
3) (integer) 1
1) "message"
2) "NEWS:SPORTS"
3) "India won ICC WC 2022"
```

> Publish and Check subscription

```commandline
127.0.0.1:6379> PUBLISH NEWS:SPORTS "India won ICC WC 2022"
(integer) 1
127.0.0.1:6379> PUBSUB CHANNELS
1) "NEWS:SPORTS"
127.0.0.1:6379> PUBSUB CHANNELS *
1) "NEWS:SPORTS"
127.0.0.1:6379> PUBSUB CHANNELS NEWS:*
1) "NEWS:SPORTS"
```

> Check number of subscriber

```commandline
127.0.0.1:6379> PUBSUB NUMSUB NEWS:SPORTS
1) "NEWS:SPORTS"
2) (integer) 1
```

## Chat Platform

- Step 1: User Set 

We create set for user and check a particular user exist, if not add member

```commandline
127.0.0.1:6379> SMEMBERS USERS
(empty list or set)
127.0.0.1:6379> SISMEMBER USERS user1
(integer) 0
127.0.0.1:6379> SADD USERS user1
(integer) 1
```

> Finally, if user leave room we remove user

```commandline
127.0.0.1:6379> SREM USERS user1
(integer) 1
127.0.0.1:6379> SISMEMBER USERS user1
(integer) 0

```

- Step 2: Chat room

> Key will be 'ROOM:[ROOM NAME]' and message will be '[USER NAME]: Message'

```commandline
127.0.0.1:6379> RPUSH ROOM:Friends "user1:Hello all!"
(integer) 1
127.0.0.1:6379> RPUSH ROOM:Friends "user2:Hi user1"
(integer) 2
127.0.0.1:6379> LRANGE ROOM:Friends 0 -1
1) "user1:Hello all!"
2) "user2:Hi user1"

```

- Step 2: Private room

> Key will be 'DIRECT:[FIRST USER]:[SECOND USER]' and message will be '[FIRST USER]: Message'

```commandline
127.0.0.1:6379> RPUSH DIRECT:user1:user2 "user1:Hello user2"
(integer) 1
127.0.0.1:6379> RPUSH DIRECT:user2:user1 "user2:Hey user1"
(integer) 1
127.0.0.1:6379> RPUSH DIRECT:user1:user2 "user1:Whats up"
(integer) 2
127.0.0.1:6379> LRANGE DIRECT:user1:user2 0 -1
1) "user1:Hello user2"
2) "user1:Whats up"
127.0.0.1:6379> LRANGE DIRECT:user2:user1 0 -1
1) "user2:Hey user1"

```

- Step 3: Common Room with PUB-SUB (Chat Room is abstracted as Channel)

> We define room as set, member in a room also as a set

```commandline
127.0.0.1:6379> SMEMBERS ROOM:School
(empty list or set)
127.0.0.1:6379> SMEMBERS ROOM:Office
(empty list or set)
127.0.0.1:6379> SADD ROOM:School ali dab
(integer) 2
127.0.0.1:6379> SADD ROOM:Office ali prem
(integer) 2
127.0.0.1:6379> SMEMBERS ROOM:School
1) "ali"
2) "dab"
127.0.0.1:6379> SMEMBERS ROOM:Office
1) "prem"
2) "ali"
```

> User enter 

```commandline
127.0.0.1:6379> SADD ROOM:School raj
(integer) 1
127.0.0.1:6379> SUBSCRIBE ROOM:School
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "ROOM:School"
3) (integer) 1
```

> User leave room

```commandline
127.0.0.1:6379> UNSUBSCRIBE ROOM:School raj
1) "unsubscribe"
2) "ROOM:School"
3) (integer) 0
127.0.0.1:6379> SREM ROOM:School raj
1) "unsubscribe"
2) "raj"
3) (integer) 0
```

