from django.urls import path, re_path

from article.views import (ArticleListCreateAPIView, 
                           ArticleRetrieveUpdateDestroyAPIView,
                           BookmarkCreateAPIView,
                           BookmarkDestroyAPIView)

app_name = "article"

urlpatterns = [
    path("", ArticleListCreateAPIView.as_view()),
    path("<int:id>/", ArticleRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:article_id>/bookmark",BookmarkCreateAPIView.as_view()),
    path("<int:article_id>/unbookmark",BookmarkDestroyAPIView.as_view()),
    
]
