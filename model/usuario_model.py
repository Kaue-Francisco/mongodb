class UsuarioModel:
    def __init__(self, conn):
        self.conn = conn

    def cadastrar_usuario(self, nome, email, senha, vendedor):
        query = """
        CREATE (u:Usuario {vendedor: $vendedor, senha: $senha, email: $email, nome: $nome})
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query, nome=nome, email=email, senha=senha)
            result.single()

    def consultar_usuario(self, email):
        query = """
        MATCH (u:Usuario {email: $email})
        RETURN u
        """
        with self.conn.session() as session:
            result = session.run(query, email=email)
            return result.single()