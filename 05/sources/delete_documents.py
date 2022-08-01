# Persist
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="manage_book", host="192.168.56.103", port=27017)


# Acknowledgment
class EmployeeRecord(Document):
    name = StringField()
    city = StringField()
    age = IntField()


# Delete single record
logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

logging.info("Deleting record for Buro")
e = EmployeeRecord.objects(name="Buro")
e.delete()

logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

# Delete multiple records
logging.info("Deleting multiple record")
e = EmployeeRecord.objects()
e.delete()

logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

# Delete full collection
EmployeeRecord.drop_collection()

logging.info("Disconnecting")
disconnect()
