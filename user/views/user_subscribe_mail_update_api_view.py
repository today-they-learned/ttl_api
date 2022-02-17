from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from config.views import BaseView
from user.models import User
from rest_framework.serializers import ModelSerializer
from tag.serializers import TagListSerializerField, TaggitSerializer


class UserSubscribeMailSerializer(TaggitSerializer, ModelSerializer):

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


class UserSubscribeMailUpdateApiView(BaseView, GenericAPIView):
    """POST: /users/user/subscribe_mail"""

    serializer_class = UserSubscribeMailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="""
            POST: /users/user/subscribe_mail

            ### params
            - subscribe_recommended_mail
        """
    )
    def post(self, request, *args, **kwargs):
        user = self.current_user

        subscribe_recommended_mail = (
            request.data.get("subscribe_recommended_mail", None) == "true"
        )

        user.subscribe_recommended_mail = subscribe_recommended_mail
        user.save()

        serializer = self.get_serializer(user)
        return Response(serializer.data)
