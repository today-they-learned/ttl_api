from rest_framework.serializers import HyperlinkedModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer

from user.models import User
from tag.serializers import TagListSerializerField, TaggitSerializer


class UserSerializer(
    TaggitSerializer, WritableNestedModelSerializer, HyperlinkedModelSerializer
):
    """Serializer definition for User Model."""

    tags = TagListSerializerField(
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
            "avatar",
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
