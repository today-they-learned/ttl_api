from django.urls import path, re_path

from article.views import (
    ArticleListCreateAPIView,
    ArticleRetrieveUpdateDestroyAPIView,
    CommentCreateAPIView,
)

app_name = "article"

urlpatterns = [
    path("", ArticleListCreateAPIView.as_view()),
    path("<int:id>/", ArticleRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:id>/comment", CommentCreateAPIView.as_view()),
]
