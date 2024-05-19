import unittest
from unittest.mock import Mock, patch

from src.external.MercadoPagoMeioPagamento import MercadoPagoMeioPagamento
from src.domain.entities.Cobranca import Cobranca


class TestMercadoPagoMeioPagamento(unittest.TestCase):
    @patch('src.external.MercadoPagoMeioPagamento.requests')
    def test_criar_cobranca(self, mock_requests):
        cobranca = Cobranca(1, status='aguardando_pagamento', valor=7.5, fornecedor_meio_pagto='mercadopago')
        mercadopago = MercadoPagoMeioPagamento()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id" : 123456,
            "date_of_expiration": "2024-05-19T15:51:27.069995",
            "point_of_interaction": {
                "transaction_data": {
                    "qr_code": "testeqrcode",
                    "ticket_url": 'https://mercadopago.com/teste'
                }
            }
        }
        mock_requests.post.return_value = mock_response
        cobranca_mp = mercadopago.criar_cobranca(cobranca)

        self.assertIsInstance(cobranca_mp, Cobranca)
        self.assertEqual(cobranca_mp.pix_codigo, 'testeqrcode')