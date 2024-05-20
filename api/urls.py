from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # api endpoints
    path('cobranca/', views.CobrancaView.as_view(), name="cobranca"),
    path('cobranca/<str:id>/', views.CobrancaDetalhesView.as_view(), name="cobranca_detalhes"),
    path('cobranca/obter_por_id_pedido/<str:id>/', views.CobrancaPorIdPedidoView.as_view(), name="cobranca_por_id_pedido"),
    path('cobranca/webhook/<str:id>/', views.CobrancaWebHookView.as_view(), name="cobranca_por_id_pedido"),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swager and redoc:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
