from rest_framework.serializers import ModelSerializer

from user.models import InstagramAccount


class InstagramAccountSerializer(ModelSerializer):
    """Serializer definition for InstagramAccount Model."""

    class Meta:
        """Meta definition for InstagramAccountSerializer."""

        model = InstagramAccount
        fields = [
            "username",
        ]
