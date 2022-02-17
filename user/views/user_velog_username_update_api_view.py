from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from config.views import BaseView
from user.models import User
from rest_framework.serializers import ModelSerializer
from tag.serializers import TagListSerializerField, TaggitSerializer


class UserVelogUsernameSerializer(TaggitSerializer, ModelSerializer):

    tags = TagListSerializerField(
        required=False,
        read_only=True,
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
            "introduce",
            "repository",
            "subscribe_recommended_mail",
            "avatar",
            "tags",
            "facebook_account",
            "instagram_account",
            "twitter_account",
            "username",
            "created_at",
            "updated_at",
        ]


class UserVelogUsernameUpdateApiView(BaseView, GenericAPIView):
    """POST: /users/user/velog_username"""

    serializer_class = UserVelogUsernameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="""
            POST: /users/user/velog_username

            ### params
            - velog_username
        """
    )
    def post(self, request, *args, **kwargs):
        user = self.current_user

        velog_username = request.data.get("velog_username", None)

        user.velog_username = velog_username
        user.save()

        serializer = self.get_serializer(user)
        return Response(serializer.data)
