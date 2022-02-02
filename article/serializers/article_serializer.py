from rest_framework.serializers import ModelSerializer

from article.models import Article
from comment.serializers import CommentSerializer


class ArticleSerializer(ModelSerializer):
    """Serializer definition for Article Model."""

    comments = CommentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article
        fields = [
            "id",
            "user",
            "title",
            "content",
            "comments",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "comments",
            "created_at",
            "updated_at",
        ]
