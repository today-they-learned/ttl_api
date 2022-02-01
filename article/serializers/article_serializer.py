from rest_framework.serializers import ModelSerializer

from article.models import Article


class ArticleSerializer(ModelSerializer):
    """Serializer definition for Article Model."""

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article
        fields = [
            "id",
            "user",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "created_at",
            "updated_at",
        ]
