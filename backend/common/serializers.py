"""
common.serializers
------------------
Serializers genéricos base para uso em outros módulos.
"""
from rest_framework import serializers

class BaseSerializer(serializers.Serializer):
    """Serializer genérico base."""
    message = serializers.CharField(read_only=True, default="Sucesso")

class TimestampSerializer(serializers.Serializer):
    """Serializer para models com TimestampMixin."""
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
