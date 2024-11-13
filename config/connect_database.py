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
        URI = "neo4j+ssc://896bedd2.databases.neo4j.io:7687"
        AUTH = ("neo4j", "bpxxe7g7HAiofVvaOjvPXtLhTjmcfZV1RXI0iz8ajqs")
        
        self.driver = GraphDatabase.driver(URI, auth=AUTH)
        self.driver.verify_connectivity()
        
        # Mensagem de sucesso
        print("Conexão estabelecida com sucesso.")

        return self.driver

################################################################################