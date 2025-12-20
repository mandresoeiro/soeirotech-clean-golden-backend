from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


# --------------------------------------------------
# 🌐 View raiz - Teste rápido do backend
# --------------------------------------------------
def root_view(request):
    return JsonResponse({
        "message": "SoeiroTech backend rodando com sucesso 🚀",
        "version": "v1",
        "endpoints": {
            "docs": "/api/docs/",
            "schema": "/api/schema/",
            "accounts": "/api/v1/accounts/",
            "security": "/api/v1/security/",
            "system": "/api/v1/system/",
            "integrations": "/api/v1/integrations/",
        }
    })


# --------------------------------------------------
# 🧭 URLs principais
# --------------------------------------------------
urlpatterns = [
    path("", root_view, name="root"),
    path("admin/", admin.site.urls),

    # Módulos internos (v1)
    path("api/v1/system/", include("system.urls")),
    path("api/v1/integrations/", include("integrations.urls")),
    path("api/v1/security/", include("security.urls")),
    path("api/v1/accounts/", include("accounts.urls")),
]


# --------------------------------------------------
# 📘 Documentação automática (DRF Spectacular)
# --------------------------------------------------
urlpatterns += [
    # Gera o schema OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Interface Swagger UI
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
