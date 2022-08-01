# One to Many relationship example
# Book to Publisher - One publisher can publish multiple books but one book can have only one publisher
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="book_db", host="192.168.56.103", port=27017)

# # EMBEDDING
# # Published book template
# class PublishedBook(EmbeddedDocument):
#     """Book which is published"""
#     name = StringField()
#     type = StringField()
#
#
# # Publisher template
# class Publisher(Document):
#     """Publisher"""
#     name = StringField()
#     city = StringField()
#     books = ListField(EmbeddedDocumentField(PublishedBook))
#
#
# # Lets create couple of books
# b1 = PublishedBook(name="Feluda 30", type="Fiction")
# b2 = PublishedBook(name="Discovery of India", type="History")
# b3 = PublishedBook(name="Let Us C", type="Science")
#
# # Now lets create Publisher for the books
# p1 = Publisher(name="Ananda", city="Kolkata", books=[b1, b2, b3])
#
# # Save
# p1.save()


# # REFERENCING
# # Published book template
# class PublishedBook2(Document):
#     """Book which is published"""
#     name = StringField()
#     type = StringField()
#
#
# # Publisher template
# class Publisher2(Document):
#     """Publisher"""
#     name = StringField()
#     city = StringField()
#     books = ListField(ReferenceField(PublishedBook2))
#
#
# # Lets create couple of books
# b4 = PublishedBook2(name="Byomkesh", type="Fiction")
# b5 = PublishedBook2(name="World War 2", type="History")
# b6 = PublishedBook2(name="Java Reference", type="Science")
#
# # Now lets create Publisher for the books
# p2 = Publisher2(name="Penguin", city="London", books=[b4, b5, b6])
#
# # Save
# b4.save()
# b5.save()
# b6.save()
# p2.save()

# REFERENCING WITH BACK REFERENCE
# Published book template
class PublishedBook3(Document):
    """Book which is published"""
    name = StringField()
    type = StringField()
    publisher = ReferenceField('Publisher3')


# Publisher template
class Publisher3(Document):
    """Publisher"""
    name = StringField()
    city = StringField()
    books = ListField(ReferenceField(PublishedBook3))


# Now lets create Publisher for the books
p3 = Publisher3(name="Oxford", city="London")

# Save Publisher
p3.save()  # Note we create Publisher first

# Lets create couple of books
b7 = PublishedBook3(name="Byomkesh", type="Fiction", publisher=p3)
b8 = PublishedBook3(name="Java Reference", type="Science", publisher=p3)

# Save Books
b8.save()
b7.save()

# Refer Book in Publisher
p3.books = [b7, b8]
p3.save()

# Now you can lookup Publisher from book like b7.publisher.name to get name of Publisher of the book

logging.info("Disconnecting")
disconnect()
