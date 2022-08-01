# Many to Many relationship example
# Book to Author Number - A book can have many author and a Author can write multiple books
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="book_db", host="192.168.56.103", port=27017)


# Authored Book
class AuthoredBook(Document):
    """Book"""
    name = StringField()
    authors = ListField(ReferenceField('Author'))  # Note how in one side we reference Class name
    # To access author detail you use array element book.author[0].name


# Author Template
class Author(Document):
    """Author"""
    name = StringField()
    books = ListField(ReferenceField(AuthoredBook))  # Other side we reference the actual class name


# Creating document
b1 = AuthoredBook(name="Know More")
b2 = AuthoredBook(name="Much More")
b1.save()
b2.save()
a1 = Author(name="SS Laal")
a2 = Author(name="Desh ka Laal")
a1.save()
a2.save()

b1.authors = [a1, a2]
b2.authors = [a1]
a1.books = [b1, b2]
a2.books = [b1]

# Saving document
b1.save()
b2.save()
a1.save()
a2.save()


logging.info("Disconnecting")
disconnect()
