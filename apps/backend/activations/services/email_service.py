from core.services.email_service import EmailService


class ActivationEmailService:

    @staticmethod
    def send_activation_email(user, token):

        activation_link = (
            f"http://localhost:3000/activate/{token.token}"
        )

        subject = "Activation de votre compte"

        message = f"""
Bonjour {user.first_name},

Votre compte a été créé.

Cliquez sur le lien suivant afin de choisir votre mot de passe :

{activation_link}

Ce lien est valable pendant 24 heures.

L'équipe YANN Sign
"""

        EmailService.send_email(
            subject=subject,
            message=message,
            recipient_list=[
                user.email
            ],
        )