# One to one relationship example
# Book to ISBN Number - One book will have one ISBN and a ISBN can only be of one Book
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="book_db", host="192.168.56.103", port=27017)


def book_type(type):
    """Validates whether book is of allowed type"""
    allowed_types = ["history", "science", "maths", "fiction"]


# Defining document
class Isbn(EmbeddedDocument):
    """Book Universal Identity"""
    isbn_num = StringField(required=True)
    datetime = DateTimeField()


class Book(Document):
    """Book"""
    name = StringField(required=True)
    type = StringField(validation=book_type)
    isbn = EmbeddedDocumentField(Isbn)  # ISBN has One to One relationship with Book


# Creating document
edoc1 = Isbn(isbn_num="ISBN0923647")
doc1 = Book(name="Compilers", type="science", isbn=edoc1)

# Saving document
doc1.save()  # Note embedded document get saved as part if enclosing document


logging.info("Disconnecting")
disconnect()
