from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username == "admin" and password == "123456":
            return Response(
                {
                    "access_token": "fake-jwt-token-1234567890",
                    "refresh_token": "fake-refresh-token-abcdefg",
                    "user": {
                        "username": "admin",
                        "role": "superuser"
                    }
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Credenciais inválidas."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
