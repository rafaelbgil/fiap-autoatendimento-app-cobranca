from src.domain.entities.Cobranca import Cobranca
from src.domain.usecases.interfaces.MeioPagamento import MeioPagamento
import datetime
import uuid


class AutoMeioPagamento(MeioPagamento):
    def criar_cobranca(self, cobranca: Cobranca) -> Cobranca:
        cobranca.pix_codigo = 'pix' + uuid.uuid4().__str__() + uuid.uuid4().__str__() + uuid.uuid4().__str__()
        cobranca.fornecedor_codigo = int(datetime.datetime.now().timestamp())
        cobranca.data_vencimento = datetime.datetime.now() + datetime.timedelta(minutes=15)
        cobranca.fornecedor_meio_pagto = 'auto'
        return cobranca
