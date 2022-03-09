from rest_framework.generics import RetrieveUpdateDestroyAPIView

from config.views import BaseView
from article.models import Article
from article.serializers.article_serializer import ArticleSerializer
from article.permissions import IsArticleEditableOrDestroyable
from user.models import Grass
from study.models import Study
from rest_framework.response import Response


class ArticleRetrieveUpdateDestroyAPIView(BaseView, RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all().prefetch_related("bookmarks", "feedbacks")
    permission_classes = [IsArticleEditableOrDestroyable]

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        user = self.current_user

        if self.is_authenticated_user:
            Study.add_study_history(article, user)
            Grass.increment_study_count(user)
            article.increment_study_count()

        serializer = self.get_serializer(article)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        Grass.increment_edit_count(self.current_user)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        Grass.increment_edit_count(self.current_user)
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
