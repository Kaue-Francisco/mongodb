################################################################################
# Imports

import datetime
import bcrypt
from model.user_model import UserModel

################################################################################
class UserController:
    def __init__(self, db):
        self.config_database = db
        self.user_model = UserModel(self.config_database)
        
        # Hashing the password
        self.salt = bcrypt.gensalt()

    ################################################################################
    def create_user(self):
        """ Create a new user """
        
        # Get the user data
        name = str(input("Digite o nome: "))
        while True:
            email = str(input("Digite o email: "))
            if not self.email_exists(email):
                break
            print("Email já cadastrado")
        password = bcrypt.hashpw(str(input("Digite a senha: ")).encode(), self.salt)
        seller = str(input("Você é um vendedor? (S/N) ")).upper() == 'S'
        registration_data = datetime.datetime.now()
        
        self.user_model.create_user(name, email, password, seller, registration_data)

    ################################################################################
    def update_user(self, user_id, user):
        return self.user_model.update_user(user_id, user)

    ################################################################################
    def delete_user(self, user_id):
        return self.user_model.delete_user(user_id)
    
    ################################################################################
    def get_user(self):
        email = str(input("Digite o email do usuario: "))
        while not self.email_exists(email):
            print("Email não cadastrado.")
            print("Digite N para sair.")
            email = str(input("Digite o email do usuario: "))
            
            if email.upper() == 'N':
                print("Saindo...")
                return
            
        print(self.user_model.get_user(email))
    
    ################################################################################
    def email_exists(self, email):
        return self.user_model.email_exists(email)