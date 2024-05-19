import unittest

from src.external.AutoMeioPagamento import AutoMeioPagamento
from src.domain.entities.Cobranca import Cobranca

class TestAutoMeioPagamento(unittest.TestCase):
    def test_criar_cobranca(self):
        cobranca = Cobranca(1,'aguardando_pagamento', 10.9, 'auto')
        cobranca_meio_pagamento = AutoMeioPagamento().criar_cobranca(cobranca)
        self.assertIsInstance(cobranca_meio_pagamento, Cobranca)