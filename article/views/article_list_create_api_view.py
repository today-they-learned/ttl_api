from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from article.serializers.article_serializer import ArticleSerializer
from config.views import BaseView
from article.models import Article
from user.models import Follow
from article.filters import TagsFilter


class ArticleListCreateAPIView(BaseView, ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, TagsFilter]
    search_fields = ["title", "content"]

    def get(self, request, *args, **kwargs):
        """GET: /api/articles/
        Article 목록
        """

        queryset = self.filter_queryset(self.get_queryset())

        tab = request.GET.get("tab")

        if tab is not None:
            if tab == "follow":
                following_user_ids = Follow.objects.filter(
                    follower=self.current_user
                ).values_list("follower__id", flat=True)

                queryset = queryset.filter(user__id__in=following_user_ids)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.current_user)

    def post(self, request, *args, **kwargs):
        """POST: /api/articles/
        Article 생성
        """
        return self.create(request, *args, **kwargs)
