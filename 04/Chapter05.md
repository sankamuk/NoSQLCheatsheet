
## Config Get

- Allow to fetch configuration
- Only allow one argument representing either config name or pattern

```
127.0.0.1:6379> CONFIG GET port
1) "port"
2) "6379"
127.0.0.1:6379> CONFIG GET p*
1) "pidfile"
2) "/var/run/redis.pid"
3) "port"
4) "6379"
5) "protected-mode"
6) "yes"
```

## Config Set

- Allow server reconfiguration
- No restart needed

```
127.0.0.1:6379> CONFIG GET cluster-node-timeout
1) "cluster-node-timeout"
2) "15000"
127.0.0.1:6379> CONFIG SET cluster-node-timeout 10000
OK
127.0.0.1:6379> CONFIG GET cluster-node-timeout
1) "cluster-node-timeout"
2) "10000"

```

## Info

- Returns information and statistics of server
- Options server, client, memory, persistance, stats, replication, cpu, comandstats, cluster, keyspace, all, default

```
127.0.0.1:6379> INFO memory
# Memory
used_memory:833496
used_memory_human:813.96K
used_memory_rss:9670656
used_memory_rss_human:9.22M
used_memory_peak:834472
used_memory_peak_human:814.91K
total_system_memory:8146305024
total_system_memory_human:7.59G
used_memory_lua:37888
used_memory_lua_human:37.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
mem_fragmentation_ratio:11.60
mem_allocator:jemalloc-3.6.0
```

## Config Resetstat

- Allows reset statistics as output of INFO
- Only below can be reset
    - keyspace hits
    - keyspace misses
    - Number of command processed
    - Number of connection recieved
    - Number of expired keys
    - Number of rejected connection

```
127.0.0.1:6379> INFO stats

expired_keys:3

127.0.0.1:6379> CONFIG RESETSTAT
OK
127.0.0.1:6379> INFO stats

expired_keys:0

```

## Command

- Returns detail about command

```
127.0.0.1:6379> COMMAND INFO GET
1) 1) "get"
   2) (integer) 2
   3) 1) readonly
      2) fast
   4) (integer) 1
   5) (integer) 1
   6) (integer) 1
```

> Output has 6 sections, argument, flags, position of first key and position of last key in argument list, count for repeating keys.

## Client List

- Return list of active clients

```
127.0.0.1:6379> CLIENT LIST
id=3 addr=127.0.0.1:44376 fd=7 name= age=391857 idle=348776 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=0 obl=0 oll=0 omem=0 events=r cmd=scan
id=4 addr=127.0.0.1:44388 fd=8 name= age=19861 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=32768 obl=0 oll=0 omem=0 events=r cmd=client

```

> IN both client above name field is blank but you can set it using 'CLIENT SETNAME <>' to easily identify names, along with this we also have 'CLIENT GETNAME'


## Client Kill

- Kill any client by id or host:port

```
127.0.0.1:6379> CLIENT KILL 127.0.0.1:44388
OK
127.0.0.1:6379> CLIENT LIST
id=3 addr=127.0.0.1:44376 fd=7 name= age=392046 idle=348965 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=0 obl=0 oll=0 omem=0 events=r cmd=scan
id=5 addr=127.0.0.1:44392 fd=8 name= age=0 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=32768 obl=0 oll=0 omem=0 events=r cmd=client
127.0.0.1:6379> CLIENT KILL 127.0.0.1:44376
OK
127.0.0.1:6379> CLIENT LIST
id=5 addr=127.0.0.1:44392 fd=8 name= age=17 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=0 qbuf-free=32768 obl=0 oll=0 omem=0 events=r cmd=client
```

> NOTE when we run redis-cli even when we kill client the tool reconnects automatically

