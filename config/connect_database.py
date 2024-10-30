################################################################################
# Imports

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config.definitions import *

################################################################################
class ConnectDatabase:

    def __init__(self):
        self.session = None
        self.cluster = None

    ################################################################################
    def connect_cassandra(self):
        # Configuração da conexão com o banco de dados
        cloud_config = {
            'secure_connect_bundle': './secure-connect-mercado-livre.zip'
        }
        auth_provider = PlainTextAuthProvider(username='token', password=TOKEN)
        self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = self.cluster.connect()

        # Definir key space 
        keyspace = 'kaue'
        self.session.execute(f"USE {keyspace};")

        # Mensagem de sucesso
        print(f"Conexão estabelecida e keyspace '{keyspace}' selecionado com sucesso.")

    ################################################################################
    def create_tables(self):
        # Criar tabela usuario
        self.session.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id UUID PRIMARY KEY,
            nome TEXT,
            email TEXT,
            senha TEXT,
            vendedor BOOLEAN,
            data_cadastro TIMESTAMP
        );
        """)

        # Criar tabela produto
        self.session.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id UUID PRIMARY KEY,
            nome TEXT,
            descricao TEXT,
            preco DECIMAL,
            vendedor_id UUID
        );
        """)

        # Criar tabela compra
        self.session.execute("""
        CREATE TABLE IF NOT EXISTS compra (
            id UUID PRIMARY KEY,
            usuario_id UUID,
            produto_id UUID,
            quantidade INT,
            total DECIMAL,
            vendedor_id UUID,
        );
        """)

        print("Tabelas 'usuario', 'produto' e 'compra' criadas com sucesso.")

    ################################################################################
    def get_connect(self):
        return self.session, self.cluster
    
################################################################################