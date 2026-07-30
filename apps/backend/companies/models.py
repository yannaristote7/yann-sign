from django.db import models


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


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return self.name