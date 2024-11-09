class CompraModel:
    def __init__(self, conn):
        self.conn = conn

    def realizar_compra(self, comprador, produto, quantidade, valor_total):
        create_query = """
        MATCH (u:Usuario {email: $email_comprador})
        MATCH (p:Produto)
        WHERE elementId(p) = $element_id_produto
        CREATE (u)-[:COMPRA {quantidade: $quantidade, valor_total: $valor_total}]->(p)
        RETURN u, p
        """

        try:
            with self.conn.session() as session:
                result = session.run(
                    create_query,
                    email_comprador=comprador['email'],
                    element_id_produto=produto['element_id'],
                    quantidade=quantidade,
                    valor_total=valor_total
                )
                record = result.single()
                
                if record:
                    print("Compra realizada com sucesso.")
                    return record
                else:
                    print("Usuário ou Produto não encontrado.")
                    return None
        except Exception as e:
            print(f"Ocorreu um erro ao realizar a compra: {e}")

    def todas_compras(self):
        query = """
        MATCH (u:Usuario)-[c:COMPRA]->(p:Produto)
        RETURN u, c, p
        """
        with self.conn.session() as session:
            result = session.run(query)
            compras = [{"comprador": record["u"], "compra": record["c"], "produto": record["p"]} for record in result]
            return compras