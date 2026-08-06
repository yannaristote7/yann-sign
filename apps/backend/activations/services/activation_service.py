from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from activations.models import ActivationToken


class ActivationService:

    @staticmethod
    @transaction.atomic
    def create_token(user):

        ActivationToken.objects.filter(
            user=user
        ).delete()

        token = ActivationToken.objects.create(

            user=user,

            expires_at=timezone.now() + timedelta(
                hours=48
            )

        )

        return token