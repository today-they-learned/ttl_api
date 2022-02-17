from django.db.models import Count

from rest_framework.generics import RetrieveAPIView
from config.views import BaseView
from article.models import Article, Feedback
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers


class ArticleSubSerializer(serializers.ModelSerializer):
    feedback = serializers.SerializerMethodField()

    class Meta:
        model = Article

        fields = [
            "id",
            "study_count",
            "feedback",
            "feedback_count",
            "bookmark_count",
        ]

        read_only_fields = [
            "id",
            "study_count",
            "feedback",
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


class ArticleSubRetrieveAPIView(BaseView, RetrieveAPIView):
    serializer_class = ArticleSubSerializer
    queryset = Article.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        article = self.get_object()

        serializer = self.get_serializer(article)
        return Response(serializer.data)