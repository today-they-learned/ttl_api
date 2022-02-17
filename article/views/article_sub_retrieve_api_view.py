from dataclasses import field
from rest_framework.generics import RetrieveAPIView
from config.views import BaseView
from article.models import Article
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer


class ArticleSubSerializer(ModelSerializer):
    class Meta:
        model = Article

        fields = [
            "id",
            "study_count",
            "feedback_count",
            "bookmark_count",
        ]

        read_only_fields = [
            "id",
            "study_count",
            "feedback_count",
            "bookmark_count",
        ]


class ArticleSubRetrieveAPIView(BaseView, RetrieveAPIView):
    serializer_class = ArticleSubSerializer
    queryset = Article.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        article = self.get_object()

        serializer = self.get_serializer(article)
        return Response(serializer.data)
