from uuid import UUID, uuid4
from datetime import datetime

from src.uitls.validar_uuid import validar_uuid


def _validar_status(status: str) -> str:
    if status != 'aguardando_pagamento' and status != 'recebido' and status != 'cancelado':
        raise AttributeError(f'Status informado é inválido: {status}')
    return status


class Cobranca:
    id_pedido: int
    status: str
    valor: float
    fornecedor_meio_pagto: str
    pix_codigo: str
    data_criacao: datetime | None

    cpf: str | None
    id: UUID | str | None
    data_vencimento: datetime | None

    def __init__(self, id_pedido: int, status: str, valor: float, fornecedor_meio_pagto: str, pix_codigo: str,
                 data_criacao: datetime | None = None, cpf: str | None = None, id: UUID | None = None,
                 data_vencimento: datetime | None = None):

        self.id_pedido = id_pedido
        self.status = _validar_status(status)
        self.valor = valor
        self.fornecedor_meio_pagto = fornecedor_meio_pagto
        self.pix_codigo = pix_codigo
        self.cpf = cpf
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
