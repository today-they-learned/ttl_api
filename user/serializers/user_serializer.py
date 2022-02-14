from rest_framework.serializers import HyperlinkedModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer

from user.models import User
from tag.serializers import TagListSerializerField, TaggitSerializer

from .facebook_account_serializer import FacebookAccountSerializer
from .instagram_account_serializer import InstagramAccountSerializer
from .twitter_account_serializer import TwitterAccountSerializer


class UserSerializer(
    TaggitSerializer, WritableNestedModelSerializer, HyperlinkedModelSerializer
):
    """Serializer definition for User Model."""

    tags = TagListSerializerField(
        required=False,
    )
    facebook_account = FacebookAccountSerializer(
        required=False,
    )
    instagram_account = InstagramAccountSerializer(
        required=False,
    )
    twitter_account = TwitterAccountSerializer(
        required=False,
    )

    class Meta:
        """Meta definition for UserSerializer."""

        model = User
        fields = [
            "id",
            "email",
            "introduce",
            "repository",
            "subscribe_recommended_mail",
            "tags",
            "velog_username",
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

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
