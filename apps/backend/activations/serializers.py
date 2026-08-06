from rest_framework import serializers


class ActivateAccountSerializer(serializers.Serializer):

    token = serializers.UUIDField()

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    password_confirmation = serializers.CharField(
        write_only=True,
        min_length=8
    )


    def validate(self, data):

        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError(
                "Les mots de passe ne correspondent pas."
            )

        return data