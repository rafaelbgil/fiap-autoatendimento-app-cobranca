from src.gateway.CobrancaRepository import CobrancaRepository
from src.domain.entities.Cobranca import Cobranca
from src.domain.usecases.interfaces.MeioPagamento import MeioPagamento


class UseCaseCobranca:
    @staticmethod
    def adicionar_cobranca(respository: CobrancaRepository, cobranca: Cobranca,
                           meio_pagamento: MeioPagamento) -> Cobranca:
        cobranca_meio_pagamento = meio_pagamento.criar_cobranca(cobranca=cobranca)
        return respository.adicionar_cobranca(cobranca_meio_pagamento)

    @staticmethod
    def obter_cobranca(repository: CobrancaRepository, id: str):
        return repository.obter_cobranca(id=id)


    @staticmethod
    def obter_cobranca_por_id_pedido(repository: CobrancaRepository, id: str):
        return repository.obter_cobranca_por_id_pedido(int(id))

    @staticmethod
    def obter_lista_cobrancas(repository: CobrancaRepository):
        return repository.obter_lista_cobrancas()