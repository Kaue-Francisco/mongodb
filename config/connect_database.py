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
        URI = "neo4j+ssc://5f44f37b.databases.neo4j.io"
        AUTH = ("neo4j", "E7g8yp5e6BWPwuRyA6PFRWz3n90G-SrlvcJt1WVkUHA")
        
        self.driver = GraphDatabase.driver(URI, auth=AUTH)
        self.driver.verify_connectivity()
        
        # Mensagem de sucesso
        print("Conexão estabelecida com sucesso.")

        return self.driver

################################################################################