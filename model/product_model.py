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