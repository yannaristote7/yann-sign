from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company


class User(AbstractUser):

    class Role(models.TextChoices):

        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
        COMPANY_ADMIN = "COMPANY_ADMIN", "Company Admin"
        EMPLOYEE = "EMPLOYEE", "Employee"


    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.EMPLOYEE
    )


    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="users",
        null=True,
        blank=True
    )


    phone = models.CharField(
        max_length=20,
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
        return self.username