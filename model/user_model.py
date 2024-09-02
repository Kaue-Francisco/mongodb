import datetime
import bcrypt

class UserModel:
    def __init__(self, config_database):
        self.config_database = config_database
        self.db = self.config_database.get_db()
        self.table_user = self.db.users

    ################################################################################
    def get_user(self, email: str):
        return self.table_user.find_one({'email': email})

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
    def email_exists(self, email: str):
        return self.table_user.find_one({'email': email}) is not None