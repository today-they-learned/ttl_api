from django.db.models import Count
from rest_framework import serializers

from article.models import Article, Feedback


class ArticleSubSerializer(serializers.ModelSerializer):
    """Serializer definition for Article Model."""

    feedback = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()
    is_feedbacked = serializers.SerializerMethodField()

    class Meta:
        """Meta definition for ArticleSubSerializer."""
        model = Article

        fields = [
            "id",
            "study_count",
            "feedback",
            "is_bookmarked",
            "is_feedbacked",
            "feedback_count",
            "bookmark_count",
        ]

        read_only_fields = [
            "id",
            "study_count",
            "feedback",
            "is_bookmarked",
            "is_feedbacked",
            "feedback_count",
            "bookmark_count",
        ]

    def get_feedback(self, obj):
        return (
            Feedback.objects.filter(article=obj)
            .values("category")
            .annotate(total=Count("category"))
            .order_by("-total")
        )

    def get_is_bookmarked(self, obj):
        try:
            user = self.context["request"].user

            return obj.bookmarks.filter(user=user).exists()
        except:
            return False

    def get_is_feedbacked(self, obj):
        try:
            user = self.context["request"].user

            return obj.feedbacks.filter(user=user).exists()
        except:
            return False
