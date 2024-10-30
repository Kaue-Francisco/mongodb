################################################################################
# Imports

from config.connect_database import ConnectDatabase
from controller.user_controller import ControllerUser
import datetime
import bcrypt
import os

################################################################################
class Menu:
    
    def __init__(self):
        self.config_database = ConnectDatabase()
        self.config_database.connect_cassandra()
        self.config_database.create_tables()
        self.session, self.cluster = self.config_database.get_connect()
        self.user_controller = ControllerUser(self.session, self.cluster)

    ################################################################################
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    ################################################################################
    def menu_usuario(self):
        self.clear_console()

        print("---------- Usuario ----------")
        print()
        print("1. Cadastrar")
        print("2. Atualizar")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                self.user_controller.create_usuario()
            case "2":
                self.user_controller.update_usuario()
            case "3":
                return
            case _:
                print("Opção inválida.")

    ################################################################################
    def main(self):

        while True:
            self.clear_console()

            print('****************************')
            print("Atividade com Cassandra.")
            print('****************************')

            print()

            print("1. Usuário")
            print("2. Produto")
            print("3. Compra")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1":
                    self.menu_usuario()
                case "2":
                    print("Produto")
                case "3":
                    print("Compra")
                case "4":
                    break
                case _:
                    print("Opção inválida.")

        
        self.session.shutdown()
        self.cluster.shutdown()

################################################################################
if __name__ == "__main__":
    menu = Menu()
    menu.main()