from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer do usuário customizado."""
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'is_active', 'is_verified', 'date_joined']
        read_only_fields = ['id', 'date_joined']
