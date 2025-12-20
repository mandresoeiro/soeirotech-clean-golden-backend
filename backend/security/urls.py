from django.urls import path
from .views import LoginView, RefreshTokenView

urlpatterns = [
    path("login/", LoginView.as_view(), name="token_obtain_pair"),
    path("refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]
