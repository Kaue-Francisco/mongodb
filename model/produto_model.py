class ProdutoModel:
    def __init__(self, conn):
        self.conn = conn
    
    def cadastrar_produto(self, nome, preco, vendedor):
        query = """
        MATCH (u:Usuario {email: $email})
        CREATE (p:Produto {id: apoc.create.uuid(), nome: $nome, preco: $preco})
        CREATE (u)-[:VENDE]->(p)
        """
        with self.conn.session() as session:
            session.run(query, nome=nome, preco=preco, email=vendedor['email'])
        
    def todos_produtos(self):
        query = """
        MATCH (p:Produto)
        RETURN p
        """
        with self.conn.session() as session:
            result = session.run(query)
            produtos = [{"element_id": record["p"].element_id, "nome": record["p"]["nome"], "preco": record["p"]["preco"]} for record in result]
            return produtos
    
    def vendedor_produto(self, produto):
        query = """
        MATCH (p:Produto)<-[:VENDE]-(u:Usuario)
        WHERE elementId(p) = $element_id
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query, element_id=produto['element_id'])
            return result.single()["u"]
        
    def todos_produtos(self):
        query = """
        MATCH (p:Produto)
        RETURN p
        """
        with self.conn.session() as session:
            result = session.run(query)
            produtos = [{"element_id": record["p"].element_id, "nome": record["p"]["nome"], "preco": record["p"]["preco"]} for record in result]
            return produtos