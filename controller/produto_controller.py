from controller.usuario_controller import UsuarioController
from model.produto_model import ProdutoModel

class ProdutoController:
    def __init__(self, conn):
        self.conn = conn
        self.produto_model = ProdutoModel(conn)
        self.usuario_controller = UsuarioController(conn)

    def cadastrar_produto(self):

        print("Selecione o vendedor:")
        vendedores = self.usuario_controller.todos_vendedores()
        
        if vendedores is False:
            return
        
        opcao = int(input("Digite o número do vendedor desejado: "))

        if opcao < 0 or opcao > len(vendedores):
            print("Opção inválida")
            return
        
        vendedor = vendedores[opcao-1]

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        self.produto_model.cadastrar_produto(nome, preco, vendedor)

    def consultar_produto(self):
        produtos = self.todos_produtos()

        opcao = int(input("Digite o número do produto desejado: "))

        if opcao < 0 or opcao > len(produtos):
            print("Opção inválida")
            return
        
        produto = produtos[opcao-1]
        vendedor = self.produto_model.vendedor_produto(produto)

        print(f"Produto: {produto['nome']}\nPreço: R$ {produto['preco']}\nNome-Vendedor: {vendedor['nome']}\nEmail-Vendedor: {vendedor['email']}\n")

    def todos_produtos(self):
        result = self.produto_model.todos_produtos()
        produtos = []

        if result is None:
            print("Nenhum produto encontrado.")
            return

        for index, record in enumerate(result):
            print(f"{index+1} - {record['nome']} - R$ {record['preco']}")
            produtos.append(record)

        return produtos