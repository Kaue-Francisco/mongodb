class UserModel:
    def __init__(self, config_database):
        self.config_database = config_database
        self.db = self.config_database.get_db()
        self.table_user = self.db.users

    ################################################################################
    def get_user(self, user_id):
        return self.db.get_user(user_id)

    ################################################################################
    def create_user(self, name, email, password, seller, registration_data):
        user = {
            'name': name,
            'email': email,
            'password': password,
            'seller': seller,
            'registration_data': registration_data
        }
        
        self.table_user.insert_one(user)
        
    ################################################################################
    def email_exists(self, email):
        return self.table_user.find_one({'email': email}) is not None