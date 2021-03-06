from django.urls import path

from article.views import (
    ArticleListCreateAPIView,
    ArticleRetrieveUpdateDestroyAPIView,
    ArticleSubRetrieveAPIView,
    BookmarkCreateAPIView,
    BookmarkDestroyAPIView,
    FeedbackCreateAPIView,
    FeedbackDestroyAPIView,
    UploadImageCreateAPIView,
)

app_name = "article"

urlpatterns = [
    path("", ArticleListCreateAPIView.as_view()),
    path("<int:id>/", ArticleRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:id>/sub/", ArticleSubRetrieveAPIView.as_view()),
    path("<int:article_id>/bookmark/", BookmarkCreateAPIView.as_view()),
    path("<int:article_id>/unbookmark/", BookmarkDestroyAPIView.as_view()),
    path("<int:article_id>/feedback/<category>/", FeedbackCreateAPIView.as_view()),
    path("<int:article_id>/feedback/", FeedbackDestroyAPIView.as_view()),
    path("upload_image/", UploadImageCreateAPIView.as_view()),
]
