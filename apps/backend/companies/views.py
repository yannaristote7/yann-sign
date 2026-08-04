
from rest_framework import generics

from core.models import AuditLog
from core.services import create_audit_log

from .models import Company
from .permissions import IsSuperAdmin
from .serializers import CompanySerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    """
    GET  : Liste des entreprises
    POST : Création d'une entreprise
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperAdmin]


    def perform_create(self, serializer):

        serializer.save()

        company = serializer.instance

        create_audit_log(
            user=self.request.user,
            action=AuditLog.Action.CREATE,
            resource="Company",
            resource_id=company.id,
            description=f"Création de l'entreprise '{company.name}'.",
            metadata={
                "company_name": company.name,
                "company_email": company.email,
            },
            ip_address=self.request.META.get("REMOTE_ADDR"),
            user_agent=self.request.META.get(
                "HTTP_USER_AGENT",
                ""
            ),
        )


class CompanyDetailView(generics.RetrieveUpdateAPIView):
    """
    GET   : Détail d'une entreprise
    PATCH : Modification
    PUT   : Remplacement complet
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperAdmin]

