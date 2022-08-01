# Connect to MongoDB
import logging
from mongoengine import connect, disconnect, register_connection

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# Connection
# If you want to connect to remote instance with MongoDB URI use it with 'host' no need of port
connection = connect(db="books", alias="books", host="192.168.56.103", port=27017)

logging.info("Connected To - {}".format(connection.server_info))
logging.info("Server Address - {}".format(connection.address))
logging.info("List DB - {}".format(connection.list_database_names()))

logging.info("Disconnecting")
disconnect("books")
