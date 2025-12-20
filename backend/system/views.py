from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connections
from django.db.utils import OperationalError
import datetime
from rest_framework.permissions import AllowAny


class HealthView(APIView):
    """
    Endpoint simples de healthcheck.
    Retorna 200 OK se o backend está vivo.
    """
    def get(self, request):
        return Response(
            {
                "status": "healthy",
                "service": "backend",
                "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            },
            status=status.HTTP_200_OK,
        )


class StatusView(APIView):
    """
    Endpoint de verificação de status interno.
    Testa dependências como banco de dados.
    """
    def get(self, request):
        db_status = "ok"
        try:
            connections["default"].cursor()
        except OperationalError:
            db_status = "error"

        return Response(
            {
                "status": "ok" if db_status == "ok" else "degraded",
                "database": db_status,
                "service": "backend",
                "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            },
            status=status.HTTP_200_OK,
        )


class ChatView(APIView):
    """
    Endpoint de chat de exemplo.
    Recebe JSON {"input": "..."} via POST e devolve eco + metadados.
    Headers opcionais:
      - x-client-id
      - x-llm-model
    """
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data or {}
        user_input = data.get("input", "")
        client_id = request.headers.get("x-client-id") or request.META.get("HTTP_X_CLIENT_ID")
        llm_model = request.headers.get("x-llm-model") or request.META.get("HTTP_X_LLM_MODEL")

        if not user_input:
            return Response({"error": "Campo 'input' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {
                "reply": f"Você disse: {user_input}",
                "meta": {
                    "client_id": client_id,
                    "llm_model": llm_model,
                    "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                },
            },
            status=status.HTTP_200_OK,
        )
