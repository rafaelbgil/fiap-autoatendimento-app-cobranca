import pymongo
from os import environ
from src.domain.entities.Cobranca import Cobranca


class CobrancaMongodbRepository:

    def __init__(self, servidor_mongodb: str | None = None):
        if not servidor_mongodb and not environ.get('MONGODB_SERVER'):
            raise Exception('Defina a variavel de ambiente MONGODB_SERVER ou informe o parametro servidor_mongodb!')

        self.database = servidor_mongodb
        if not servidor_mongodb:
            self.database = environ.get('MONGODB_SERVER')

        self.conexao = pymongo.MongoClient(environ.get('MONGODB_SERVER'))
        self.database = self.conexao.get_database('cobrancas')
        self.collection = self.database.get_collection('cobrancas')

    def adicionar_cobranca(self, cobranca: Cobranca) -> Cobranca:
        try:
            self.collection.insert_one(cobranca.__dict__)
            return cobranca
        except Exception as e:
            raise Exception('Nao foi possivel adicionar a cobranca')

    def obter_cobranca(self, id: str) -> Cobranca:
        try:
            return self.collection.find_one({"id": id})
        except Exception as e:
            raise Exception('Nao foi possivel obter a cobranca')

    def atualizar_cobranca(self, id: str, status_novo: str):
        try:
            self.obter_cobranca(id)
