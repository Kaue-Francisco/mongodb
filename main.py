################################################################################
# Imports

from controller.user_controller import UserController
from config.config_database import ConfigDatabase
import os
import time

################################################################################
# Defined variables

config_database = ConfigDatabase()
user_controller = UserController(config_database)

################################################################################
def main():
    while True:
        print("1 - Usuário")
        print("2 - Produto")
        print("3 - Compra")
        print("4 - Sair")

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
        case _:
            print("Opção inválida")

################################################################################
def handle_product():
    data = {
        'name': 'Produto 1',
        'price': 10.0,
        'quantity': 10
    }

################################################################################
def handle_shopping():
    data = {
        'user_id': 1,
        'product_id': 1,
        'quantity': 2
    }

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

################################################################################
if __name__ == '__main__':    
    main()