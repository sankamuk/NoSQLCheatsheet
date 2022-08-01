# Connect to MongoDB and Create a document in a collection
import logging
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="new_books", host="192.168.56.103", port=27017)


# Creating a document template
class History(Document):
    meta = {
        "collection": "history"
    }
    # https://docs.mongoengine.org/guide/defining-documents.html#fields
    name = StringField()
    author = StringField()


# Creating document
hb1 = History(name="Ocean of Churns", author="Sanjeev Sanyal")
# Persisting document in MongoDB
hb1.save()


logging.info("Disconnecting")
disconnect()
