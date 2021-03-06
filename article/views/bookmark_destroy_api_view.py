from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from django.shortcuts import get_object_or_404
from article.models import Bookmark, article
from article.serializers import BookmarkSerializer
from article.models import Article
from article.permissions import IsArticleEditableOrDestroyable


class BookmarkDestroyAPIView(
    BaseView, mixins.DestroyModelMixin, generics.GenericAPIView
):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    permission_classes = [IsAuthenticated, IsArticleEditableOrDestroyable]

    def delete(self, request, article_id):
        bookmark = get_object_or_404(
            Bookmark, user=self.current_user, article__id=article_id
        )
        bookmark.delete()

        article = get_object_or_404(Article, id=article_id)
        article.decrement_bookmark_count()

        return Response(status=status.HTTP_204_NO_CONTENT)
