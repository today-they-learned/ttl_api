from django.urls import path

from comment.views import (
    CommentCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)

app_name = "comment"

urlpatterns = [
    path("", CommentCreateAPIView.as_view()),
    path("<int:id>/", CommentRetrieveUpdateDestroyAPIView.as_view()),
]
