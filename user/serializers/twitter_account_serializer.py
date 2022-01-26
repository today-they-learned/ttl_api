from rest_framework.serializers import ModelSerializer

from user.models import TwitterAccount


class TwitterAccountSerializer(ModelSerializer):
    """Serializer definition for TwitterAccount Model."""

    class Meta:
        """Meta definition for TwitterAccountSerializer."""

        model = TwitterAccount
        fields = [
            "username",
        ]
