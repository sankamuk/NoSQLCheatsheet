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


logging.info("Creating 3 Employee")
e1 = EmployeeRecord(name="Buro", city="Kolkata", age=38)
e2 = EmployeeRecord(name="Dab", city="Belghoria", age=37)
e3 = EmployeeRecord(name="Paka", city="Baguiati", age=36)

logging.info("Saving employee")
EmployeeRecord.objects().insert([e1, e2, e3])

logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

# Update One record
logging.info("Updating Dab's city to Kolkata")
d = EmployeeRecord.objects(name='Dab')
d.update_one(city="Kolkata")
# Note once you run update on an object reference it changes so second update will not work, you need to fetch again

logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

logging.info("Alternate approach to update")
d = EmployeeRecord.objects(name='Dab').first()
d.city = "Belghoria"
d.save()

logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

# Update Multiple records
# https://docs.mongoengine.org/guide/querying.html#atomic-updates
logging.info("Updating every employee by 1")
EmployeeRecord.objects().update(inc__age=1)  # Note you can use dec to decrement

logging.info("Employee: {}".format(
    ["{}, {} years stays at {}".format(e.name, e.age, e.city) for e in EmployeeRecord.objects()]
))

logging.info("Disconnecting")
disconnect()
