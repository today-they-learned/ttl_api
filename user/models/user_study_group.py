from django.db import models

from django.utils.translation import gettext_lazy as _


class UserStudyGroup(models.Model):
    """Model definition for UserStudyGroup."""

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
    )
    study_group = models.ForeignKey(
        "user.StudyGroup",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # 유저 그룹 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )  # 유저 그룹 레코드가 수정된 일자

    class Meta:
        """Meta definition for UserStudyGroup."""

        verbose_name = "UserStudyGroup"
        verbose_name_plural = "UserStudyGroup"
        db_table = "user_study_groups"
