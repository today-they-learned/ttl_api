from django.urls import path

from comment.views import (
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)

app_name = "comment"

urlpatterns = [
    path("", CommentListCreateAPIView.as_view()),
    path("<int:id>/", CommentRetrieveUpdateDestroyAPIView.as_view()),
]
