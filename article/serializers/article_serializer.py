from django.db.models import Count
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from tag.serializers import TagListSerializerField, TaggitSerializer
from article.models import Article, Feedback
from comment.serializers import CommentSerializer
from user.serializers import UserSerializer


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
    user = UserSerializer(
        read_only=True,
        required=False,
    )
    feedback = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for ArticleSerializer."""

        model = Article
        fields = [
            "id",
            "user",
            "title",
            "content",
            "tags",
            "thumbnail",
            "study_count",
            "feedback_count",
            "bookmark_count",
            "is_bookmarked",
            "feedback",
            "comments",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "study_count",
            "feedback_count",
            "bookmark_count",
            "is_bookmarked",
            "feedback",
            "comments",
            "created_at",
            "updated_at",
        ]

    def get_feedback(self, obj):
        return (
            Feedback.objects.filter(article=obj)
            .values("category")
            .annotate(total=Count("category"))
            .order_by("-total")
        )

    def get_is_bookmarked(self, obj):
        user = self.context["request"].user

        return obj.bookmarks.filter(user=user).exists()
