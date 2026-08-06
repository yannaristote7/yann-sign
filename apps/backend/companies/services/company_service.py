from django.db import transaction
from rest_framework.exceptions import ValidationError

from accounts.models import User
from companies.models import Company

from activations.services.activation_service import ActivationService
from core.services.email_service import EmailService


class CompanyService:

    @staticmethod
    @transaction.atomic
    def create_company(validated_data):

        admin_first_name = validated_data.pop(
            "admin_first_name",
            None
        )

        admin_last_name = validated_data.pop(
            "admin_last_name",
            None
        )

        admin_email = validated_data.pop(
            "admin_email",
            None
        )

        if admin_email and User.objects.filter(
            email=admin_email
        ).exists():

            raise ValidationError({
                "admin_email": 
                "Un utilisateur avec cette adresse e-mail existe déjà."
            })


        company = Company.objects.create(
            **validated_data
        )


        admin = User.objects.create(
            username=admin_email,
            email=admin_email,
            first_name=admin_first_name,
            last_name=admin_last_name,
            company=company,
            role=User.Role.COMPANY_ADMIN,
            is_active=False,
        )


        admin.set_unusable_password()
        admin.save()


        token = ActivationService.create_token(
            user=admin
        )


        activation_link = (
            f"http://localhost:3000/activate/{token.token}"
        )


        EmailService.send_email(
            subject="Activation de votre compte YANN Sign",
            message=f"""
Bonjour {admin.first_name},

Votre compte administrateur pour {company.name}
a été créé.

Veuillez activer votre compte via ce lien :

{activation_link}

Ce lien expire dans 24 heures.

L'équipe YANN Sign
""",
            recipient_list=[
                admin.email
            ]
        )


        return company