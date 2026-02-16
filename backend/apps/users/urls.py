"""
Users URL patterns.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserRegistrationView, get_profile, update_profile

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", get_profile, name="profile"),
    path("profile/update/", update_profile, name="profile-update"),
]
