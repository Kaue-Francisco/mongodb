################################################################################

from pymongo import MongoClient
from model.product_model import ProductModel
from controller.user_controller import UserController

################################################################################

class ProductController:
    
    def __init__(self, db: MongoClient) -> None:
        self.config_database = db
        self.product_model = ProductModel(self.config_database)
        self.user_controller = UserController(self.config_database)
    
    ################################################################################
    def create_product(self) -> None:
        
        # Get the product data
        name = str(input("Digite o nome do produto: "))
        price = float(input("Digite o preço do produto: ").replace(',', '.'))
        description = str(input("Digite a descrição do produto: "))
        
        # Select the seller
        all_sellers = self.user_controller.get_all_sellers()
        
        if len(all_sellers) == 0:
            print("Não há vendedores cadastrados.")
            return
        
        seller_index = self.get_valid_index(all_sellers, "Digite o número do vendedor que deseja utilizar:")
        seller_selected = all_sellers[seller_index]
        seller = {"id": seller_selected['_id'], "name": seller_selected['name']}
        
        self.product_model.create_product(name, price, description, seller)

    ################################################################################
    def get_product(self) -> None:
        print("Digite o nome do produto que você deseja buscar: ")
        name_product = str(input())
        products = self.product_model.get_product(name_product)
        
        if len(products) == 0:
            print()
            print("Não foi encontrado esse produto!")
            print()
            return
        
        print();print("Produtos encontrados")
        for index, product in enumerate(products):
            print(f"{index + 1} - {product['name']} - Price: {product['price']} - Vendedor: {product['seller']['name']}")
        
        print()
    
    ################################################################################
    def update_product(self) -> None:
        print("Todos os produtos cadastrados:")
        all_products = self.get_all_products()
        print("Digite o número do produto que deseja atualizar:")
        product_index = int(input())
        
        product_selected = all_products[product_index-1]
        
        print("1 - Nome")
        print("2 - Preço")
        print("3 - Descrição")
        print("4 - Sair")
        
        option = self.get_valid_index([1, 2, 3, 4], "Digite o número do campo que deseja atualizar:", True)
        
        match option:
            case 1:
                new_name = str(input("Digite o novo nome: "))
                self.product_model.update_product(product_selected['_id'], 'name', new_name)
            case 2:
                new_price = float(input("Digite o novo preço: ").replace(',', '.'))
                self.product_model.update_product(product_selected['_id'], 'price', new_price)
            case 3:
                new_description = str(input("Digite a nova descrição: "))
                self.product_model.update_product(product_selected['_id'], 'description', new_description)
            case 4:
                print("Saindo...")
                return
    
    ################################################################################
    def get_all_products(self) -> list:
        all_products = []
        
        for i, product in enumerate(self.product_model.get_all_products()):
            seller = product['seller']
            print(f"{i+1} - {product['name']} - R$ {product['price']} - Vendedor: {seller['name']}")
            all_products.append(product)
        
        print()
        
        return all_products
    
    ################################################################################
    def delete_product(self) -> None:
        print("Todos os produtos cadastrados:")
        all_products = self.get_all_products()
        product_index = self.get_valid_index(all_products, "Digite o número do produto que deseja deletar:")
        
        product_selected = all_products[product_index]
        
        self.product_model.delete_product(product_selected['_id'])
    
    ################################################################################
    def get_valid_index(self, items: dict, prompt: str, update=False) -> int:
        while True:
            print(prompt)
            index = int(input())
            
            if update == True:
                if 1 <= index <= len(items):
                    return index
                print("Índice inválido. Tente novamente")
                continue    
            
            if 1 <= index <= len(items):
                return index - 1
            
            print("Índice inválido. Tente novamente.")