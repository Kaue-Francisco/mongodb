################################################################################
# Imports 

from config.definitions import *
from pymongo import MongoClient

################################################################################
class ConfigDatabase:
    def __init__(self):
        self.url = URL
        self.client = MongoClient(self.url)

    ################################################################################
    def get_db(self):
        db = self.client[DB_NAME]
        return db