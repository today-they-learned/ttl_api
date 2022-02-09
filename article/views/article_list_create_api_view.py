from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from article.serializers.article_serializer import ArticleSerializer
from config.views import BaseView
from article.models import Article
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ArticleListCreateAPIView(BaseView, ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        """GET: /api/articles/
        Article 목록
        """
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.current_user)

    def post(self, request, *args, **kwargs):
        """POST: /api/articles/
        Article 생성
        """

        return self.create(request, *args, **kwargs)
