from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from article.models import Bookmark, article
from article.serializers import BookmarkSerializer
from article.models import Article

class BookmarkListCreateAPIView(BaseView,
                                generics.ListCreateAPIView, generics.GenericAPIView):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def create(self, request, article_id, *args, **kwargs):
        try:
            #중복 북마크 방지
            bookmark_check = Bookmark.objects.filter(user=self.current_user)
            for bookmark in bookmark_check:
                if article_id == bookmark.article.id:
                    print(article_id,bookmark.article.id)
                    return Response(status=status.HTTP_409_CONFLICT)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            is_article_exist = self.perform_create(serializer,article_id)
            #없는 게시글에 대한 북마크 방지
            if is_article_exist is False:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)       
        except Bookmark.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            is_article_exist = self.perform_create(serializer,article_id)
            #없는 게시글에 대한 북마크 방지
            if is_article_exist is False:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, article_id):
        try:
            article = Article.objects.get(id=article_id)
            serializer.save(user=self.current_user,article=article)
        except Article.DoesNotExist:  
            return False

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
