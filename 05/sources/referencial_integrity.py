# Referential integrity
# OPTION 1: Block deletion of referred object
# OPTION 2: Allow deletion but nullify reference
# OPTION 3: Cascade delete reference
# OPTION 4: Pulls out the reference
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="manage_book", host="192.168.56.103", port=27017)


# # OPTION 1: Block deletion of object in reference
# # Publisher
# class Publisher(Document):
#     name = StringField()
#
#
# # Book
# class Book(Document):
#     name = StringField()
#     publisher = ReferenceField(Publisher, reverse_delete_rule=DENY)
#
#
# # Create and Save
# p1 = Publisher(name="ABP")
# p1.save()
# b1 = Book(name="Some Book", publisher=p1)
# b1.save()
#
# logging.info("Book and Publisher saved")
# logging.info("Publisher {}".format(p1.name))
# logging.info("Book {}".format(b1.name))
# logging.info("Book Publisher {}".format(b1.publisher.name))
#
# logging.info("Lets delete")
# p1.delete()  # Exception - mongoengine.errors.OperationError: Could not delete document (Book.publisher refers to it)


# # OPTION 2
# # Publisher
# class Publisher2(Document):
#     name = StringField()
#
#
# # Book
# class Book2(Document):
#     name = StringField()
#     publisher = ReferenceField(Publisher2, reverse_delete_rule=NULLIFY)
#
#
# # Create and Save
# p1 = Publisher2(name="ABP 1")
# p1.save()
# b1 = Book2(name="Some New Book", publisher=p1)
# b1.save()
#
# logging.info("Book and Publisher saved")
# logging.info("Publisher {}".format(p1.name))
# logging.info("Book {}".format(b1.name))
# logging.info("Book Publisher {}".format(b1.publisher.name))
#
# logging.info("Lets delete")
# p1.delete()  # Allow and will clear the field


# # OPTION 3
# # Publisher
# class Publisher3(Document):
#     name = StringField()
#
#
# # Book
# class Book3(Document):
#     name = StringField()
#     publisher = ReferenceField(Publisher3, reverse_delete_rule=CASCADE)
#
#
# # Create and Save
# p1 = Publisher3(name="ABP 1")
# p1.save()
# b1 = Book3(name="Some New Book", publisher=p1)
# b1.save()
#
# logging.info("Book and Publisher saved")
# logging.info("Publisher {}".format(p1.name))
# logging.info("Book {}".format(b1.name))
# logging.info("Book Publisher {}".format(b1.publisher.name))
#
# logging.info("Lets delete")
# p1.delete()  # Allow and will clear the field


# OPTION 4
# Publisher
class Author4(Document):
    name = StringField()


# Book
class Book4(Document):
    name = StringField()
    authors = ListField(ReferenceField(Author4, reverse_delete_rule=PULL))


# Create and Save
a1 = Author4(name="Some one")
a1.save()
a2 = Author4(name="Another one")
a2.save()
b1 = Book4(name="Some New Book", authors=[a1, a2])
b1.save()

logging.info("Book and Author saved")
logging.info("Author {}, {}".format(a1.name, a2.name))
logging.info("Book {}".format(b1.name))
logging.info("Book Author {}, {}".format(b1.authors[0].name, b1.authors[1].name))

logging.info("Lets delete")
a1.delete()  # Allow and will clear the field

logging.info("Disconnecting")
disconnect()
