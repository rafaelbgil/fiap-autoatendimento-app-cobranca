from rest_framework import serializers


class CobrancaSerializer(serializers.Serializer):
    id_pedido = serializers.IntegerField()
    id = serializers.UUIDField(read_only=True)
    status = serializers.CharField(max_length=20)
    valor = serializers.FloatField()
    fornecedor_meio_pagto = serializers.CharField(max_length=20)
    pix_codigo = serializers.CharField(max_length=300)
    cpf = serializers.CharField(max_length=11, min_length=11, required=False)
    data_vencimento = serializers.DateTimeField()
    data_criacao = serializers.DateTimeField(required=False)
