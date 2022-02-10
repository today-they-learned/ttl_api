from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from django.shortcuts import get_object_or_404
from article.models import Bookmark, article
from article.serializers import BookmarkSerializer
from article.models import Article

class BookmarkCreateAPIView(BaseView,
                                generics.CreateAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def create(self, request, article_id, *args, **kwargs):
        article = get_object_or_404(Article, id = article_id)
        bookmark, is_bookmarked = Bookmark.objects.get_or_create(user=self.current_user, article=article)

        if is_bookmarked:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=bookmark)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


