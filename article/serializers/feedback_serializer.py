from rest_framework.serializers import ModelSerializer

from article.models import Feedback


class FeedbackSerializer(ModelSerializer):
    """Serializer definition for Feedback Model."""

    class Meta:
        """ "Meta definition for FeedbackSerializer."""

        model = Feedback
        fields = [
            "article",
            "created_at",
            "user",
            "category",
        ]
        read_only_fields = [
            "article",
            "created_at",
            "user",
            "category",
        ]
