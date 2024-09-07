################################################################################
# Imports

from pymongo import MongoClient
import datetime
import bcrypt

################################################################################
class UserModel:
    
    def __init__(self, config_database: MongoClient) -> None:
        self.config_database = config_database
        self.db = self.config_database.get_db()
        self.table_user = self.db.users

    ################################################################################
    def get_user(self, email: str) -> dict:
        return self.table_user.find_one({'email': email})

    ################################################################################
    def get_all_users(self) -> dict:
        return self.table_user.find()
    
    ################################################################################
    def get_all_sellers(self) -> dict:
        return self.table_user.find({'seller': True})
    
    ################################################################################
    def create_user(self, 
                    name: str,                      # User name
                    email: str,                     # User email
                    password: bcrypt,               # User password (hashed)
                    seller: bool,                   # User is a seller
                    registration_data: datetime):   # User registration date
        
        user = {
            'name': name,
            'email': email,
            'password': password,
            'seller': seller,
            'registration_data': registration_data
        }
        
        self.table_user.insert_one(user)
    
    ################################################################################
    def update_user(self, user_id: str, field: str, value: str) -> None:
        self.table_user.update_one({'_id': user_id}, {'$set': {field: value}})
        
    ################################################################################
    def delete_user(self, user_id: str) -> None:
        self.table_user.delete_one({'_id': user_id})

    ################################################################################
    def email_exists(self, email: str) -> bool:
        return self.table_user.find_one({'email': email}) is not None