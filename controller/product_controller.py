################################################################################

from model.product_model import ProductModel
from controller.user_controller import UserController

################################################################################

class ProductController:
    
    def __init__(self, db):
        self.config_database = db
        self.product_model = ProductModel(self.config_database)
        self.user_controller = UserController(self.config_database)
    
    ################################################################################
    def create_product(self):
        
        # Get the product data
        name = str(input("Digite o nome do produto: "))
        price = float(input("Digite o preço do produto: ").replace(',', '.'))
        description = str(input("Digite a descrição do produto: "))
        
        # Select the seller
        all_sellers = self.user_controller.get_all_sellers()
        
        if len(all_sellers) == 0:
            print("Não há vendedores cadastrados.")
            return
        
        print("Digite o número do vendedor que deseja utilizar:")
        seller_index = int(input())
        seller_selected = all_sellers[seller_index-1]
        seller = {"id": seller_selected['_id'], "name": seller_selected['name']}
        
        self.product_model.create_product(name, price, description, seller)

    ################################################################################
    def get_product(self):
        pass
    
    ################################################################################
    def update_product(self):
        pass
    
    ################################################################################
    def get_all_products(self):
        pass
    
    ################################################################################
    def delete_product(self):
        pass