from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from article.models import Article
from article.serializers.article_serializer import ArticleSerializer
from article.permissions import IsArticleEditableOrDestroyable
from user.models import Grass
from study.models import Study


class ArticleRetrieveUpdateDestroyAPIView(BaseView, RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated, IsArticleEditableOrDestroyable]

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        user = self.current_user
        Study.add_study_history(article, user)
        Grass.increment_study_count(user)
        article.increment_study_count()

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        Grass.increment_edit_count(self.current_user)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        Grass.increment_edit_count(self.current_user)
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
