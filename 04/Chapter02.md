
## Redis Up & Running

- Run Redis in docker (https://hub.docker.com/r/centos/redis)

```
docker run -d -p 6379:6379 -e MASTER=true centos/redis:latest
```

- Check Redis

```
docker exec -it $(docker ps | grep "centos/redis" | awk '{ print $1 }') sh
sh-4.2$ redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> quit
sh-4.2$
```

## Redis Cli

- Running in Non Interactive Mode

```
sh-4.2$ redis-cli SET k3 100
OK
sh-4.2$ redis-cli GET k3 > /tmp/k3.value
sh-4.2$ cat /tmp/k3.value
100
```

- Check Service Status & Printing

```
127.0.0.1:6379> PING
PONG
127.0.0.1:6379> ECHO "Hello"
"Hello"
```

- Set & Get Key Value

```
127.0.0.1:6379> SET k1 v1
OK
127.0.0.1:6379> GET k1
"v1"
```

- Increament & Decrement Values

```
127.0.0.1:6379> SET k2 10
OK
127.0.0.1:6379> INCR k2
(integer) 11
127.0.0.1:6379> INCR k2
(integer) 12
127.0.0.1:6379> DECR k2
(integer) 11
127.0.0.1:6379> GET k2
"11"
127.0.0.1:6379> SET k1 100
OK
127.0.0.1:6379> INCR k1 10
(error) ERR wrong number of arguments for 'incr' command
127.0.0.1:6379>
127.0.0.1:6379> INCRBY k1 10
(integer) 110
127.0.0.1:6379> GET k1
"110"
127.0.0.1:6379> DECRBY k1 50
(integer) 60
127.0.0.1:6379> GET k1
"60"

```

- Check Key Existance

```
127.0.0.1:6379> EXISTS k1
(integer) 1
127.0.0.1:6379> EXISTS k2
(integer) 1
127.0.0.1:6379> EXISTS k3
(integer) 0
```

> Note for EXISTS the output is not the value but 0/1 represents binary for NOT EXISTS (0) and EXITS (1)

- Remove Key

```
127.0.0.1:6379> DEL k1
(integer) 1
127.0.0.1:6379> EXISTS k1
(integer) 0
```

- Monitor Server Activity

### Terminal 1

```
sh-4.2$ redis-cli INCR k3
(integer) 101
sh-4.2$ redis-cli GET k3
"101"

```

### Terminal 2

```
sh-4.2$ redis-cli MONITOR
OK
1655050798.006334 [0 127.0.0.1:59310] "INCR" "k3"
1655050813.877928 [0 127.0.0.1:59312] "GET" "k3"

```

- Clear Redis

```
sh-4.2$ redis-cli EXISTS k1
(integer) 0
sh-4.2$ redis-cli EXISTS k2
(integer) 1
sh-4.2$ redis-cli EXISTS k3
(integer) 1
sh-4.2$ redis-cli FLUSHALL
OK
sh-4.2$ redis-cli EXISTS k3
(integer) 0
sh-4.2$ redis-cli EXISTS k2
(integer) 0
sh-4.2$ redis-cli EXISTS k1
(integer) 0
sh-4.2$ redis-cli GET k1
(nil)

```

> Use this ***carefully***.


- Namespaces

```
127.0.0.1:6379> SET IBM:employee1 '{"name": "San"}'
OK
127.0.0.1:6379> SET IBM:employee2 '{"name": "Jad"}'
OK
127.0.0.1:6379> SET TSC:employee1 '{"name": "Kun"}'
OK
127.0.0.1:6379> GET TSC:employee1
"{\"name\": \"Kun\"}"

```

- Expiry

```
127.0.0.1:6379> SET TSC:employee2 '{"name": "Xun"}'
OK
127.0.0.1:6379> EXPIRE TSC:employee2 30
(integer) 1
127.0.0.1:6379> GET TSC:employee2
"{\"name\": \"Xun\"}"
127.0.0.1:6379> GET TSC:employee2
(nil)
```

```
```

- Tracking Expiry

```
127.0.0.1:6379> SET TSC:employee2 '{"name": "Xun"}'
OK
127.0.0.1:6379> TTL TSC:employee2
(integer) -1
127.0.0.1:6379> EXPIRE TSC:employee2 30
(integer) 1
127.0.0.1:6379> TTL TSC:employee2
(integer) 26
127.0.0.1:6379> TTL TSC:employee2
(integer) 15
127.0.0.1:6379> TTL TSC:employee2
(integer) -2

```

> Note if there is no Expiry TTL is -1 and once the key expired it becomes -2 (Not Set Key). Every other scenario the TTL represents value of second remain for expiry.

