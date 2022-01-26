from rest_framework.serializers import ModelSerializer

from user.models import FacebookAccount


class FacebookAccountSerializer(ModelSerializer):
    """Serializer definition for FacebookAccount Model."""

    class Meta:
        """Meta definition for FacebookAccountSerializer."""

        model = FacebookAccount
        fields = [
            "username",
        ]
