import datetime
import logging
import uuid

import requests
from os import environ
from src.domain.entities.Cobranca import Cobranca
from src.domain.usecases.interfaces.MeioPagamento import MeioPagamento


class MercadoPagoMeioPagamento(MeioPagamento):
    token: str

    def __init__(self, token=None):
        self.token = token
        if not token:
            self.token = environ.get('MERCADOPAGO_TOKEN')

    def criar_cobranca(self, cobranca: Cobranca) -> Cobranca:
        email_comprador = environ.get('MERCADOPAGO_EMAIL')
        data_vencimento = datetime.datetime.now() + datetime.timedelta(minutes=15)
        data_vencimento_mercadopago = str(data_vencimento.year) + '-' + str(data_vencimento.strftime('%m')) + '-' + \
                                      str(data_vencimento.strftime('%d')) + 'T' + \
                                      data_vencimento.time().__str__()[:8] + '.000-03:00'
        dados_cobranca = {
            "statement_descriptor": "Lanchonete Fiap",
            # "notification_url": 'https://localhost',
            "date_of_expiration": data_vencimento_mercadopago,
            "transaction_amount": float(cobranca.valor),
            "description": f'Pedido Fiap Lanchonete - {cobranca.id_pedido}',
            "payment_method_id": 'pix',
            "installments": 1,
            "payer": {
                "entity_type": "individual",
                "type": "customer",
                "email": email_comprador,
            }
        }
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % (self.token),
            'X-Idempotency-Key': uuid.uuid4().__str__()
        }
        try:
            cobranca_mercadopago = requests.post('https://api.mercadopago.com/v1/payments', json=dados_cobranca,
                                                 headers=header)

            if cobranca_mercadopago.status_code == 200 or cobranca_mercadopago.status_code == 201:
                cobranca.fornecedor_codigo = cobranca_mercadopago.json()['id']
                cobranca.pix_codigo = cobranca_mercadopago.json()['point_of_interaction']['transaction_data']['qr_code']
                cobranca.fornecedor_url_pagamento = \
                cobranca_mercadopago.json()['point_of_interaction']['transaction_data']['ticket_url']
                cobranca.data_vencimento = datetime.datetime.fromisoformat(
                    cobranca_mercadopago.json()['date_of_expiration'])
                return cobranca
            else:
                raise Exception('Nao foi possivel criar cobranca no mercadopago')

        except Exception as e:
            raise Exception(f'nao foi possivel criar a cobranca no mercadopago {e.__str__()}')
