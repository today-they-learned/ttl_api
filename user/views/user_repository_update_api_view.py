from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from config.views import BaseView
from user.models import User
from rest_framework.serializers import ModelSerializer
from tag.serializers import TagListSerializerField, TaggitSerializer


class UserRepositorySerializer(TaggitSerializer, ModelSerializer):

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


class UserRepositoryUpdateApiView(BaseView, GenericAPIView):
    """POST: /users/user/repository"""

    serializer_class = UserRepositorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="""
            POST: /users/user/repository

            ### params
            - repository
        """
    )
    def post(self, request, *args, **kwargs):
        user = self.current_user

        repository = request.data.get("repository", None)

        user.repository = repository
        user.save()

        serializer = self.get_serializer(user)
        return Response(serializer.data)
