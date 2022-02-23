from rest_framework.serializers import ModelSerializer

from user.models import Follow
from user.serializers import UserSerializer


class FollowSerializer(ModelSerializer):
    """Serializer definition for Follow Model."""

    follower = UserSerializer(
        read_only=True,
        required=False,
    )
    following = UserSerializer(
        read_only=True,
        required=False,
    )

    class Meta:
        """Meta definition for FollowSerializer."""

        model = Follow
        fields = ["follower", "following", "created_at"]
        read_only_fields = ["follower", "following", "created_at"]


class FollowerSerializer(ModelSerializer):
    """Serializer definition for Follow Model."""

    follower = UserSerializer(
        read_only=True,
        required=False,
    )

    class Meta:
        """Meta definition for FollowSerializer."""

        model = Follow
        fields = ["follower", "created_at"]
        read_only_fields = ["follower", "created_at"]


class FollowingSerializer(ModelSerializer):
    """Serializer definition for Follow Model."""

    following = UserSerializer(
        read_only=True,
        required=False,
    )

    class Meta:
        """Meta definition for FollowSerializer."""

        model = Follow
        fields = ["following", "created_at"]
        read_only_fields = ["following", "created_at"]
