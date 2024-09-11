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
            'registration_data': registration_data,
            'favorite_products': []
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
    
    ################################################################################
    def favorite_product(self, id_user: str, id_product: str, name_product: str) -> None:
        self.table_user.update_one(
            {'_id': id_user},
            {'$addToSet': {'favorite_products': {'id_product': id_product, 'name_product': name_product}}}
        )
    
    ################################################################################
    def get_all_favorites(self, user_id: str) -> list:
        # Encontrar o usuário pelo ID
        user = self.table_user.find_one({'_id': user_id}, {'favorite_products': 1, '_id': 0})
        
        # Se o usuário for encontrado, retornar a lista de produtos favoritos
        if user:
            return user.get('favorite_products', [])
        
        # Caso contrário, retornar uma lista vazia
        return []
    
    ################################################################################
    def remove_favorite(self, user_id: str, product_id: str):
        self.table_user.update_one(
            {'_id': user_id},
            {'$pull': {'favorite_products': {'id_product': product_id}}}
        )