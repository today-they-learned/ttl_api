from django.db import models
from django.utils.translation import gettext_lazy as _


class StudyGroup(models.Model):
    """Model definition for StudyGroup.
    - django.contrib.auth의 Group 모델과 겹치지 않도록 함.
    """

    name = models.CharField(
        verbose_name=_("group name"),
        max_length=100,
        blank=True,
        null=True,
    )  # 그룹명

    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # 그룹 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )  # 그룹 레코드가 수정된 일자

    class Meta:
        """Meta definition for User."""

        verbose_name = "StudyGroup"
        verbose_name_plural = "StudyGroups"
        db_table = "study_groups"

    def __str__(self):
        """Unicode representation of StudyGroup."""
        return self.name
