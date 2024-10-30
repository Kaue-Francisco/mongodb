################################################################################
# Imports

import bcrypt
import datetime
import os
from model.user_model import UserModel

################################################################################
class UserController:
    
    def __init__(self, session, cluster):
        self.session = session
        self.cluster = cluster
        self.user_model = UserModel(session, cluster)

    ################################################################################
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    ################################################################################
    def create_usuario(self):
        self.clear_console()

        print("---------- Cadastrar Usuário ----------")
        print()

        nome = input("Digite o nome: ")
        email = input("Digite o Email: ")
        senha = bcrypt.hashpw(input("Digite a senha: ").encode(), bcrypt.gensalt()).decode()
        vendedor = input("É vendedor? (S/N): ").upper() == 'S'
        data_cadastro = datetime.datetime.now()

        user = {"nome": nome, "email": email, "senha": senha, "vendedor": vendedor, "data_cadastro": data_cadastro}

        self.user_model.create_user(user)

        print("Usuário cadastrado com sucesso.")

    ################################################################################
    def update_usuario(self):
        todos_usuarios = self.user_model.get_all_users()

        for index, usuario in enumerate(todos_usuarios):
            print(f"{index + 1}. {usuario.nome}")

        opcao = int(input("Escolha um usuário para atualizar: "))

        if opcao < 1 or opcao > len(todos_usuarios):
            print("Usuário inválido.")
            return

        usuario = todos_usuarios[opcao - 1]

        nome = usuario.nome
        email = usuario.email
        senha = usuario.senha
        vendedor = usuario.vendedor

        self.clear_console()
        print("---------- Atualizar Usuário ----------")
        print()

        print("1. Nome")
        print("2. Email")
        print("3. Senha")
        print("4. Vendedor")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                nome = input("Digite o nome: ")
            case "2":
                email = input("Digite o Email: ")
            case "3":
                senha = bcrypt.hashpw(input("Digite a senha: ").encode(), bcrypt.gensalt()).decode()
            case "4":
                vendedor = input("É vendedor? (S/N): ").upper() == 'S'
            case "5":
                return
            case _:
                print("Opção inválida.")

        user = {"id": usuario.id, "nome": nome, "email": email, "senha": senha, "vendedor": vendedor}

        self.user_model.update_user(user)

    def get_all_sellers(self):
        return self.user_model.get_all_sellers()

################################################################################