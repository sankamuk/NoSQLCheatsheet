# Connect to MongoDB and Create a document in a collection with standard field type validation options
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="new_books", host="192.168.56.103", port=27017)


# Creating a document template
class Biology(Document):
    # Check all the data type and options available for each Type
    # https://docs.mongoengine.org/apireference.html#mongoengine.base.fields.BaseField (validations)
    id = LongField(primary_key=True)
    name = StringField(required=True)
    author = StringField(max_length=10, min_length=4)


# Creating document
cb1 = Biology()
cb1.id = 100230000
cb1.author = "Unknown"

# Persisting document in MongoDB
cb1.save()  # Fail - ValidationError (Biology:100230000) (Field is required: ['name'])

# Creating document
cb2 = Biology()
cb2.id = 100230001
cb2.name = "School Biology"
cb2.author = "RAS"

# Persisting document in MongoDB
cb2.save()  # Fail - ValidationError (Biology:100230001) (String value is too short: ['author'])

logging.info("Disconnecting")
disconnect()
