
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone


class ActivationToken(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activation_token"
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
        
    )

    expires_at = models.DateTimeField()

    used = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def is_valid(self):

        return (
            not self.used
            and timezone.now() < self.expires_at
        )

    def __str__(self):

        return f"{self.user.email}"

class Meta:

    ordering = ["-created_at"]

    indexes = [
        models.Index(fields=["token"]),
        models.Index(fields=["expires_at"]),
    ]