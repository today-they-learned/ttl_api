from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from comment.serializers import CommentSerializer
from article.models import Article
from comment.models import Comment

from config.views import BaseView


class CommentCreateAPIView(BaseView, CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]

    def perform_create(self, serializer, article):
        serializer.save(
            user=self.current_user,
            article=article,
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "article_id",
                openapi.IN_QUERY,
                description="Article ID",
                type=openapi.TYPE_NUMBER,
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["article_id"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, article)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
