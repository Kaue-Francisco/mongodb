class ProductModel:

    def __init__(self, session, cluster):
        self.session = session
        self.cluster = cluster

    ################################################################################
    def create_product(self, name, price, vendor_id):
        self.session.execute(f"INSERT INTO produto (id, nome, preco, vendedor_id) VALUES (uuid(), '{name}', {price}, {vendor_id})")

    ################################################################################
    def get_all_products(self):
        return list(self.session.execute("SELECT * FROM produto;"))
    
################################################################################