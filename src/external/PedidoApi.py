import requests
from requests import Response
from os import environ


class PedidoApi:
    def __init__(self):
        self.api_url = environ.get('PEDIDO_API_URL')

    def atualizar_status_pedido(self, id_pedido: str, status: str) -> Response:
        return requests.post(url=f'{self.api_url}/pedido/{id_pedido}/atualizarStatus/', json={"status": status})
