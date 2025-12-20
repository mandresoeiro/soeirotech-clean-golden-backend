"""
common.mixins
-------------
Mixins reutilizáveis para models e views.
"""
from django.db import models
from rest_framework import status
from rest_framework.response import Response

class TimestampMixin(models.Model):
    """Adiciona campos created_at e updated_at aos models."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ResponseMixin:
    """Facilita criação de respostas padronizadas em views DRF."""

    def success_response(self, data, message="Operação realizada com sucesso."):
        return Response({"message": message, "data": data}, status=status.HTTP_200_OK)

    def error_response(self, error, code=status.HTTP_400_BAD_REQUEST):
        return Response({"error": str(error)}, status=code)
