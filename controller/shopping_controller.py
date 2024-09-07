################################################################################
# Imports

from model.shopping_model import ShoppingModel
from controller.product_controller import ProductController
from controller.user_controller import UserController
import datetime

################################################################################

class ShoppingController:
    
    def __init__(self, db):
        self.config_database = db
        self.shopping_model = ShoppingModel(self.config_database)
        self.product_controller = ProductController(self.config_database)
        self.user_controller = UserController(self.config_database)
    
    ################################################################################
    
    def buy_product(self) -> None:
        print("Qual produto deseja comprar?")
        all_products = self.product_controller.get_all_products()
        print("Digite o index do produto que deseja comprar:")
        product_index = self.get_valid_index(all_products, "Digite o index do produto que deseja comprar:")
        product_selected = all_products[product_index-1]
        
        print("Digite a quantidade que deseja comprar:")
        quantity = int(input())
        
        print("Qual usuário está comprando?")
        all_users = self.user_controller.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o index do usuário que deseja comprar:")
        user_selected = all_users[user_index-1]
        
        price_total = product_selected['price'] * quantity
        
        date = datetime.datetime.now()
        
        user = {
            '_id': user_selected['_id'],
            'name': user_selected['name']
        }
        
        product = {
            '_id': product_selected['_id'],
            'name': product_selected['name'],
            'price': product_selected['price']
        }
        
        self.shopping_model.buy_product(user,          # User
                                        quantity,      # Quantity
                                        price_total,   # Total price
                                        date,          # Date of purchase
                                        product)       # Product
        
    ################################################################################
    def get_shopping(self) -> None:
        print("Compra de qual usuário deseja consultar?")
        all_users = self.user_controller.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o index do usuário que deseja consultar:")
        user_selected = all_users[user_index-1]
        
        shoppings = self.get_shopping_for_user(user_selected['_id'])
        
        if len(shoppings) == 0:
            print("Nenhuma compra encontrada para este usuário.")
            return
        
    ################################################################################
    def get_shopping_for_user(self, user_id: str) -> None:
        shoppings = self.shopping_model.get_all_shopping_for_user(user_id)
        all_shopping_for_user = []
        
        if len(shoppings) == 0:
            return []
        
        for index, shopping in enumerate(shoppings):
            print(f"{index+1} - Produto: {shopping['product']['name']}")
            print(f"  | Quantidade: {shopping['quantity']}")
            print(f"  | Preço total: {shopping['price_total']}")
            print(f"  | Data: {shopping['date'].strftime('%d/%m/%Y')}")
            print("   ---------------------------------")
            all_shopping_for_user.append(shopping)
            
        return all_shopping_for_user
    
    ################################################################################
    def get_all_shoppings(self) -> None:
        shoppings = self.shopping_model.get_all_shoppings()
        
        if len(shoppings) == 0:
            print("Nenhuma compra encontrada.")
            return
        
        for index, shopping in enumerate(shoppings):
            print(f"{index+1} - Produto: {shopping['product']['name']}")
            print(f"  | Quantidade: {shopping['quantity']}")
            print(f"  | Preço total: {shopping['price_total']}")
            print(f"  | Data: {shopping['date'].strftime('%d/%m/%Y')}")
            print(f"  | Cliente: {shopping['user']['name']}")
            print("   ---------------------------------")
    
    ################################################################################
    def delete_shopping(self) -> None:
        print("Compra de qual usuario você deseja deletar?")
        all_users = self.user_controller.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o index do usuário que deseja consultar:")
        user_selected = all_users[user_index-1]

        shoppings = self.get_shopping_for_user(user_selected['_id'])
        
        if len(shoppings) == 0:
            print("Nenhuma compra encontrada para este usuário.")
            return

        shopping_index = self.get_valid_index(shoppings, "Digite o index da compra que deseja deletar:")
        shopping_selected = shoppings[shopping_index-1]
        
        self.shopping_model.delete_shopping(shopping_selected['_id'])
        
    ################################################################################
    def update_shopping(self) -> None:
        print("Compra de qual usuário deseja atualizar?")
        all_users = self.user_controller.get_all_users()
        user_index = self.get_valid_index(all_users, "Digite o index do usuário que deseja consultar:")
        user_selected = all_users[user_index-1]
        
        shoppings = self.get_shopping_for_user(user_selected['_id'])
        
        if len(shoppings) == 0:
            print("Nenhuma compra encontrada para este usuário.")
            return
        
        shopping_index = self.get_valid_index(shoppings, "Digite o index da compra que deseja atualizar:")
        shopping_selected = shoppings[shopping_index-1]
        
        print("O que deseja atualizar?")
        print("1 - Quantidade")
        print("2 - Preço total")
        print("3 - Sair")
        
        option = self.get_valid_index([1, 2, 3], "Digite o index do campo que deseja atualizar:")
        
        match option:
            case 1:
                new_quantity = int(input("Digite a nova quantidade: "))
                self.shopping_model.update_shopping(shopping_selected['_id'], 'quantity', new_quantity)
            case 2:
                new_price_total = float(input("Digite o novo preço total: ").replace(',', '.'))
                self.shopping_model.update_shopping(shopping_selected['_id'], 'price_total', new_price_total)
            case 3:
                print("Saindo...")
                return
    
    ################################################################################
    def get_valid_index(self, items: dict, prompt: str) -> int:
        while True:
            print(prompt)
            index = int(input())
            if 1 <= index <= len(items):
                return index - 1
            print("Índice inválido. Tente novamente.")