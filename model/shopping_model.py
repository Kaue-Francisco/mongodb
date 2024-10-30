class ShoppingModel:

    def __init__(self, session, cluster):
        self.session = session
        self.cluster = cluster

    def insert_shopping(self, user_id, product_id, quantity, total, seller_id):
        self.session.execute(f"""
        INSERT INTO compra (id, usuario_id, produto_id, quantidade, total, vendedor_id)
        VALUES (uuid(), {user_id}, {product_id}, {quantity}, {total}, {seller_id});
        """)

    def get_all_shopping(self):
        return self.session.execute("SELECT * FROM compra;")
    
    def delete_shopping(self, shopping_id):
        self.session.execute(f"DELETE FROM compra WHERE id = {shopping_id};")