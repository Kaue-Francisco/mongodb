class ProductModel:
    
    def __init__(self, db) -> None:
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
    def update_product(self, product_id, field, value):
        self.table_product.update_one({'_id': product_id}, {'$set': {field: value}})
        
    ################################################################################
    def get_all_products(self):
        products = self.table_product.find()
        return list(products)