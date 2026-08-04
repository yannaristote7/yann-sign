
from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    admin_first_name = serializers.CharField(
        write_only=True,
        required=False
    )

    admin_last_name = serializers.CharField(
        write_only=True,
        required=False
    )

    admin_email = serializers.EmailField(
        write_only=True,
        required=False
    )


    class Meta:

        model = Company

        fields = [
            "id",
            "name",
            "email",
            "logo",
            "is_active",
            "created_at",
            "updated_at",

            "admin_first_name",
            "admin_last_name",
            "admin_email",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


    def create(self, validated_data):

        from companies.services import CompanyService

        return CompanyService.create_company(
            validated_data
        )

