from django.urls import path, include, re_path
from rest_framework_simplejwt import views

from accounts.views.custom_token_view import CustomTokenObtainPairView, LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    re_path(r"^auth/", include("djoser.urls.base")),
    # re_path(r"^auth/", include("djoser.urls.authtoken")),
    # re_path(r"^auth/", include("djoser.urls.jwt")),
    re_path(r"^auth/jwt/create/?", CustomTokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^auth/jwt/refresh/?", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^auth/jwt/verify/?", views.TokenVerifyView.as_view(), name="jwt-verify"),
    re_path(r"^auth/jwt/blacklist/", LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
]
