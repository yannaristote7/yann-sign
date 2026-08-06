from django.urls import path, include

from core.views import health_check

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path(
        "health/",
        health_check
    ),

    path(
        "auth/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),

    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),

    path(
        "companies/",
        include("companies.urls")
    ),

    path(
       "activations/",
       include("activations.urls"),
    ),

]