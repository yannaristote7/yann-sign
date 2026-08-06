from django.db import transaction

from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import AuditLog
from core.services import create_audit_log

from activations.models import ActivationToken


class AccountActivationService:

    @staticmethod
    @transaction.atomic
    def activate_account(validated_data):

        token_value = validated_data["token"]
        password = validated_data["password"]

        try:
            activation_token = ActivationToken.objects.select_related(
                "user"
            ).get(
                token=token_value
            )

        except ActivationToken.DoesNotExist:
            raise ValidationError({
                "token": "Token d'activation invalide."
            })

        if not activation_token.is_valid():
            raise ValidationError({
                "token": "Ce lien d'activation est expiré ou déjà utilisé."
            })

        user = activation_token.user

        user.set_password(password)
        user.is_active = True
        user.save()

        activation_token.used = True
        activation_token.save()

        create_audit_log(
            user=user,
            action=AuditLog.Action.ACCOUNT_ACTIVATE,
            resource="User",
            resource_id=user.id,
            description="Activation du compte.",
            metadata={
                "email": user.email,
                "role": user.role,
            },
        )

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": user,
        }