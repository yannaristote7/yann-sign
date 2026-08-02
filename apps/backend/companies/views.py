from django.shortcuts import render

from rest_framework import generics

from .models import Company
from .serializers import CompanySerializer
from .permissions import IsSuperAdmin


class CompanyListCreateView(generics.ListCreateAPIView):
    """
    GET  : liste des entreprises
    POST : création d'une entreprise
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperAdmin]


class CompanyDetailView(generics.RetrieveUpdateAPIView):
    """
    GET   : détail d'une entreprise
    PATCH : modification
    PUT   : remplacement complet
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperAdmin]
