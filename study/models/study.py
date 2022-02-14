from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


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
    count = models.PositiveBigIntegerField(default=0)
    studied_at = models.DateField(
        verbose_name=_("studied at"),
        auto_now_add=True,
    )  # 조회한 일자

    class Meta:
        """Meta definition for Study."""

        verbose_name = "Study"
        verbose_name_plural = "Studys"
        db_table = "studies"

    @classmethod
    def add_study_history(cls, article, user):
        study, _ = cls.objects.get_or_create(
            article=article,
            user=user,
            studied_at=now(),
        )
        study.count += 1

        study.save()
