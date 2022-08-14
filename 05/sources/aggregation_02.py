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


# Multi-step group aggregation (count sum of group)
mvs_grp = Movies.objects.aggregate([{
    "$group": {
        "_id": "$countries",
        "count": {                   # New field
            "$sum": 1                # Sum operation
        }
    }
}, {
    "$sort": {                       # Operation sort
        "count": 1                   # Field count and order ascending (i.e. 1, descending is -1)
    }
}])

# Print result
# logging.info("Sum of count for country group sorted : {}".format(list(mvs_grp)))

# Multi-step group aggregation with limit (count sum of group)
mvs_grp = Movies.objects.aggregate([{
    "$group": {
        "_id": "$countries",
        "count": {                   # New field
            "$sum": 1                # Sum operation
        }
    }
}, {
    "$sort": {                       # Operation sort
        "count": 1                   # Field count and order ascending (i.e. 1, descending is -1)
    }
}, {
    "$limit": 10                     # Limit
}])

# Print result
# logging.info("Sum of count for country group sorted : {}".format(list(mvs_grp)))

# Explode array column before group aggregation with limit (count sum of group)
mvs_grp = Movies.objects.aggregate([{
    "$unwind": {                     # explode operation
        "path": "$countries"         # Field to explode
    }
}, {
    "$group": {
        "_id": "$countries",
        "count": {
            "$sum": 1
        }
    }
}, {
    "$sort": {
        "count": -1
    }
}, {
    "$limit": 10
}])

# Print result
# logging.info("Sum of count for country group sorted : {}".format(list(mvs_grp)))

# Filter
mvs_grp = Movies.objects.aggregate([{
    "$match": {
        "countries": "India"
    }
}])

# Print result
# logging.info("Movies from India : {}".format(list(mvs_grp)))

# Average Rating for Movies
mvs_grp = Movies.objects.aggregate([{
    "$unwind": {
        "path": "$countries"                   # This is important as the countries field is a array
    }
}, {
    "$group": {
        "_id": "$countries",
        "average rating": {
            "$avg": "$imdb.rating"
        }
    }
}, {
    "$sort": {
        "average rating": -1
    }
}])

# Print result
# logging.info("Movies average rating: {}".format(list(mvs_grp)))

# Average Rating for Movies in India
mvs_grp = Movies.objects.aggregate([{
    "$unwind": {
        "path": "$countries"                   # This is important as the countries field is a array
    }
}, {
    "$match": {
        "countries": "India"
    }
}, {
    "$group": {
        "_id": "$countries",
        "average rating": {
            "$avg": "$imdb.rating"
        }
    }
}])

# Print result
# logging.info("Movies from India average rating: {}".format(list(mvs_grp)))

# Project fields
mvs_grp = Movies.objects.aggregate([{
    "$project": {                              # Project by default exclude everything unless its projected
        "_id": 0,                              # 0 means projected out, which is redundant as anyway it will be excluded
        "title": 1,
        "rating": "$imdb.rating"               # Embedded fields
    }
}])

# Print result
# logging.info("Movies title: {}".format(list(mvs_grp)))

# Skipping records
mvs_grp = Movies.objects.aggregate([{
    "$project": {
        "_id": 0,
        "title": 1,
        "rating": "$imdb.rating"
    }
}, {
    "$skip": 10
}])

# Print result
# logging.info("Movies title: {}".format(list(mvs_grp)))

# Create Table As Select (Creating new Collection from Query)
mvs_grp = Movies.objects.aggregate([{
    "$project": {
        "title": 1,
        "rating": "$imdb.rating"
    }
}, {
    "$out": 'movies_rating_tmp'
}])
logging.info("New collection movies_rating_tmp should be available now!")

# > db.movies_rating_tmp.find().limit(3).pretty()
# {
#         "_id" : ObjectId("573a1390f29313caabcd4135"),
#         "title" : "Blacksmith Scene",
#         "rating" : 6.2
# }
# {
#         "_id" : ObjectId("573a1390f29313caabcd42e8"),
#         "title" : "The Great Train Robbery",
#         "rating" : 7.4
# }
# {
#         "_id" : ObjectId("573a1390f29313caabcd4323"),
#         "title" : "The Land Beyond the Sunset",
#         "rating" : 7.1
# }


logging.info("Disconnecting")
disconnect()
