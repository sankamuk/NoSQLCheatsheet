
## Installing MongoDB

- Linux

```commandline
curl -L -o mongodb-org-server-5.0.9-1.el8.x86_64.rpm https://repo.mongodb.org/yum/redhat/8/mongodb-org/5.0/x86_64/RPMS/mongodb-org-server-5.0.9-1.el8.x86_64.rpm
rpm -ivh mongodb-org-server-5.0.9-1.el8.x86_64.rpm
systemctl enable mongod
systemctl start mongod
systemctl status mongod
● mongod.service - MongoDB Database Server
   Loaded: loaded (/usr/lib/systemd/system/mongod.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-07-10 20:57:05 IST; 3s ago
     Docs: https://docs.mongodb.org/manual
  Process: 1881 ExecStart=/usr/bin/mongod $OPTIONS (code=exited, status=0/SUCCESS)
  Process: 1879 ExecStartPre=/usr/bin/chmod 0755 /var/run/mongodb (code=exited, status=0/SUCCESS)
  Process: 1878 ExecStartPre=/usr/bin/chown mongod:mongod /var/run/mongodb (code=exited, status=0/SUCCESS)
  Process: 1876 ExecStartPre=/usr/bin/mkdir -p /var/run/mongodb (code=exited, status=0/SUCCESS)
 Main PID: 1884 (mongod)
   Memory: 74.9M
   CGroup: /system.slice/mongod.service
           └─1884 /usr/bin/mongod -f /etc/mongod.conf

Jul 10 20:57:01 localhost.localdomain systemd[1]: Starting MongoDB Database Server...
Jul 10 20:57:01 localhost.localdomain mongod[1881]: about to fork child process, waiting until server is ready for connections.
Jul 10 20:57:01 localhost.localdomain mongod[1881]: forked process: 1884
Jul 10 20:57:05 localhost.localdomain mongod[1881]: child process started successfully, parent exiting
Jul 10 20:57:05 localhost.localdomain systemd[1]: Started MongoDB Database Server.
```

- Allow MongoDB to Listen to all ports

```commandline
sed -i.bak 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/g' /etc/mongod.conf
```

- Verify 

```commandline
curl -L -o mongodb-org-shell-5.0.9-1.el8.x86_64.rpm https://repo.mongodb.org/yum/redhat/8/mongodb-org/5.0/x86_64/RPMS/mongodb-org-shell-5.0.9-1.el8.x86_64.rpm
rpm -ivh mongodb-org-shell-5.0.9-1.el8.x86_64.rpm
mongo
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```

> Note please remember i was installing MongoDB in RHEL Linux 8, if you do not have similar environment pls update binary link accordingly, [LINK](https://www.mongodb.com/try/download/community)

- Install Python Client

```commandline
pip install mongoengine
```

- Install MongoDB DB Tools

```commandline
wget https://repo.mongodb.org/yum/redhat/8/mongodb-org/5.0/x86_64/RPMS/mongodb-database-tools-100.5.4.x86_64.rpm
yum install cyrus-sasl-gssapi
yum install cyrus-sasl-plain
rpm -ivh mongodb-database-tools-100.5.4.x86_64.rpm
```

> DB tool helps you avail import export feature.

```commandline
mongorestore --host localhost --port 27017 --db mflix --dir quick-mongo-atlas-datasets-master/dump/sample_mflix
```
