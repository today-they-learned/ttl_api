from django.urls import path, include
from .views import TagListAPIView

app_name = "tag"

urlpatterns = [
    path("", TagListAPIView.as_view()),
]
