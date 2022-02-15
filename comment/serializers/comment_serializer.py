from rest_framework.serializers import ModelSerializer

from comment.models import Comment

from user.serializers import UserSerializer


class CommentSerializer(ModelSerializer):
    """Serializer definition for Comment Model."""

    user = UserSerializer(
        read_only=True,
        required=False,
    )

    class Meta:
        """Meta definition for CommentSerializer."""

        model = Comment
        fields = [
            "id",
            "article_id",
            "user",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "article_id",
            "user",
            "created_at",
            "updated_at",
        ]
