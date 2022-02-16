from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response

from article.serializers import FeedbackSerializer
from article.models import Feedback, Article
from article.models.feedback import CATEGORY_CHOICES
from config.views import BaseView


class FeedbackCreateAPIView(
    BaseView,
    generics.CreateAPIView,
):
    """FeedbackCreateView
    POST: api/articles/<article_id>/feedback/<category>
    - Article(article)에 현재 유저가 Feedback(feedback)을 생성
    """

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def __init__(self):
        self.CATEGORY_CHOICES = (
            ("thumbs_up", "thumbs_up"),
            ("heart", "heart"),
            ("clap", "clap"),
            ("lion", "lion"),
            ("thinking", "thinking"),
            ("smile", "smile"),
            ("clover", "clover"),
            ("eyes", "eyes"),
            ("perfect", "perfect"),
            ("bulb", "bulb"),
        )

    def create(self, request, category, article_id, *args, **kwargs):
        article = get_object_or_404(Article, id=article_id)

        if Feedback.objects.filter(article=article, user=self.current_user).count() > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for _category, _ in CATEGORY_CHOICES:
            if _category == category:
                break
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(
            user=self.current_user,
            article=article,
            category=category,
        )
        article.increment_feedback_count()

        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
