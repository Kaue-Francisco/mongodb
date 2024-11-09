class UsuarioModel:
    def __init__(self, conn):
        self.conn = conn

    def cadastrar_usuario(self, nome, email, senha, vendedor):
        query = """
        CREATE (u:Usuario {vendedor: $vendedor, senha: $senha, email: $email, nome: $nome})
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query, nome=nome, email=email, senha=senha, vendedor=vendedor)
            result.single()

    def consultar_usuario(self, email):
        query = """
        MATCH (u:Usuario {email: $email})
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query, email=email)
            return result.single()
        
    def todos_vendedores(self):
        query = """
        MATCH (u:Usuario {vendedor: true})
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query)
            vendedores = [record["u"] for record in result]
            return vendedores
    
    def todos_usuarios(self):
        query = """
        MATCH (u:Usuario)
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query)
            usuarios = [record["u"] for record in result]
            return usuarios