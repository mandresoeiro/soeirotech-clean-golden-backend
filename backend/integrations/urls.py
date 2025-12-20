from django.urls import path
from .views import ExternalPingView

urlpatterns = [
    path("ping/", ExternalPingView.as_view(), name="external-ping"),
]
