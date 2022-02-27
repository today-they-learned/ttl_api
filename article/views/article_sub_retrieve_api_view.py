from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from article.serializers.article_sub_serializer import ArticleSubSerializer
from config.views import BaseView
from article.models import Article


class ArticleSubRetrieveAPIView(BaseView, RetrieveAPIView):
    serializer_class = ArticleSubSerializer
    queryset = Article.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        article = self.get_object()

        serializer = self.get_serializer(article)
        return Response(serializer.data)
