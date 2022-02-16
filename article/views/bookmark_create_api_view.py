from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from django.shortcuts import get_object_or_404
from article.models import Bookmark, article
from article.serializers import BookmarkSerializer
from article.models import Article


class BookmarkCreateAPIView(BaseView, generics.CreateAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, article_id, *args, **kwargs):
        article = get_object_or_404(Article, id=article_id)
        bookmark, is_created = Bookmark.objects.get_or_create(
            user=self.current_user, article=article
        )

        if not is_created:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        article.increment_bookmark_count()

        return Response(
            BookmarkSerializer(bookmark).data,
            status=status.HTTP_201_CREATED,
        )
