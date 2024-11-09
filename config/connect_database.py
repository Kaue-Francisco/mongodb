################################################################################]
# Imports

from neo4j import GraphDatabase

################################################################################
class ConnectDatabase:

    def __init__(self):
        self.driver = None

    ################################################################################
    def connect_neo4j(self):
        # Configuração da conexão com o banco de dados
        URI = ""
        AUTH = ("", "")
        
        self.driver = GraphDatabase.driver(URI, auth=AUTH)
        self.driver.verify_connectivity()
        
        # Mensagem de sucesso
        print("Conexão estabelecida com sucesso.")

        return self.driver

################################################################################