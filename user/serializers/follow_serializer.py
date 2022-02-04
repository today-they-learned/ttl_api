from rest_framework.serializers import ModelSerializer

from user.models import Follow

class FollowSerializer(ModelSerializer):
    """Serializer definition for Follow Model."""

    class Meta:
        """"Meta definition for FollowSerializer."""

        model = Follow
        fields = [
            "follower",
            "following",
            "created_at"
        ]
        read_only_fields = [
            "follower",
            "following",
            "created_at"
        ]
