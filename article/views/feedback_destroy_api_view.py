from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated

from config.views import BaseView
from django.shortcuts import get_object_or_404
from article.models import Feedback
from article.serializers import FeedbackSerializer
from article.models import Article
from article.permissions import IsArticleEditableOrDestroyable


class FeedbackDestroyAPIView(
    BaseView, mixins.DestroyModelMixin, generics.GenericAPIView
):
    """FeedbackDestroyAPIView
    DELETE: api/articles/<article_id>/feedback
    Feedback 삭제
    """

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated, IsArticleEditableOrDestroyable]

    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)

        feedback = get_object_or_404(
            Feedback,
            user=self.current_user,
            article=article,
        )
        feedback.delete()
        article.decrement_feedback_count()

        return Response(status=status.HTTP_204_NO_CONTENT)
