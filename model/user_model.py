################################################################################
class UserModel():

    def __init__(self, session, cluster):
        self.session = session
        self.cluster = cluster
    
    ################################################################################
    def create_user(self, user):
        self.session.execute(
            f"""
            INSERT INTO usuario (id, nome, email, senha, vendedor, data_cadastro)
            VALUES (uuid(), '{user['nome']}', '{user['email']}', '{user['senha']}', {user['vendedor']}, '{user['data_cadastro']}');
            """
        )

    ################################################################################
    def get_all_users(self):
        return list(self.session.execute("SELECT * FROM usuario;"))
    
    ################################################################################
    def update_user(self, user):
        self.session.execute(
            f"""
            UPDATE usuario
            SET nome = '{user['nome']}', email = '{user['email']}', senha = '{user['senha']}', vendedor = {user['vendedor']}
            WHERE id = {user['id']};
            """
        )

################################################################################