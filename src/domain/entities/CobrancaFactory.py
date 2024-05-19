from src.domain.entities.Cobranca import Cobranca
from uuid import UUID

class CobrancaFactory:

    @staticmethod
    def from_dict(dicionario_cobranca: dict) -> Cobranca:
        if not 'fornecedor_codigo' in dicionario_cobranca:
            dicionario_cobranca['fornecedor_codigo'] = None
        if not 'pix_codigo' in dicionario_cobranca:
            dicionario_cobranca['pix_codigo'] = None

        if not 'data_criacao' in dicionario_cobranca:
            dicionario_cobranca['data_criacao'] = None

        if not 'cpf' in dicionario_cobranca:
            dicionario_cobranca['cpf'] = None

        if not 'id' in dicionario_cobranca:
            dicionario_cobranca['id'] = None

        if not 'data_vencimento' in dicionario_cobranca:
            dicionario_cobranca['data_vencimento'] = None

        if not 'fornecedor_url_pagamento' in dicionario_cobranca:
            dicionario_cobranca['fornecedor_url_pagamento'] = None

        return Cobranca(id_pedido=dicionario_cobranca['id_pedido'], status=dicionario_cobranca['status'],
                        valor=dicionario_cobranca['valor'],
                        fornecedor_meio_pagto=dicionario_cobranca['fornecedor_meio_pagto'],
                        fornecedor_codigo=dicionario_cobranca['fornecedor_codigo'],
                        fornecedor_url_pagamento=dicionario_cobranca['fornecedor_url_pagamento'],
                        pix_codigo=dicionario_cobranca['pix_codigo'],
                        data_criacao=dicionario_cobranca['data_criacao'], cpf=dicionario_cobranca['cpf'],
                        id=dicionario_cobranca['id'], data_vencimento=dicionario_cobranca['data_vencimento']
                        )
