# Connect to MongoDB and Create a document in a collection with Custom Validation in fields
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="new_books", host="192.168.56.103", port=27017)


# Validation function
def check_first_capital(str_name):
    """Check whether first character of a name os provided in Capital"""
    if not str_name[0].isupper():
        raise ValidationError("First character need to be in Capital")


# Creating a document template
class Physics(Document):
    id = LongField(primary_key=True)
    name = StringField(required=True)
    author = StringField(validation=check_first_capital)


# Creating document
cb2 = Physics()
cb2.id = 100230001
cb2.name = "Theory of Relativity"
cb2.author = "A Einstein"

# Persisting document in MongoDB
cb2.save()  # Succeeds

# Creating document
cb1 = Physics()
cb1.id = 100230000
cb1.name = "School Physics"
cb1.author = "unknown"

# Persisting document in MongoDB
cb1.save()  # Fail - ValidationError (Physics:100230000) (First character need to be in Capital: ['author'])

logging.info("Disconnecting")
disconnect()
