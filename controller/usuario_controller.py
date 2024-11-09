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
            print(f"Usuário: {record['nome']}\nEmail: {record['email']}\nSenha: {record['senha']}\n")