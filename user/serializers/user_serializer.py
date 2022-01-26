from rest_framework.serializers import ModelSerializer

from user.models import User
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField
from .facebook_account_serializer import FacebookAccountSerializer
from .instagram_account_serializer import InstagramAccountSerializer
from .twitter_account_serializer import TwitterAccountSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserSerializer(TaggitSerializer, WritableNestedModelSerializer):
    """Serializer definition for User Model."""

    tags = TagListSerializerField()
    facebook_account = FacebookAccountSerializer()
    instagram_account = InstagramAccountSerializer()
    twitter_account = TwitterAccountSerializer()

    class Meta:
        """Meta definition for UserSerializer."""

        model = User
        fields = [
            "id",
            "email",
            "tags",
            "facebook_account",
            "instagram_account",
            "twitter_account",
            "username",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "email",
            "username",
            "created_at",
            "updated_at",
        ]
