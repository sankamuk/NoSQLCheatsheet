# Aggregation Framework (https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)
import logging
from datetime import datetime
from mongoengine import *
from mongoengine.queryset.visitor import Q

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="mflix", host="192.168.56.103", port=27017)


# Step 1: Define the document to be searched
# Note no need to map the whole document define only field needed
class Imdb(EmbeddedDocument):
    rating = FloatField()
    votes = IntField()
    id = IntField()


class Movies(Document):
    title = StringField()
    runtime = IntField()
    rated = StringField()
    countries = ListField(StringField())
    imdb = EmbeddedDocumentField(Imdb)

    meta = {
        'strict': False  # This will tell MongoDB that all fields are not required
    }


mvs = Movies.objects.aggregate([])  # Returns a generator to iterate over the collection

# Print two movies
logging.info("First movie: {}".format(mvs.next()))
logging.info("Second movie: {}".format(mvs.next()))

# Group aggregation (on Country)
mvs_grp = Movies.objects.aggregate([{
    "$group": {
        "_id": "$countries"
    }
}])

# Print result
logging.info("List of countries : {}".format(list(mvs_grp)))

# Group aggregation (count sum of group)
mvs_grp = Movies.objects.aggregate([{
    "$group": {
        "_id": "$countries",
        "count": {                   # New field
            "$sum": 1                # Sum operation
        }
    }
}])

# Print result
logging.info("Sum of count for country group : {}".format(list(mvs_grp)))

logging.info("Disconnecting")
disconnect()
