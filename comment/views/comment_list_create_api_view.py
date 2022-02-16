from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from comment.serializers import CommentSerializer
from article.models import Article
from comment.models import Comment

from config.views import BaseView


class CommentListCreateAPIView(BaseView, ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by("created_at")
    permission_classes = [IsAuthenticatedOrReadOnly]

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
        article_id = request.query_params.get("article_id", None)
        article = get_object_or_404(Article, id=article_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, article)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
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
    def get(self, request):
        article_id = request.query_params.get("article_id", None)
        queryset = self.get_queryset().filter(article_id=article_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
