# # Grid FS - Allow Mongo DB to host File outside DB storage
# import logging
# from mongoengine import *
#
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
#
# # Connection
# connection = connect(db="accounts", host="192.168.56.103", port=27017)
#
#
# # Creating a document template
# class UserAccount(Document):
#     name = StringField()
#     resume = FileField()
#
#
# # Creating document
# usr1 = UserAccount(name="Jade Jabber")
# with open("../Chapter01.md", 'rb') as f:
#     usr1.resume.put(f, content_type="text/plain")
#
# # Persisting document in MongoDB
# usr1.save()
#
# logging.info("Disconnecting")
# disconnect()
