from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample

from api.serializers import CobrancaWebHookSerializer

from src.domain.usecases.UseCaseCobranca import UseCaseCobranca
from src.db.CobrancaMongodbRepository import CobrancaMongodbRepository
from src.domain.entities.CobrancaFactory import CobrancaFactory
from src.external.MercadoPagoMeioPagamento import MercadoPagoMeioPagamento
from src.external.AutoMeioPagamento import AutoMeioPagamento
from api.tasks import atualizar_status_pagamento_queue


class CobrancaWebHookView(APIView):
    """
    Api para gerenciamento de cobranças
    """
    serializer_class = CobrancaWebHookSerializer

    def post(self, request, id: str):
        """
        Obtém cobranca
        """
        try:
            cobranca = UseCaseCobranca.atualizar_status_cobranca(repository=CobrancaMongodbRepository(), id=id,
                                                                 status=request.data['status'])
            atualizar_status_pagamento_queue.delay(id_pedido=cobranca.id_pedido, status=request.data['status'])

        except Exception as e:
            return Response(data={"status" : "erro", "detalhes" : e.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        if not cobranca:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data=cobranca.dicionario(), status=status.HTTP_200_OK)
