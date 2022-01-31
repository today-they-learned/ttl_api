from django.db import models

from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    """Model definition for Comment."""

    article = models.ForeignKey(
        "article.Article",
        related_name="comments",
        on_delete=models.CASCADE,
    )  # 댓글이 작성된 article
    user = models.ForeignKey(
        "user.User",
        related_name="comments",
        on_delete=models.CASCADE,
    )  # 댓글을 작성한 user
    content = models.TextField()
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # comment 레코드가 생성된 일저
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )  # comment 레코드가 수정된 일자

    class Meta:
        """Meta definition for Comment."""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comments"
