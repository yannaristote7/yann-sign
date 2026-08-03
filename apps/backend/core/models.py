from django.conf import settings
from django.db import models


class AuditLog(models.Model):

    class Action(models.TextChoices):

        LOGIN = "LOGIN", "Connexion"
        LOGOUT = "LOGOUT", "Déconnexion"

        CREATE = "CREATE", "Création"
        UPDATE = "UPDATE", "Modification"
        DELETE = "DELETE", "Suppression"

        DOCUMENT_VIEW = "DOCUMENT_VIEW", "Consultation document"
        DOCUMENT_DOWNLOAD = "DOCUMENT_DOWNLOAD", "Téléchargement"
        DOCUMENT_SIGN = "DOCUMENT_SIGN", "Signature"

        SUPPORT_ACCESS = "SUPPORT_ACCESS", "Accès support"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=50,
        choices=Action.choices
    )

    resource = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Nom de la ressource concernée (Company, User, Document, Signature...)"
    )

    resource_id = models.PositiveBigIntegerField(
        null=True,
        blank=True,
        help_text="Identifiant de la ressource concernée"
    )

    description = models.TextField()

    metadata = models.JSONField(
        default=dict,
        blank=True,
        help_text="Informations complémentaires sur l'action"
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    user_agent = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"]

        indexes = [
            models.Index(fields=["action"]),
            models.Index(fields=["resource"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):

        username = self.user.username if self.user else "Système"

        return (
            f"{username} | "
            f"{self.action} | "
            f"{self.resource or 'N/A'} "
            f"#{self.resource_id if self.resource_id else '-'}"
        )