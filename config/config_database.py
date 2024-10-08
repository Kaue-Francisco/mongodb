################################################################################
# Imports 

from config.definitions import *
from pymongo import MongoClient
import redis

################################################################################
class ConfigDatabase:
    def __init__(self):
        self.url = URL
        self.client = MongoClient(self.url)
        
        self.redis_conn = redis.Redis(
            host='redis-10053.c308.sa-east-1-1.ec2.redns.redis-cloud.com',
            port=10053,
            password=PASSWORD_REDIS)

    ################################################################################
    def get_db(self):
        db = self.client[DB_NAME]
        return db
    
    def get_redis(self):
        return self.redis_conn