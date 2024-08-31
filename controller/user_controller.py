################################################################################
# Imports

import datetime
from model.user_model import UserModel

################################################################################
class UserController:
    def __init__(self, db):
        self.config_database = db
        self.user_model = UserModel(self.config_database)

    ################################################################################
    def create_user(self, data: dict):
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        seller = False
        registration_data = datetime.datetime.now()
        self.user_model.create_user(name, email, password, seller, registration_data)

    ################################################################################
    def update_user(self, user_id, user):
        return self.user_service.update_user(user_id, user)

    ################################################################################
    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)