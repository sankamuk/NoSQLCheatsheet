
## Data Persistent Feature

- Data stored in memory can also be saved to disk
- Allow creation of fork which copy of parent process storing data
- Copy On Write snapshot
- Write Path 
    - [Client Memory] Client send write command to Redis
    - [Server Memory] Redis recieves the write
    - [Kernel Buffer] Redis makes system call to persist data on disk. This is start of persistance.
    - [Disk Cache] OS transfer data from write buffer to disk controller
    - [Physical Disk] Disk controller write to disk
- Redis allow creation of Pools which are multiple Redis process in same machine (Vertical Scaling)
- Redis allows replication with master slave architecture. Slaves hold copy of master data. (Horizontal scaling)
    - Asynchronous process
    - Multiple slave
    - Connection from other slave
    - Non blocking on slave side
    - Scalabilty and data redundancy
    - Slave is read only
    - Replication process
        - Master save data in background while buffering commands that modify data
        - After background saving it send files updated to slave
        - Slave save files in disk and load it in memory
        - Master send all buffer commands to slaves

- Redis persistence options
    - RDB -> Point in Time Snapshot
    - AOF -> Write Operation Logging
    - Disabled
    - RDB and AOF

## RDB & Snapshot

- RDB -> Redis Database File
- Enabled by default
- Single file point in time representation
- Use snapshots
- Advantages
    - Easy to use
    - Compact as in one file
    - Perfect for backup and recovery
    - Maximize perfomance
    - Allow after startup time
- Disadvantages
    - Limited to save points
    - Data loss is inevitable
    - Need to fork often putting stress on CPU
- Snapshoting
    - Controlled by user
    - Modifiable at runtime
    - Output is an .rbd file
    - Commands:
        - SAVE -> Synchronous operation and point in time state if data. But since its blocking all clients will be blocked for operation. Arguments second after which files save and after how many keys save is done.
        - BIGSAVE -> Save is done in background while parent continue to serve clients


## AOF

- AOF -> Append Only File
- Main persistance oparation
- Every operation gets logged
- Log are same format used by client and server
- Logs can be piped to other instance
- Using logs data can be reconstructed
- Large file handle process
    - When AOF File goes to big
    - Redis rewrite data from scratch
    - this data reconstruction happen reading the memory and disck not involved
    - Once data reconstructed data is written to disk
- Sync to Disk (FSYNC) Policies
    - Never. In this case data synched by OS (30 secs)
    - Every second (default)
    - On every query
- Advantages
    - Durable than RDB
    - Single file no corruption
    - AUtomatically rewritten once it gets big, in background
    - easy to understand log instaruction
- Disadvantages
    - Restart slow
    - Can be slower than RDB if correct FSYNC policy not choosen
    - AOF files are bigger than RDB files

> Use tools like ***rdiff-backup*** to hanlde backup task

- RDB (dump.rdb)

```
sh-4.2$ find / -name '*.rdb' 2>/dev/null
/redis-master-data/dump.rdb
sh-4.2$ ls -ltr /redis-master-data/
total 8
-rw-r--r--. 1 997 root 2035 Jul  3 18:58 appendonly.aof
-rw-r--r--. 1 997 root  367 Jul  4 18:31 dump.rdb

127.0.0.1:6379> HMSET emp:alif name "Alif" age 36 city "belmundi"
OK
127.0.0.1:6379> HMSET emp:alif name "Dabli" age 37 city "kolkata"
OK
127.0.0.1:6379> HMSET emp:alif name "Jade" age 38 city "paris"
OK
127.0.0.1:6379> SAVE
OK

sh-4.2$ ls -ltr /redis-master-data/
total 8
-rw-r--r--. 1 997 root 2325 Jul  4 19:14 appendonly.aof
-rw-r--r--. 1 997 root  372 Jul  4 19:15 dump.rdb

```

- AOF (appendonly.aof)

```
sh-4.2$ grep ^appendonly /etc/redis.conf
appendonly no

sh-4.2$ echo "INFO" | redis-cli | grep aof_enabled
aof_enabled:1

#status of rewrite, 1 - in progress 0 - rewrite complete
sh-4.2$ echo "INFO" | redis-cli | grep aof_rewrite_in_progress
aof_rewrite_in_progress:0

```

