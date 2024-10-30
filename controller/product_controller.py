################################################################################
# Imports

from model.product_model import ProductModel
from controller.user_controller import UserController
import os

################################################################################
class ProductController:

    def __init__(self, session, cluster):
        self.session = session
        self.cluster = cluster
        self.product_model = ProductModel(self.session, self.cluster)
        self.user_controller = UserController(self.session, self.cluster)

    ################################################################################
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    ################################################################################
    def create_product(self):

        all_sellers = self.user_controller.get_all_sellers()
        
        if len(all_sellers) == 0:
            print("Não há vendedores cadastrados.")
            return
        
        for index, seller in enumerate(all_sellers):
            print(f"{index + 1}. {seller.nome}")

        seller_index = int(input("Escolha um vendedor para cadastrar o produto: "))

        if seller_index < 1 or seller_index > len(all_sellers):
            print("Vendedor inválido.")
            return
        
        seller = all_sellers[seller_index - 1]

        print("---------- Cadastrar Produto ----------")
        print()

        name = input("Nome: ")
        price = input("Preço: ")
        vendor_id = seller.id

        self.product_model.create_product(name, price, vendor_id)

    ################################################################################
    def get_products(self):
        products = self.product_model.get_all_products()

        for index, product in enumerate(products):
            print(f"{index + 1} Nome: {product.nome}")
        
        opcao = int(input("Pressione qualquer tecla para voltar ao menu principal."))

        if opcao < 1 or opcao > len(products):
            print("Opção inválida.")
            return
        
        product = products[opcao - 1]

        print(f"Nome: {product.nome}")
        print(f"Preço: {product.preco}")

################################################################################