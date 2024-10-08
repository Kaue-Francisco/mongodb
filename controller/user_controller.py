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
    def create_user(self) -> None:
        
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
    def update_user(self) -> None:
        
        print("Todos os usuários cadastrados:")
        all_users = self.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o número do usuário que deseja atualizar:")
        
        user_selected = all_users[user_index]
        
        print("1 - Nome")
        print("2 - Email")
        print("3 - Senha")
        print("4 - Vendedor")
        print("5 - Remover Favoritos")
        print("6 - Sair")
        
        option = self.get_valid_index([1, 2, 3, 4, 5, 6], "Digite o número do campo que deseja atualizar:", True)
        
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
                favorites = self.get_all_favorites(user_selected['_id'])
                
                if favorites is None or len(favorites) == 0:
                    return
                
                favorite_index = self.get_valid_index(favorites, "Digite o número do favorito que deseja remover:")
                favorite_selected = favorites[favorite_index]
                self.user_model.remove_favorite(user_selected['_id'], favorite_selected['id_product'])
            case 6:
                print("Saindo...")
                return
            case _:
                print("Opção inválida")
        
    ################################################################################
    def delete_user(self) -> None:
        
        print("Todos os usuários cadastrados:")
        all_users = self.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o número do usuário que deseja deletar:")
        user_selected = all_users[user_index]
        
        self.user_model.delete_user(user_selected['_id'])
    
    ################################################################################
    def get_user(self) -> dict:
        
        email = str(input("Digite o email do usuario: "))
        while not self.email_exists(email):
            print("Email não cadastrado.")
            print("Digite N para sair.")
            email = str(input("Digite o email do usuario: "))
            
            if email.upper() == 'N':
                print("Saindo...")
                return
        
        user = self.user_model.get_user(email)
        print("Nome: ", user['name'])
        print("Email: ", user['email'])
        print("É vendedor? ", user['seller'])
        if 'favorites_products' not in user or not user['favorite_products']:
            print("Favoritos: Não há favoritos")
        else:
            print("Favoritos:")
            for product in user['favorite_products']:
                print(" - ", product['name_product'])

        print("Data de cadastro: ", user['registration_data'])
        print()
    
    ################################################################################
    def get_all_users(self) -> list:
        
        all_users = []
        users = self.user_model.get_all_users()
        print()
        
        for i, user in enumerate(users):
            print(f"{i+1} - {user['name']} - {user['email']}")
            all_users.append(user)
        
        print()
            
        return all_users
    
    ################################################################################
    def get_all_sellers(self) -> list:
        all_sellers = []
        sellers = self.user_model.get_all_sellers()
        print()
        
        for i, seller in enumerate(sellers):
            print(f"{i+1} - {seller['name']}")
            all_sellers.append(seller)
        
        print()
        
        return all_sellers
    
    ################################################################################
    def email_exists(self, email: str) -> bool:
        return self.user_model.email_exists(email)
    
    ################################################################################
    def get_valid_index(self, items: dict, prompt: str, favorite=False) -> int:
        while True:
            print(prompt)
            index = int(input())
            if favorite == True:
                if 1 <= index <= len(items):
                    return index
                print("Índice inválido. Tente novamente.")
                continue
                
            if 1 <= index <= len(items):
                return index - 1
            print("Índice inválido. Tente novamente.")
    
    ################################################################################
    def favorite_product(self):
        from controller.product_controller import ProductController
        
        print("Selecione o usuário:")
        all_users = self.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o número do usuário que deseja favoritar um produto:")
        user_selected = all_users[user_index]
        
        print("Selecione o produto:")
        all_products = ProductController(self.config_database).get_all_products()
        product_index = self.get_valid_index(all_products, "Digite o número do produto que deseja favoritar:")
        product_selected = all_products[product_index]
        
        self.user_model.favorite_product(user_selected['_id'], product_selected['_id'], product_selected['name'])
        
    ################################################################################
    def get_all_favorites(self, user_id: str):
        all_favorites = []
        favorites = self.user_model.get_all_favorites(user_id)
        print()
        if favorites == None or len(favorites) == 0:
            print("O usuário não tem favoritos.")
            return favorites
        
        for i, favorite in enumerate(favorites):
            print(f"{i+1} - {favorite['name_product']}")
            all_favorites.append(favorite)
        
        print()
        
        return all_favorites
    
    ################################################################################
    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password)
    
    ################################################################################
    def login(self):
        while True:
            email = input("Digite o email: ")
            password = input("Digite a senha: ")
            
            user = self.user_model.get_user(email)
            
            is_password = self.check_password(password, user['password'])
            
            if is_password:
                redis_conn = self.config_database.get_redis()
                redis_conn.setex(f"user: {user['_id']}", 120, user['email'])
                
                print("Usuário logado com sucesso")
                return
            
            print("Email ou senha inválidos")
            
            opcao = input("Deseja tentar novamente? (S/N) ").upper()
            if opcao == 'N':
                return