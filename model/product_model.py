################################################################################
# Imports

from pymongo import MongoClient
from bson import ObjectId

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
    def create_product_redis(self, 
                        name: str,                      # Product name
                        price: float,                   # Product price
                        description: str,               # Product quantity
                        seller_id: str,                 # Seller ID
                        seller_name: str):              # Seller Name

        
        redis_conn = self.config_database.get_redis()
        
        product ={
            'name': name,
            'price': price,
            'description': description,
            'seller_id': seller_id,
            'seller_name': seller_name
        }
        
        redis_conn.hmset(f"product:{name}", {k: str(v) for k, v in product.items()})
    
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
    
    ################################################################################
    def get_all_products_redis(self) -> list:
        redis_conn = self.config_database.get_redis()
        product_keys = redis_conn.keys("product:*")
        
        products = []
        
        if len(product_keys) == 0:
            return products
        
        for key in product_keys:
            product_data = redis_conn.hgetall(key)
            product = {k.decode('utf-8'): v.decode('utf-8') for k, v in product_data.items() if k.decode('utf-8') != "seller_id" and k.decode('utf-8') != "seller_name"}
            
            # Decodifica seller_id para string antes de passar para ObjectId
            seller_id = product_data[b"seller_id"].decode('utf-8')
            product["seller"] = {"id": ObjectId(seller_id), "name": product_data[b"seller_name"].decode('utf-8')}
            
            redis_conn.delete(key)
            
            products.append(product)

        return products