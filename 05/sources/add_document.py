# Add document
import logging
from datetime import datetime
from mongoengine import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
connection = connect(db="library", host="192.168.56.103", port=27017)


logging.info("Disconnecting")
disconnect()
