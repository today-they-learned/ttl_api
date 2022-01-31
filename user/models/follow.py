from django.db import models
from django.utils.translation import gettext_lazy as _


class Follow(models.Model):
    """Model definition for Follow."""

    follower = models.ForeignKey(
        "user.User",
        related_name="follower",
        verbose_name=_("follower"),
        on_delete=models.CASCADE
    )   # follow를 하는 user
    following = models.ForeignKey(
        "user.User",
        related_name="following",
        verbose_name=_("following"),
        on_delete=models.CASCADE
    )   # follow를 당하는 user
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )  # Follow 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )  # Follow 레코드가 수정된 일자

    class Meta:
        """Meta definition for Follow."""

        verbose_name = "Follow"
        verbose_name_plural = "Follows"
        db_table = "follows"

    def __str__(self):
        """Unicode representation of Follow."""
        return f"{self.follower} follows {self.following}"