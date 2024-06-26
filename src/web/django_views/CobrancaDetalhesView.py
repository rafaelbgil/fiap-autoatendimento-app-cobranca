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


class CobrancaDetalhesView(APIView):
    """
    Api para gerenciamento de cobranças
    """
    serializer_class = CobrancaSerializer

    def get(self, request, id: str):
        """
        Obtém cobranca
        """
        cobranca = UseCaseCobranca.obter_cobranca(repository=CobrancaMongodbRepository(), id=id)
        if not cobranca:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data=cobranca.dicionario(), status=status.HTTP_200_OK)
