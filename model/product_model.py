################################################################################
# Imports

from pymongo import MongoClient

################################################################################
class ProductModel:
    
    def __init__(self, db: MongoClient) -> None:
        self.config_database = db
        self.db = self.config_database.get_db()
        self.table_product = self.db.products
        
    ################################################################################
    def create_product(self, 
                        name: str,                      # Product name
                        price: float,                   # Product price
                        description: str,               # Product quantity
                        seller: dict):                  # Seller ID and Name
        
        product ={
            'name': name,
            'price': price,
            'description': description,
            'seller': seller
        }
        
        self.table_product.insert_one(product)
    
    ################################################################################
    def delete_product(self, product_id: str) -> None:
        self.table_product.delete_one({"_id": product_id})
    
    ################################################################################
    def update_product(self, product_id: str, field: str, value: str) -> None:
        self.table_product.update_one({'_id': product_id}, {'$set': {field: value}})
        
    ################################################################################
    def get_all_products(self) -> None:
        products = self.table_product.find()
        return list(products)
    
    ################################################################################
    def get_product(self, name_product) -> None:
        return list(self.table_product.find({"name": name_product}))