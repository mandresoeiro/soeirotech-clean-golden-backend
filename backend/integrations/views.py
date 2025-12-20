from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class ExternalPingView(APIView):
    """
    Simula uma chamada externa.
    Útil para testar conectividade de rede e latência.
    """
    def get(self, request):
        try:
            # Simulação de ping a uma API pública (exemplo: GitHub)
            response = requests.get("https://api.github.com", timeout=3)
            if response.status_code == 200:
                return Response(
                    {"external_service": "reachable", "status": "ok"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"external_service": "unreachable", "status": "error"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        except requests.RequestException:
            return Response(
                {"external_service": "error", "status": "unreachable"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
