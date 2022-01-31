from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from article.serializers import CommentSerializer
from article.models import Article, Comment

from config.views import BaseView


class CommentCreateAPIView(BaseView, CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classses = [SessionAuthentication, JWTAuthentication]

    def perform_create(self, serializer, article):
        serializer.save(
            user=self.current_user,
            article=article,
        )

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, article)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
