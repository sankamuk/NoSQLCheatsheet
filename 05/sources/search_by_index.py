# Use index based search
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="library_book", host="192.168.56.103", port=27017)


# # Non Index Based Search
# # Book
# class BookNonIndex(Document):
#     name = StringField()
#
#
# # Create and search
# b1 = BookNonIndex(name="Theory of Relativity")
# b2 = BookNonIndex(name="Discovery of India")
# b1.save()
# b2.save()
#
# # Search
# logging.info("Searching")
# logging.info(BookNonIndex.objects(name="Theory of Relativity"))
# logging.info("Query Explain :")
# logging.info(BookNonIndex.objects(name="Theory of Relativity").explain())
# You should see COLLSCAN (Collection Scan) meaning you doing full table scan


# Non Index Based Search
# Book
class BookIndex(Document):
    name = StringField()
    meta = {
        'indexes': [
            'name'
        ]
    }
# We can create more than one index by adding element in list and create compound index by (e1, e2) and
# Also create index in reverse order by specifying negation (e1, -e2)


# Create and search
b1 = BookIndex(name="Theory of Relativity")
b2 = BookIndex(name="Discovery of India")
b1.save()
b2.save()

# Search
logging.info("Searching")
logging.info(BookIndex.objects(name="Theory of Relativity"))
logging.info("Query Explain :")
logging.info(BookIndex.objects(name="Theory of Relativity").explain())
# You should see IXSCAN to denote scan in Index

# Note to much index can degrade performance in write

# Create Index
# logging.info("Create new Index")
# BookIndex.create_index('-name')
# db.book_index.getIndexes() <- Show all Indexes

# Drop Index
c = BookIndex._get_collection()
c.drop_index('name_1')

logging.info("Disconnecting")
disconnect()
