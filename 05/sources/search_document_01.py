# Search Document
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


# Step 2: Map Collection to Object
# Get total object count
count_movies = Movies.objects.count()
logging.info("Total movies in DB: {}".format(count_movies))

# Search specific object
logging.info("Total UNRATED movies: {}".format(Movies.objects(rated='UNRATED').count()))

# List all possible rating
logging.info("All possible ratings:")
for r in Movies.objects().distinct('rated'):
    logging.info(r)

# Search with not equal condition
# https://docs.mongoengine.org/guide/querying.html
logging.info("Total NOT UNRATED movies: {}".format(Movies.objects(rated__ne='UNRATED').count()))
logging.info("Total Runtime more than an hour: {}".format(Movies.objects(runtime__gt=60).count()))
logging.info("Total Runtime NOT more than an hour: {}".format(Movies.objects(runtime__not__gt=60).count()))

# Search in embedded document
logging.info("Total movies with IMDB votes greater than 1000: {}".format(Movies.objects(imdb__votes__gt=1000).count()))

# Search in List fields
logging.info("Total movies in country USA OR India: {}".format(Movies.objects(countries__in=['USA', 'India']).count()))
logging.info("Total movies NOT in country USA or India: {}".format(Movies.objects(countries__not__in=['USA',
                                                                                                      'India'])
                                                                   .count()))
logging.info("Total movies in country USA AND India: {}".format(Movies.objects(countries__all=['USA', 'India'])
                                                                .count()))
for m in Movies.objects(countries__all=['USA', 'India'])[:2]:
    logging.info("Movie: {}, Country: {}".format(m.title, m.countries))

# Note below we access Index in Array
logging.info("Total movies where USA is the first country: {}".format(Movies.objects(countries__0='USA').count()))
for m in Movies.objects(countries__0='USA')[:2]:
    logging.info("Movie: {}, Country: {}".format(m.title, m.countries))

logging.info("Total movies where 3 countries involved: {}".format(Movies.objects(countries__size=3).count()))
for m in Movies.objects(countries__size=3)[:2]:
    logging.info("Movie: {}, Country: {}".format(m.title, m.countries))

# String search
# https://docs.mongoengine.org/guide/querying.html#string-queries
logging.info("Total movies having india in its name: {}".format(Movies.objects(title__icontains='india').count()))
for m in Movies.objects(title__icontains='india')[:2]:
    logging.info("Movie: {}, Country: {}".format(m.title, m.countries))


# Sorting Result
logging.info("Total movies having india in its name sorted by imdb rating: {}".format(
    ["{}, {}".format(m.title, m.imdb.rating) for m in Movies.objects(title__icontains='india')
        .order_by('imdb.rating')]))
logging.info("Total movies having india in its name sorted by imdb rating: {}".format(
    ["{}, {}".format(m.title, m.imdb.rating) for m in Movies.objects(title__icontains='india')
        .order_by('-imdb.rating')]))  # Reversing the order


# Aggregation
logging.info("Total movies runtime: {}".format(Movies.objects().sum('runtime')))
logging.info("Average runtime with India in its name: {}".format(Movies.objects(title__icontains='india')
                                                                 .average('runtime')))
logging.info("All distinct rating with India in its name: {}".format(Movies.objects(title__icontains='india')
                                                                     .distinct('rated')))

# Project column
logging.info("Movies where 3 countries involved: {}".format(
    ["{}, {}, {}".format(m.title, m.countries, m.rated) for m in Movies.objects(countries__size=3)
        .only('title', 'countries')]))  # Note the field not projected returns None or Empty (e.g. list)


# Skip records
logging.info("Movies list skipped 100: {}".format(
    ["{}, {}, {}".format(m.title, m.countries, m.rated) for m in Movies.objects().skip(100).limit(5)]))


# Multiple operators
logging.info("Total movies having india in its name AND IMDB rating more than 7: {}".format(
    Movies.objects(Q(title__icontains='india') & Q(imdb__rating__gt=7)).count()))
logging.info("Total movies having india in its name OR IMDB rating more than 7: {}".format(
    Movies.objects(Q(title__icontains='india') | Q(imdb__rating__gt=7)).count()))

logging.info("Disconnecting")
disconnect()
