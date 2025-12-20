from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer


class LoginView(TokenObtainPairView):
    """
    Login com email e senha.
    Retorna access + refresh + dados do usuário.
    """
    serializer_class = CustomTokenObtainPairSerializer


class RefreshTokenView(TokenRefreshView):
    """
    Recebe um refresh token e devolve um novo access token.
    """
    pass
