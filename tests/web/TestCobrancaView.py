from unittest.mock import Mock, patch
import unittest
from django.test import Client
from src.domain.entities.Cobranca import Cobranca


class TestCobrancaView(unittest.TestCase):
    @patch('src.web.django_views.CobrancaView.UseCaseCobranca')
    def test_obter_cobranca(self, mock_usecase):

        lista = [Cobranca(1, 'aguardando_pagamento', 9.9, 'mercadopago').__dict__]
        mock_usecase.obter_lista_cobrancas.return_value = lista

        client = Client()
        response = client.get('/cobranca/')
        self.assertEqual(response.status_code, 200)
