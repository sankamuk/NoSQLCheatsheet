# Persist
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="manage_book", host="192.168.56.103", port=27017)


# Acknowledgment
class Employee(Document):
    name = StringField()


e1 = Employee(name="Ali")
e1.save(write_concern={
    "w": 1
})  # You can set value more than 1 when you have multiple replica in your MongoDB Cluster


# Batch write
e2 = Employee(name="Dab")
e3 = Employee(name="Paka")
e4 = Employee(name="Buro")
Employee.objects().insert([e2, e3, e4])  # Batch write


logging.info("Disconnecting")
disconnect()
