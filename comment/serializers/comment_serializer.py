from rest_framework.serializers import ModelSerializer

from comment.models import Comment


class CommentSerializer(ModelSerializer):
    """Serializer definition for Comment Model."""

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
