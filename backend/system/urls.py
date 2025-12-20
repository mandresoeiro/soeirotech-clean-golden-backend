from django.contrib import admin
from django.urls import path, include
from .views import HealthView, StatusView, ChatView

urlpatterns = [
    # Rotas de monitoramento
    path("health/", HealthView.as_view(), name="health"),
    path("status/", StatusView.as_view(), name="status"),

    # Chat simples (exemplo)
    path("chat/", ChatView.as_view(), name="chat"),

    # Painel administrativo
    path("admin/", admin.site.urls),

    # API principal (módulo accounts)
    path("api/", include("accounts.urls")),
]
