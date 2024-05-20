from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

from api.serializers import CobrancaSerializer, CobrancaCreateSerializer

from src.domain.usecases.UseCaseCobranca import UseCaseCobranca
from src.db.CobrancaMongodbRepository import CobrancaMongodbRepository
from src.domain.entities.CobrancaFactory import CobrancaFactory
from src.external.MercadoPagoMeioPagamento import MercadoPagoMeioPagamento
from src.external.AutoMeioPagamento import AutoMeioPagamento


class CobrancaView(APIView):
    """
    Api para gerenciamento de cobranças
    """
    serializer_class = CobrancaSerializer

    def get(self, request):
        """
        Obtém lista de cobranças
        """
        lista_cobrancas = UseCaseCobranca.obter_lista_cobrancas(repository=CobrancaMongodbRepository())
        return Response(data=lista_cobrancas, status=status.HTTP_200_OK)

    @extend_schema(summary='Adicionar nova cobranca', examples=[
        OpenApiExample('Exemplo de uso',
                       value={"id_pedido": 1,
                              "status": 'aguardando_pagamento', "valor": 10.7, "fornecedor_meio_pagto": "auto"},
                       request_only=True,
                       response_only=False,
                       )
    ])
    def post(self, request):
        """
        Cria nova cobranca
        """

        cobranca = CobrancaFactory.from_dict(request.data)

        if request.data['fornecedor_meio_pagto'] == 'mercadopago':
            meio_pagamento = MercadoPagoMeioPagamento()
        elif request.data['fornecedor_meio_pagto'] == 'auto':
            meio_pagamento = AutoMeioPagamento()
        else:
            raise AttributeError('Meio de pagamento invalida. opcoes validas: ["mercadopago" , "auto"]')

        retorno_cobranca = UseCaseCobranca.adicionar_cobranca(respository=CobrancaMongodbRepository(),
                                                              cobranca=cobranca,
                                                              meio_pagamento=meio_pagamento)

        return Response(data=retorno_cobranca.dicionario(), status=status.HTTP_201_CREATED)
