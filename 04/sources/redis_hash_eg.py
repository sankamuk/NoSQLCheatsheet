import redis
import sys

try:
    print("Starting to connect to Redis instance locally.")
    client = redis.Redis(host="localhost", port=6379, db=0)
except Exception as e:
    print("Could not connect to Redis.")
    print(e)
    sys.exit(1)
print("Successfully connected to Redis.")

print("Populating Hash of emp in DB")
client.hmset("emp:ali", {
    "name": "Alif",
    "age": 36,
    "city": "belmundi"
})
client.hmset("emp:dab", {
    "name": "Dabli",
    "age": 37,
    "city": "kolkata"
})

print("Print Hash key")
print("emp:dab name is {}".format(client.hget("emp:dab", "name")))

