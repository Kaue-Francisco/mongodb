from model.shopping_model import ShoppingModel
from model.product_model import ProductModel
from model.user_model import UserModel

class ShoppingController:

    def __init__(self, session, cluster):
        self.session = session
        self.cluster = cluster
        self.product_model = ProductModel(session, cluster)
        self.user_model = UserModel(session, cluster)
        self.shopping_model = ShoppingModel(session, cluster)

    def do_shopping(self):
        
        all_products = self.product_model.get_all_products()

        if not all_products:
            print("Nenhum produto encontrado")
            return

        for index, product in enumerate(all_products):
            print(f"{index+1}. {product.nome} - {product.preco}")

        opcao = int(input("Digite o número do produto que deseja comprar: "))

        product = all_products[opcao-1]

        all_users = self.user_model.get_all_users()

        if not all_users:
            print("Nenhum usuário encontrado")
            return

        for index, user in enumerate(all_users):
            print(f"{index+1}. {user.nome} - {user.email}")

        opcao = int(input("Digite o número do usuário que deseja comprar: "))

        user = all_users[opcao-1]

        quantity = int(input("Digite a quantidade que deseja comprar: "))
        total = quantity * product.preco

        self.shopping_model.insert_shopping(user.id, product.id, quantity, total, product.vendedor_id)

    def get_all_shopping(self):
        return self.shopping_model.get_all_shopping()
        
    def delete_shopping(self):
        all_shopping = list(self.get_all_shopping())

        if not all_shopping:
            print("Nenhuma compra encontrada")
            return

        for index, shopping in enumerate(all_shopping):
            print(f"{index+1}. {shopping.usuario_id} - {shopping.produto_id} - {shopping.quantidade} - {shopping.total}")

        opcao = int(input("Digite o número da compra que deseja excluir: "))

        if opcao < 1 or opcao > len(all_shopping):
            print("Opção inválida")
            return

        shopping = all_shopping[opcao-1]

        self.shopping_model.delete_shopping(shopping.id)