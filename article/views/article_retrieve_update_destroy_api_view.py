from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from article.models import Article
from article.serializers.article_serializer import ArticleSerializer
from article.permissions import IsArticleEditableOrDestroyable
from study.models import Study


class ArticleRetrieveUpdateDestroyAPIView(BaseView, RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated, IsArticleEditableOrDestroyable]

    def get(self, request, *args, **kwargs):
        Study.add_study_history(self.get_object(), self.current_user)

        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
