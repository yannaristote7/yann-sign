from django.db import models
from django.utils import timezone


is_active = models.BooleanField(
    default=True
)


deleted_at = models.DateTimeField(
    null=True,
    blank=True
)

class Company(models.Model):

    name = models.CharField(
        max_length=255
    )


    email = models.EmailField(
        unique=True
    )


    logo = models.URLField(
        blank=True,
        null=True
    )


    is_active = models.BooleanField(
        default=True
    )


    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )