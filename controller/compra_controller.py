from controller.usuario_controller import UsuarioController
from controller.produto_controller import ProdutoController
from model.compra_model import CompraModel

class CompraController:
    def __init__(self, conn):
        self.conn = conn
        self.usuario_controller = UsuarioController(conn)
        self.produto_controller = ProdutoController(conn)
        self.compra_model = CompraModel(conn)

    def realizar_compra(self):
        print("Selecione o comprador:")
        usuarios = self.usuario_controller.todos_usuarios()

        opcao = int(input("Digite o número do comprador desejado: "))

        if opcao < 0 or opcao > len(usuarios):
            print("Opção inválida")
            return
        
        comprador = usuarios[opcao-1]

        print("Selecione o produto:")
        produtos = self.produto_controller.todos_produtos()

        opcao = int(input("Digite o número do produto desejado: "))

        if opcao < 0 or opcao > len(produtos):
            print("Opção inválida")
            return
        
        produto = produtos[opcao-1]
        quantidade = int(input("Digite a quantidade desejada: "))
        valor_total = quantidade * produto["preco"]

        self.compra_model.realizar_compra(comprador, produto, quantidade, valor_total)

    def todas_compras(self):
        compras = self.compra_model.todas_compras()

        for index, record in enumerate(compras):
            print(f"{index+1} - {record['comprador']['nome']} - {record['produto']['nome']}")

        return compras

    def consultar_compra(self):
        print("Qual compra deseja consultar?")
        compras = self.todas_compras()

        opcao = int(input("Digite o número da compra desejada: "))

        if opcao < 0 or opcao > len(compras):
            print("Opção inválida")
            return

        compra = compras[opcao-1]

        print(f"Comprador: {compra['comprador']['nome']}\nProduto: {compra['produto']['nome']}\nQuantidade: {compra['compra']['quantidade']}\nValor Total: R$ {compra['compra']['valor_total']}")    