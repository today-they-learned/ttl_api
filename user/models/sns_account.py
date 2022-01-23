from django.db import models
from django.utils.translation import ugettext_lazy as _


class SnsAccount(models.Model):
    """Abstract Model definition for SnsUser."""

    @staticmethod
    def get_user_related_name():
        return "sns_account"

    username = models.TextField(
        verbose_name=_("username"),
    )

    user = models.ForeignKeyField(
        related_name=get_user_related_name.__func__(),
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        """Meta definition for SnsAccount."""

        abstract = True
        verbose_name = "SnsAccount"
        verbose_name_plural = "SnsAccounts"

    def __str__(self):
        """Unicode representation of SnsAccount."""
        return f"{self.user}: {self.username}"
