################################################################################
# Imports

from config.connect_database import ConnectDatabase
from controller.usuario_controller import UsuarioController
from controller.produto_controller import ProdutoController
# from controller.compra_controller import CompraController

################################################################################

class Menu:
    def __init__(self):
        self.database_config = ConnectDatabase()
        self.conn = self.database_config.connect_neo4j()
        self.usuario_controller = UsuarioController(self.conn)
        self.produto_controller = ProdutoController(self.conn)

    def usuario_menu(self):
        while True:
            print("1 - Cadastrar usuário")
            print("2 - Consultar usuário")
            print("3 - Sair")

            opcao = int(input("Digite a opção desejada: "))

            if opcao < 1 or opcao > 3:
                print("Opção inválida")
                return
            
            if opcao == 1:
                self.usuario_controller.cadastrar_usuario()
            elif opcao == 2:
                self.usuario_controller.consultar_usuario()
            elif opcao == 3:
                return

    ################################################################################
    def produto_menu(self):
        while True:
            print("1 - Cadastrar produto")
            print("2 - Consultar produto")
            print("3 - Sair")

            opcao = int(input("Digite a opção desejada: "))

            if opcao < 1 or opcao > 3:
                print("Opção inválida")
                return
            
            if opcao == 1:
                self.produto_controller.cadastrar_produto()
            elif opcao == 2:
                self.produto_controller.consultar_produto()
            elif opcao == 3:
                return

    ################################################################################
    def compra_menu(self):
        while True:
            print("1 - Realizar compra")
            print("2 - Consultar compra")
            print("3 - Sair")

            opcao = int(input("Digite a opção desejada: "))

            if opcao < 1 or opcao > 3:
                print("Opção inválida")
                return
            
            if opcao == 1:
                self.realizar_compra()
            elif opcao == 2:
                self.consultar_compra()
            elif opcao == 3:
                return

    ################################################################################
    def main_menu(self):

        while True:
            print("1 - Usuario")
            print("2 - Produto")
            print("3 - Compra")
            print("4 - Sair")

            opcao = int(input("Digite a opção desejada: "))

            if opcao < 1 or opcao > 4:
                print("Opção inválida")
                return
            
            if opcao == 1:
                self.usuario_menu()
            elif opcao == 2:
                self.produto_menu()
            elif opcao == 3:
                self.compra_menu()
            elif opcao == 4:
                break

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()