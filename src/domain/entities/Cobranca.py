from uuid import UUID, uuid4
from datetime import datetime

from src.utils.validar_uuid import validar_uuid
import copy

def _validar_status(status: str) -> str:
    if status != 'aguardando_pagamento' and status != 'recebido' and status != 'cancelado':
        raise AttributeError(f'Status informado é inválido: {status}')
    return status


class Cobranca:
    id_pedido: int
    status: str
    valor: float
    fornecedor_meio_pagto: str

    fornecedor_codigo: str | None
    pix_codigo: str | None
    data_criacao: datetime | None
    cpf: str | None
    id: UUID | None
    data_vencimento: datetime | None

    def __init__(self, id_pedido: int, status: str, valor: float, fornecedor_meio_pagto: str,
                 fornecedor_codigo: str | None = None, fornecedor_url_pagamento: str | None = None,
                 pix_codigo: str | None = None,
                 data_criacao: datetime | None = None, cpf: str | None = None, id: UUID | None = None,
                 data_vencimento: datetime | None = None):

        self.id_pedido = id_pedido
        self.status = _validar_status(status)
        self.valor = valor
        self.fornecedor_meio_pagto = fornecedor_meio_pagto
        self.fornecedor_codigo = fornecedor_codigo
        self.pix_codigo = pix_codigo
        self.cpf = cpf
        self.fornecedor_url_pagamento = fornecedor_url_pagamento
        self.data_vencimento = data_vencimento
        if not id:
            self.id = uuid4()
        else:
            self.id = validar_uuid(id)

        if not data_criacao:
            self.data_criacao = datetime.now()

    def atualizar_status(self, status: str):
        status_validado = _validar_status(status)
        if self.status == 'recebido' or self.status == 'cancelado':
            raise AttributeError(f'Não é possível alterar status de cobrancas com o status {self.status}')
        self.status = status_validado

    def dicionario(self):
        dicionario = copy.deepcopy(self.__dict__)
        dicionario['id'] = self.id.__str__()
        return dicionario