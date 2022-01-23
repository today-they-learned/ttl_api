from rest_framework.serializers import ModelSerializer

from user.models import User
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField


class UserSerializer(TaggitSerializer, ModelSerializer):
    """Serializer definition for User Model."""

    tags = TagListSerializerField()

    class Meta:
        """Meta definition for UserSerializer."""

        model = User
        fields = [
            "id",
            "email",
            "tags",
            "username",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at",
        ]
