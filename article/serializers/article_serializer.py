from drf_writable_nested.serializers import WritableNestedModelSerializer

from tag.serializers import TagListSerializerField, TaggitSerializer
from article.models import Article
from comment.serializers import CommentSerializer


class ArticleSerializer(TaggitSerializer, WritableNestedModelSerializer):
    """Serializer definition for Article Model."""

    tags = TagListSerializerField(
        required=False,
        read_only=False,
    )
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
            "tags",
            "study_count",
            "feedback_count",
            "comments",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "study_count",
            "feedback_count",
            "comments",
            "created_at",
            "updated_at",
        ]
