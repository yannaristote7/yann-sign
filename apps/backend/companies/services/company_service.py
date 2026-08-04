from django.db import transaction

from companies.models import Company


class CompanyService:

    @staticmethod
    @transaction.atomic
    def create_company(
        validated_data
    ):

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


        company = Company.objects.create(
            **validated_data
        )


        return company