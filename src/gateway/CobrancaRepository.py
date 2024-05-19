from abc import ABC, abstractmethod
from src.domain.entities.Cobranca import Cobranca


class CobrancaRepository(ABC):
    @abstractmethod
    def adicionar_cobranca(self, cobranca: Cobranca) -> Cobranca:
        pass

    @abstractmethod
    def obter_cobranca(self, id: str) -> Cobranca:
        pass

    @abstractmethod
    def obter_cobranca_por_id_pedido(self, id_pedido: int) -> Cobranca:
        pass

    @abstractmethod
    def atualizar_cobranca(self, id: str, status_novo: str) -> Cobranca:
        pass

    @abstractmethod
    def obter_lista_cobrancas(self):
        pass
