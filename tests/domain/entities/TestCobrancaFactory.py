import unittest

from src.domain.entities.CobrancaFactory import CobrancaFactory
from src.domain.entities.Cobranca import Cobranca
class TestCobrancaFactory(unittest.TestCase):
    def setUp(self):
        self.dicionario_cobranca_simples = {
            "id_pedido" : 123456,
            "status" : "aguardando_pagamento",
            "valor" : 10.90,
            "fornecedor_meio_pagto" : "mercadopago"
        }

    def test_criar_cobranca_por_dicionario(self):
        cobranca = CobrancaFactory.from_dict(self.dicionario_cobranca_simples)
        self.assertIsInstance(cobranca, Cobranca)
        self.assertEqual(cobranca.status, 'aguardando_pagamento')


