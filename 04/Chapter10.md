
## HyperLog

Efficient data structure to count unique elements. Example usage could be unique visitors in a website.

> Important consideration is though Hyperlog is extremely efficient (memory and compute) mean to keep count of elements in a Set but since its a probabilistic data structure thus not 100% accurate all times.

- Adding, Counting and Merging 

```commandline
127.0.0.1:6379> PFADD user:attendance:office buro dabli
(integer) 1
127.0.0.1:6379> PFADD user:attendance:office buro dabli alif
(integer) 1
127.0.0.1:6379> PFCOUNT user:attendance:office
(integer) 3
127.0.0.1:6379> PFADD user:attendance:wfh jewel dabli
(integer) 1
127.0.0.1:6379> PFCOUNT user:attendance:wfh
(integer) 2
127.0.0.1:6379> PFMERGE user:attendance user:attendance:office user:attendance:wfh
OK
127.0.0.1:6379> PFCOUNT user:attendance
(integer) 4
```

