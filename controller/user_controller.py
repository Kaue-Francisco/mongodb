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
    def update_user(self):
        
        print("Todos os usuários cadastrados:")
        all_users = self.get_all_users()
        print("Digite o número do usuário que deseja atualizar:")
        user_index = self.get_valid_index(all_users, "Digite o número do usuário que deseja atualizar:")
        
        user_selected = all_users[user_index-1]
        
        print("1 - Nome")
        print("2 - Email")
        print("3 - Senha")
        print("4 - Vendedor")
        print("5 - Sair")
        
        print("Digite o número do campo que deseja atualizar:")
        option = self.get_invalid_index([1, 2, 3, 4, 5], "Digite o número do campo que deseja atualizar:")
        
        match option:
            case 1:
                new_name = str(input("Digite o novo nome: "))
                self.user_model.update_user(user_selected['_id'], 'name', new_name)
            case 2:
                new_email = str(input("Digite o novo email: "))
                self.user_model.update_user(user_selected['_id'], 'email', new_email)
            case 3:
                new_password = bcrypt.hashpw(str(input("Digite a nova senha: ")).encode(), self.salt)
                self.user_model.update_user(user_selected['_id'], 'password', new_password)
            case 4:
                new_seller = str(input("Você é um vendedor? (S/N) ")).upper() == 'S'
                self.user_model.update_user(user_selected['_id'], 'seller', new_seller)
            case 5:
                print("Saindo...")
                return
            case _:
                print("Opção inválida")
        
    ################################################################################
    def delete_user(self):
        
        print("Todos os usuários cadastrados:")
        all_users = self.get_all_users()
        print("Digite o número do usuário que deseja deletar:")
        user_index = self.get_valid_index(all_users, "Digite o número do usuário que deseja deletar:")
        user_selected = all_users[user_index-1]
        
        self.user_model.delete_user(user_selected['_id'])
    
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
    def get_all_users(self):
        
        all_users = []
        users = self.user_model.get_all_users()
        print()
        
        for i, user in enumerate(users):
            print(f"{i+1} - {user['name']}")
            all_users.append(user)
        
        print()
            
        return all_users
    
    ################################################################################
    def get_all_sellers(self):
        all_sellers = []
        sellers = self.user_model.get_all_sellers()
        print()
        
        for i, seller in enumerate(sellers):
            print(f"{i+1} - {seller['name']}")
            all_sellers.append(seller)
        
        print()
        
        return all_sellers
    
    ################################################################################
    def email_exists(self, email):
        return self.user_model.email_exists(email)
    
    ################################################################################
    def get_valid_index(self, items, prompt):
        while True:
            print(prompt)
            index = int(input())
            if 1 <= index <= len(items):
                return index - 1
            print("Índice inválido. Tente novamente.")
    
    # be-improve: Adicionando tratamento para indice invalido,