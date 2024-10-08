################################################################################
# Imports

from controller.user_controller import UserController
from controller.product_controller import ProductController
from controller.shopping_controller import ShoppingController
from config.config_database import ConfigDatabase
import os
import time

################################################################################
# Defined variables

config_database = ConfigDatabase()
user_controller = UserController(config_database)
product_controller = ProductController(config_database)
shopping_controller = ShoppingController(config_database)

################################################################################
def main():
    while True:
        print("1 - Usuário")
        print("2 - Produto")
        print("3 - Compra")
        print("4 - Logar")
        print("5 - Sair")

        print("O que deseja fazer?")
        opcao = int(input())
        
        match opcao:
            case 1:
                handle_user()
            case 2:
                handle_product()
            case 3:
                handle_shopping()
            case 4:
                handle_login()
            case 5:
                print("Saindo...")
                time.sleep(1.5)
                clear_screen()
                break
            case _:
                print("Opção inválida")
    
################################################################################
def handle_user():
    clear_screen()
    print("########## Usuário ##########");print()
    
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Listar")
    print("5 - Deletar")
    print("6 - Favoritar")
    print("7 - Sair")
        
    print()
    print("O que deseja fazer?")
    opcao = int(input())
    
    match opcao:
        case 1:
            user_controller.create_user()
        case 2:
            user_controller.get_user()
        case 3:
            user_controller.update_user()
        case 4:
            user_controller.get_all_users()
        case 5:
            user_controller.delete_user()
        case 6:
            user_controller.favorite_product()
        case 7:
            clear_screen()
            return
        case _:
            print("Opção inválida")

################################################################################
def handle_login():
    email = input("Digite o email: ")
    password = input("Digite a senha: ")
    
    pass

################################################################################
def handle_product():
    clear_screen()
    print("########## Produto ##########");print()
    
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Listar")
    print("5 - Deletar")
    print("6 - Sair")
    
    print()
    print("O que deseja fazer?")
    opcao = int(input())
    
    match opcao:
        case 1:
            product_controller.create_product()
        case 2:
            product_controller.get_product()
        case 3:
            product_controller.update_product()
        case 4:
            product_controller.get_all_products()
        case 5:
            product_controller.delete_product()
        case 6:
            clear_screen()
            return
        case _:
            print("Opção inválida")

################################################################################
def handle_shopping():
    clear_screen()
    print("########## Compra ##########");print()
    
    print("1 - Comprar")
    print("2 - Consultar")
    print("3 - Atualizar")
    print("4 - Listar")
    print("5 - Deletar")
    print("6 - Sair")
    
    print()
    print("O que deseja fazer?")
    opcao = int(input())
    
    match opcao:
        case 1:
            shopping_controller.buy_product()
        case 2:
            shopping_controller.get_shopping()
        case 3:
            shopping_controller.update_shopping()
        case 4:
            shopping_controller.get_all_shoppings()
        case 5:
            shopping_controller.delete_shopping()
        case 6:
            clear_screen()
            return
        case _:
            print("Opção inválida")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

################################################################################
if __name__ == '__main__':    
    main()