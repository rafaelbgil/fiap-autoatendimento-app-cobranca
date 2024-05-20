import pymongo
from os import environ
from src.domain.entities.Cobranca import Cobranca
from src.domain.entities.CobrancaFactory import CobrancaFactory
from src.gateway.CobrancaRepository import CobrancaRepository


class CobrancaMongodbRepository(CobrancaRepository):

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

        if self.obter_cobranca_por_id_pedido(cobranca.id_pedido):
            raise AttributeError(
                f'Nao foi possível criar a cobranca. Já existe uma cobranca com o id de pedido {cobranca.id_pedido}')

        try:
            self.collection.insert_one(cobranca.dicionario())
            return cobranca
        except Exception as e:
            raise Exception('Nao foi possivel adicionar a cobranca')

    def obter_cobranca(self, id: str) -> Cobranca:
        try:
            return CobrancaFactory.from_dict(self.collection.find_one({"id": id}))
        except Exception as e:
            return None

    def atualizar_cobranca(self, id: str, status_novo: str):
        try:
            cobranca = self.obter_cobranca(id)
            cobranca.atualizar_status(status=status_novo)
            self.collection.update_one({'id': id}, {"$set": cobranca.dicionario()})
            return cobranca
        except Exception as e:
            raise Exception(f'Nao foi possivel atualizar a cobranca {e.__str__()}')

    def obter_lista_cobrancas(self):
        lista_cobrancas = []
        for cobranca_mongodb in self.collection.find():
            cobranca = CobrancaFactory.from_dict(cobranca_mongodb)
            print(cobranca.dicionario())
            lista_cobrancas.append(cobranca.dicionario())
        return lista_cobrancas

    def obter_cobranca_por_id_pedido(self, id: int):
        try:
            return CobrancaFactory.from_dict(self.collection.find_one({"id_pedido": id}))
        except Exception as e:
            return None
