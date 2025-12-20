from django.contrib.auth.hashers import check_password
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import User
from .serializers import UserSerializer
from .services.user_service import AccountApplicationService


class UserViewSet(viewsets.ModelViewSet):
    """
    Gateway REST para CRUD de usuários via Service Layer.
    Integra camada de domínio (AccountApplicationService) com o Django REST Framework.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # ----------------------------------------------------------------------
    # CREATE USER (usando camada de serviço)
    # ----------------------------------------------------------------------
    def perform_create(self, serializer):
        email = serializer.validated_data.get("email")
        full_name = serializer.validated_data.get("full_name", "")
        password = serializer.validated_data.get("password", None)

        entity = AccountApplicationService.create_user(
            email=email, full_name=full_name, password=password
        )
        serializer.instance = User.objects.get(id=entity.id)

    # ----------------------------------------------------------------------
    # ACTIVATE USER
    # ----------------------------------------------------------------------
    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        """Ativa um usuário pelo ID (endpoint: /api/accounts/users/{id}/activate/)."""
        try:
            user = AccountApplicationService.activate_user(pk)
            return Response({"detail": f"Usuário {user.email} ativado com sucesso."})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # ----------------------------------------------------------------------
    # VERIFY EMAIL
    # ----------------------------------------------------------------------
    @action(detail=True, methods=["post"])
    def verify(self, request, pk=None):
        """Verifica o e-mail de um usuário (endpoint: /api/accounts/users/{id}/verify/)."""
        try:
            user = AccountApplicationService.verify_email(pk)
            return Response({"detail": f"Usuário {user.email} verificado com sucesso."})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # ----------------------------------------------------------------------
    # PROFILE: GET /me/
    # ----------------------------------------------------------------------
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Retorna o perfil do usuário autenticado.
        Endpoint: GET /api/accounts/users/me/
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    # ----------------------------------------------------------------------
    # UPDATE PROFILE
    # ----------------------------------------------------------------------
    @action(detail=False, methods=["patch"], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        """
        Atualiza os dados do usuário autenticado.
        Endpoint: PATCH /api/accounts/users/update_profile/
        """
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ----------------------------------------------------------------------
    # CHANGE PASSWORD
    # ----------------------------------------------------------------------
    @action(detail=False, methods=["put"], permission_classes=[IsAuthenticated])
    def change_password(self, request):
        """
        Altera a senha do usuário autenticado.
        Endpoint: PUT /api/accounts/users/change_password/
        """
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            return Response(
                {"detail": "Campos 'old_password' e 'new_password' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(old_password, user.password):
            return Response(
                {"detail": "Senha antiga incorreta."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save(update_fields=["password"])

        return Response(
            {"detail": "Senha atualizada com sucesso."},
            status=status.HTTP_200_OK
        )
