from model.usuario_model import UsuarioModel
import bcrypt

class UsuarioController:
    def __init__(self, conn):
        self.conn = conn
        self.usuario_model = UsuarioModel(conn)

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        senha = bcrypt.hashpw(input("Digite a senha do usuário: ").encode(), bcrypt.gensalt())
        vendedor = input("O usuário é vendedor? (S/N): ").upper() == "S"

        self.usuario_model.cadastrar_usuario(nome, email, senha, vendedor)
    
    def consultar_usuario(self):
        email = input("Digite o email do usuário: ")

        result = self.usuario_model.consultar_usuario(email)
        
        if result is None:
            print("Usuário não encontrado.")
            return

        for record in result:
            print(f"Usuário: {record['nome']}\nEmail: {record['email']}\nSenha: {record['senha']}\nVendedor: {record['vendedor']}\n")

    def todos_vendedores(self):
        result = self.usuario_model.todos_vendedores()
        vendedores = []

        if result is None:
            print("Nenhum vendedor encontrado.")
            return

        for index, record in enumerate(result):
            print(f"{index+1} - {record['nome']}")
            vendedores.append(record)

        return vendedores
    
    def todos_usuarios(self):
        result = self.usuario_model.todos_usuarios()
        usuarios = []

        if result is None:
            print("Nenhum usuario encontrado.")
            return

        for index, record in enumerate(result):
            print(f"{index+1} - {record['nome']}")
            usuarios.append(record)

        return usuarios