
## Python Redis

- Install Redis client

```
[root@localhost REDIS]# python3 -m venv venv
[root@localhost REDIS]# source venv/bin/activate
(venv) [root@localhost REDIS]# pip install redis
Collecting redis
Successfully installed async-timeout-4.0.2 deprecated-1.2.13 importlib-metadata-4.8.3 packaging-21.3 pyparsing-3.0.9 redis-4.3.4 typing-extensions-4.1.1 wrapt-1.14.1 zipp-3.6.0
```

- Connecting to Redis 

```
python templates/connect.py
Starting to connect to Redis instance locally.
Successfully connected to Redis.
Detail: {'redis_version': '3.2.12', 'redis_git_sha1': 0, 'redis_git_dirty': 0, 'redis_build_id': '7897e7d0e13773f', 'redis_mode': 'standalone', 'os': 'Linux 4.18.0-305.19.1.el8_4.x86_64 x86_64', 'arch_bits': 64, 'multiplexing_api': 'epoll', 'gcc_version': '4.8.5', 'process_id': 7, 'run_id': '15330838fd6ade826d97dc60561eb96b2ae64e04', 'tcp_port': 6379, 'uptime_in_seconds': 44071, 'uptime_in_days': 0, 'hz': 10, 'lru_clock': 12836096, 'executable': '/redis-server', 'config_file': '/redis-master/redis.conf', 'connected_clients': 2, 'client_longest_output_list': 0, 'client_biggest_input_buf': 0, 'blocked_clients': 0, 'used_memory': 835464, 'used_memory_human': '815.88K', 'used_memory_rss': 9805824, 'used_memory_rss_human': '9.35M', 'used_memory_peak': 835464, 'used_memory_peak_human': '815.88K', 'total_system_memory': 8146305024, 'total_system_memory_human': '7.59G', 'used_memory_lua': 37888, 'used_memory_lua_human': '37.00K', 'maxmemory': 0, 'maxmemory_human': '0B', 'maxmemory_policy': 'noeviction', 'mem_fragmentation_ratio': 11.74, 'mem_allocator': 'jemalloc-3.6.0', 'loading': 0, 'rdb_changes_since_last_save': 0, 'rdb_bgsave_in_progress': 0, 'rdb_last_save_time': 1656962158, 'rdb_last_bgsave_status': 'ok', 'rdb_last_bgsave_time_sec': 0, 'rdb_current_bgsave_time_sec': -1, 'aof_enabled': 1, 'aof_rewrite_in_progress': 0, 'aof_rewrite_scheduled': 0, 'aof_last_rewrite_time_sec': -1, 'aof_current_rewrite_time_sec': -1, 'aof_last_bgrewrite_status': 'ok', 'aof_last_write_status': 'ok', 'aof_current_size': 2325, 'aof_base_size': 2035, 'aof_pending_rewrite': 0, 'aof_buffer_length': 0, 'aof_rewrite_buffer_length': 0, 'aof_pending_bio_fsync': 0, 'aof_delayed_fsync': 0, 'total_connections_received': 10, 'total_commands_processed': 19, 'instantaneous_ops_per_sec': 0, 'total_net_input_bytes': 563, 'total_net_output_bytes': 78315, 'instantaneous_input_kbps': 0.0, 'instantaneous_output_kbps': 0.0, 'rejected_connections': 2, 'sync_full': 0, 'sync_partial_ok': 0, 'sync_partial_err': 0, 'expired_keys': 0, 'evicted_keys': 0, 'keyspace_hits': 1, 'keyspace_misses': 1, 'pubsub_channels': 0, 'pubsub_patterns': 0, 'latest_fork_usec': 250, 'migrate_cached_sockets': 0, 'role': 'master', 'connected_slaves': 0, 'master_repl_offset': 0, 'repl_backlog_active': 0, 'repl_backlog_size': 1048576, 'repl_backlog_first_byte_offset': 0, 'repl_backlog_histlen': 0, 'used_cpu_sys': 5.73, 'used_cpu_user': 2.38, 'used_cpu_sys_children': 0.01, 'used_cpu_user_children': 0.0, 'cluster_enabled': 0, 'db0': {'keys': 20, 'expires': 0, 'avg_ttl': 0}}

```

- Test by setting and fetching Keys 

```commandline
(venv) [root@localhost REDIS]# python key.py
Starting to connect to Redis instance locally.
Successfully connected to Redis.
Setting keys to DB
Get Keys
Name of sankar - b'Sankar Mukherjee'
```

- Test populating and fetching List

```commandline
(venv) [root@localhost REDIS]# python redis_list_eg.py
Starting to connect to Redis instance locally.
Successfully connected to Redis.
Populating List names in DB
Print List names
b'Jade'
b'Alif'
b'Dabli'
b'Sankar'
```

- Test populating and fetching Hash

```commandline

```