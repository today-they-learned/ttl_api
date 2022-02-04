from django.db import models
from django.utils.translation import gettext_lazy as _


class Study(models.Model):
    """Model definition for Study."""

    article = models.ForeignKey(
        "article.Article",
        related_name="studies",
        on_delete=models.CASCADE,
    )  # 조회한 article
    user = models.ForeignKey(
        "user.User",
        related_name="studies",
        on_delete=models.CASCADE,
    )  # 조회한 user
    studied_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # 조회한 일자

    class Meta:
        """Meta definition for Study."""

        verbose_name = "Study"
        verbose_name_plural = "Studys"
        db_table = "studies"
