from django.db import models
from django.utils import timezone


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

    phone = models.CharField(max_length=20, blank=True)

    address = models.TextField(blank=True)

    country = models.CharField(max_length=100, blank=True)

    city = models.CharField(max_length=100, blank=True)

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


    def __str__(self):
        return self.name