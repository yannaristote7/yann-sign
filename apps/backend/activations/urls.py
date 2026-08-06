from django.urls import path

from .views import ActivateAccountView


urlpatterns = [
    path(
        "activate/",
        ActivateAccountView.as_view(),
        name="activate-account",
    ),
]