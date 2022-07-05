import redis
import sys

try:
    print("Starting to connect to Redis instance locally.")
    client = redis.Redis(host="localhost", port=6379, db=0)
except Exception as e:
    print("Could not connect to Redis.")
    print(e)
    sys.exit(1)

print("Successfully connected to Redis. \nDetail: {}".format(client.info()))
