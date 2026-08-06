from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ActivateAccountSerializer
from .services.account_activation_service import AccountActivationService


class ActivateAccountView(APIView):

    def post(self, request):

        serializer = ActivateAccountSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = AccountActivationService.activate_account(
            serializer.validated_data
        )

        return Response(
            {
                "message": "Compte activé avec succès.",
                "email": user.email
            },
            status=status.HTTP_200_OK
        )