# Connect to MongoDB and Create a document in a collection with id field as input
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="new_books", host="192.168.56.103", port=27017)


# Creating a document template
class Computing(Document):
    # https://docs.mongoengine.org/guide/defining-documents.html#fields
    id = LongField(primary_key=True)
    name = StringField()
    author = StringField()
    released = DateTimeField()
    price = DecimalField()


# Creating document
cb1 = Computing()
cb1.id = 100230000
cb1.name = "Let Us C"
cb1.author = "H Kanitkar"
cb1.released = datetime.now()
cb1.price = 300.00

# Persisting document in MongoDB
cb1.save()


logging.info("Disconnecting")
disconnect()
