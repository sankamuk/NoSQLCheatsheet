# Use index based search
import logging
from datetime import datetime
from mongoengine import connect, Document, StringField, disconnect

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="mflix", host="192.168.56.103", port=27017)


# Define document
class Movies(Document):
    title = StringField()
    fullplot = StringField()

    meta = {
        'strict': False  # This will tell MongoDB that all fields are not required
    }


# Single field Index
# Set Text Index
# Movies.create_index("$fullplot")
#
# # Search in Index
# mvs = Movies.objects.search_text("India")
#
# # Print
# logging.info("India in Plot: {}".format(["{}: {}".format(m.title, m.fullplot) for m in list(mvs)[:2]]))

# # Complex multiple field index with weight
# # Set Text Index
# Movies.create_index(["$title", "$fullplot"], weights={"title": 2, "fullplot": 1})
#
# # Search in Index
# mvs = Movies.objects.search_text("India")
#
# # Print
# logging.info("India in Plot: {}".format(["{}: {}".format(m.title, m.fullplot) for m in list(mvs)[:2]]))

# Complex multiple field index with weight and result by weight
# Set Text Index
Movies.create_index(["$title", "$fullplot"], weights={"title": 2, "fullplot": 1})

# Search in Index

mvs = Movies.objects.search_text("India").order_by("$text_score")

# Print
logging.info("India in Plot: {}".format(["{}: {}".format(m.title, m.fullplot) for m in list(mvs)[:2]]))

logging.info("Disconnecting")
disconnect()
