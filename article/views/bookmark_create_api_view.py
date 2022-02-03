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
    # def create(self, request, article_id, *args, **kwargs):
    #     try:
    #         bookmark_check = Bookmark.objects.filter(user=self.current_user)
    #         for bookmark in bookmark_check:
    #             if article_id == bookmark.article.id:
    #                 print(article_id,bookmark.article.id)
    #                 return Response(status=status.HTTP_409_CONFLICT)
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         is_article_exist = self.perform_create(serializer,article_id)
    #         if is_article_exist is False:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #         else:
    #             headers = self.get_success_headers(serializer.data)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)       
    #     except Bookmark.DoesNotExist:
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         is_article_exist = self.perform_create(serializer,article_id)
    #         if is_article_exist is False:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #         else:
    #             headers = self.get_success_headers(serializer.data)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, article_id):
        article = Article.objects.get(id=article_id)
        serializer.save(user=self.current_user,article=article)


