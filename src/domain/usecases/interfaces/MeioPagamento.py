from abc import ABC, abstractmethod
from src.domain.entities.Cobranca import Cobranca

class MeioPagamento(ABC):
    @staticmethod
    @abstractmethod
    def criar_cobranca(self, cobranca: Cobranca) -> Cobranca:
        pass