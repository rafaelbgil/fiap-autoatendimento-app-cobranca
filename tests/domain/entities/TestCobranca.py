import unittest

from src.domain.entities.Cobranca import Cobranca
from uuid import UUID


class TestCobranca(unittest.TestCase):
    def test_criar_cobranca(self):
        cobranca = Cobranca(id_pedido=1, status='aguardando_pagamento', valor=10, fornecedor_meio_pagto='mercadopago',
                            id='9142dc08-f6b6-48f6-8c19-2b0bb59a1713')
        self.assertIsInstance(cobranca, Cobranca)

    def test_atualizar_status_cobranca(self):
        cobranca = Cobranca(id_pedido=1, status='aguardando_pagamento', valor=10, fornecedor_meio_pagto='mercadopago',
                            id='9142dc08-f6b6-48f6-8c19-2b0bb59a1713')

        cobranca.atualizar_status('recebido')
        self.assertIsInstance(cobranca, Cobranca)
        self.assertEqual(cobranca.status, 'recebido')


    def test_cobranca_retorno_dicionario(self):
        cobranca = Cobranca(id_pedido=1, status='aguardando_pagamento', valor=10, fornecedor_meio_pagto='mercadopago',
                            id='9142dc08-f6b6-48f6-8c19-2b0bb59a1713')
        self.assertIsInstance(cobranca.dicionario(), dict)
